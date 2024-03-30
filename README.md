CHALLENGER MERCADO LIBRE
Se presenta un Reporte General y detallado de todas las acciones llevadas a cabo para lograr los 
objetivos, y de las herramientas empleadas, puede ubicarlo en: Reporte.ipynb, en el presente Repositorio.


Primera Parte - SQL
Objetivo
A partir de la siguiente necesidad, se requiere diseñar un DER que responda al modelo del
negocio. Luego, se debe responder mediante SQL diferentes preguntas.

Descripción de la necesidad
Teniendo en cuenta el modelo de ecommerce que manejamos, tenemos algunas entidades
básicas que queremos representar: Customer, Order, Item y Category.
A resolver:
1. Listar los usuarios que cumplan años el día de hoy cuya cantidad de ventas
realizadas en enero 2020 sea superior a 1500.
2. Por cada mes del 2020, se solicita el top 5 de usuarios que más vendieron($) en la
categoría Celulares. Se requiere el mes y año de análisis, nombre y apellido del
vendedor, cantidad de ventas realizadas, cantidad de productos vendidos y el monto
total transaccionado.
3. Se solicita poblar una nueva tabla con el precio y estado de los Ítems a fin del día.
Tener en cuenta que debe ser reprocesable. Vale resaltar que en la tabla Item,
vamos a tener únicamente el último estado informado por la PK definida. (Se puede
resolver a través de StoredProcedure)
Backlog de Tareas
A partir de la situación planteada, te pedimos:
● Diseñar un DER del modelo de datos que logre responder cada una de las
preguntas mencionadas anteriormente.
● Generar el script DDL para la creación de cada una de las tablas representadas en
el DER. Enviarlo con el nombre “create_tables.sql”.
● Generar el código SQL para responder cada una de las situaciones mencionadas
anteriormente sobre el modelo diseñado. Nombre solicitado:
“respuestas_negocio.sql”

Segunda Parte - APIs (Deseable)
Objetivo
Realizar un análisis sobre la oferta/vidriera de las opciones de productos que responden a
distintas búsquedas en el sitio Mercadolibre.com.ar
Consignas
1) Barrer una lista de más de 150 ítems ids en el servicio público:
https://api.mercadolibre.com/sites/MLA/search?q=chromecast&limit=50#json
En este caso particular y solo a modo de ejemplo, son resultados para la búsqueda
“chromecast”, pero deberás elegir otros términos para el experimento que permitan
enriquecer el análisis en un hipotético dashboard (ejemplo Google Home, Apple TV,
Amazon Fire TV, o afines para poder comparar dispositivos portátiles, o bien elegir
otros 3 que te interesen para comparar).
2) Por cada resultado, realizar el correspondiente GET por Item_Id al recurso público:
https://api.mercadolibre.com/items/{Item_Id}
3) Escribir los resultados en un archivo plano delimitado por comas, desnormalizando
el JSON obtenido en el paso anterior, en tantos campos como sea necesario para
guardar las variables que te interesen modelar.
