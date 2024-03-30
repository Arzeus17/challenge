/*1° Listar los usuarios que cumplan años el día de hoy cuya cantidad de ventas
realizadas en enero 2020 sea superior a 1500.*/
 
SELECT c.Nombre, c.Apellido
FROM Customer c
INNER JOIN Orders o ON c.Customer_id = o.Customer_id
--Filtro los clientes que que cumplen años hoy
WHERE MONTH(c.Fecha_Nacimiento) = MONTH(NOW()) AND DAY(c.Fecha_Nacimiento) = DAY(NOW())
--Filtro las ordenes realizadas en enero de 2020
AND o.Fecha_Compra BETWEEN '2020-01-01' AND '2020-01-31'
GROUP BY c.Customer_id
--Filtro solo los clientes que tienen mas de 1500 ordenes en enero de 2020
HAVING COUNT(o.order_id) > 1500;


/*2° Por cada mes del 2020, se solicita el top 5 de usuarios que más vendieron($) en la
categoría Celulares. Se requiere el mes y año de análisis, nombre y apellido del
vendedor, cantidad de ventas realizadas, cantidad de productos vendidos y el monto
total transaccionado.*/

--Extraigo por años y mes de compra, y nombre y apellido del comprador
SELECT
    year,
    month,
    Nombre,
    Apellido,
--Estimo la cantidad de ventas, productos y el total transaccionado por vendedor
    cantidad_ventas,
    cantidad_productos,
    monto_total_transaccion
FROM
    (
       --Subconsulto para tener el top 5 de usuarios por mes
       SELECT
            YEAR(o.Fecha_Compra) AS year,
            MONTH(o.Fecha_Compra) AS month, 
            c.Nombre AS Nombre,
            c.Apellido AS Apellido,
            COUNT(o.Order_id) AS cantidad_ventas,
            SUM(o.Cantidad) AS cantidad_productos,
            SUM(o.Monto_Total) AS monto_total_transaccion,
            ROW_NUMBER() OVER (PARTITION BY YEAR(o.Fecha_Compra), MONTH(Fecha_Compra), o.Customer_id ORDER BY SUM(Monto_Total) DESC) AS ranking
        FROM
            Orders o
                INNER JOIN Customer c ON o.Customer_id = c.Customer_id
                INNER JOIN Item i ON o.Item_id = i.Item_id
                INNER JOIN Category cat ON i.Categoria_id = cat.Categoria_id
        --Filtro por la categoria 'Celulares'
        WHERE
            cat.nombre ='Celulares'
            AND o.Fecha_Compra BETWEEN '2020-01-01' AND '2020-12-31'
            GROUP BY 
                YEAR(o.Fecha_Compra), MONTH(o.Fecha_Compra), c.Customer_id
    ) AS top_users_per_month
WHERE
    ranking <= 5 --top 5
ORDER BY
    year, month, monto_total_transaccion;


/*3° Se solicita poblar una nueva tabla con el precio y estado de los Ítems a fin del día.
Tener en cuenta que debe ser reprocesable. Vale resaltar que en la tabla Item,
vamos a tener únicamente el último estado informado por la PK definida. (Se puede
resolver a través de StoredProcedure)*/

DELIMITER //

CREATE PROCEDURE UpdateOrInsertItemPriceAndState()
BEGIN
    --Elimino datos anteriores de la tabla de precios y estados de los items
    TRUNCATE TABLE ItemPriceAndState;

    --Inserto nuevos datos en la tabla de precios y estados de los datos
    INSERT INTO ItemPriceAndState (Item_id, Precio, Estado, Fecha) 
    SELECT i.Item_id, i.Precio, i.Estado, CURDATE() AS Fecha
    FROM Item i
    WHERE i.Fecha_Baja IS NULL; --considero solo los items activos

    --Actualizo registros existentes en la tabla Item
    UPDATE Item i
    JOIN (
        --Subconsulto para identificar el estado mas reciente para cada item
        SELECT Item_id, MAX(Fecha_Baja) AS UltimaFecha
        FROM Item
        GROUP BY Item_id
    ) AS UltimosEstados ON Item_id = UltimosEstados.Item_id
    SET i.Precio = (SELECT Precio FROM Item WHERE Item_id = i.Item_id AND Fecha_Baja = UltimosEstados.UltimaFecha),
        i.Estado = (SELECT Estado FROM Item WHERE Item_id = i.Item_id AND Fecha_Baja = UltimosEstados.UltimaFecha)
    WHERE i.Fecha_Baja = UltimosEstados.UltimaFecha;

    --Inserto nuevos registros en la tabla Item
    INSERT INTO Item (Item_id, Precio, Estado, Fecha_Baja)
    SELECT ips.Item_id, ips.Precio, ips.Estado, ips.Fecha
    FROM ItemPriceAndState ips 
    WHERE NOT EXISTS (
        SELECT 1
        FROM Item WHERE Item.Item_id = ips.Item_id
    );
END//

DELIMITER ;



