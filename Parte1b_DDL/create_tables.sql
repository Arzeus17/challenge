--Se presenta el script DDL, referente a la estructura de las tablas de la base de datos

CREATE TABLE Customer (
    Customer_id INT PRIMARY KEY,
    Email VARCHAR(255),
    Nombre VARCHAR(50),
    Apellido VARCHAR(50),
    Sexo CHAR(1),
    Direccion VARCHAR(255),
    Fecha_Nacimiento DATE,
    Telefono VARCHAR(20)
);

CREATE TABLE Orders (
    Order_id INT PRIMARY KEY,
    Customer_id INT,
    Fecha_Compra DATE,
    FOREIGN KEY (Customer_id) REFERENCES Customer(Customer_id)
);

CREATE TABLE Item (
    Item_id INT PRIMARY KEY,
    nombre VARCHAR(100),
    Descripcion VARCHAR(255),
    Precio DECIMAL(10, 2),
    Estado VARCHAR(20),
    Fecha_Baja DATE,
    Categoria_id INT,
    FOREIGN KEY (Categoria_id) REFERENCES Category(Categoria_id)
);

CREATE TABLE Category (
    Categoria_id INT PRIMARY KEY,
    nombre VARCHAR(50),
    path VARCHAR(50)
);