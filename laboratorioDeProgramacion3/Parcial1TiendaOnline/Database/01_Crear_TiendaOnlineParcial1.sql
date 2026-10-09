/* Ejecutar en SQL Server Management Studio con una cuenta que pueda crear bases. */
IF DB_ID('TiendaOnlineParcial1') IS NULL
    CREATE DATABASE TiendaOnlineParcial1;
GO
USE TiendaOnlineParcial1;
GO

IF OBJECT_ID('dbo.categorias', 'U') IS NULL
BEGIN
    CREATE TABLE dbo.categorias (
        idCategoria INT IDENTITY(1,1) NOT NULL CONSTRAINT PK_categorias PRIMARY KEY,
        descripcion VARCHAR(80) NOT NULL CONSTRAINT UQ_categorias_descripcion UNIQUE
    );
END;
GO

IF OBJECT_ID('dbo.productos', 'U') IS NULL
BEGIN
    CREATE TABLE dbo.productos (
        idProducto INT IDENTITY(1,1) NOT NULL CONSTRAINT PK_productos PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        precio DECIMAL(10,2) NOT NULL CONSTRAINT CK_productos_precio CHECK (precio >= 0),
        idCategoria INT NOT NULL,
        CONSTRAINT FK_productos_categorias FOREIGN KEY (idCategoria)
            REFERENCES dbo.categorias(idCategoria)
    );
END;
GO

IF NOT EXISTS (SELECT 1 FROM dbo.categorias)
    INSERT INTO dbo.categorias (descripcion) VALUES ('Tecnología'), ('Hogar'), ('Accesorios'), ('Oficina');
GO

IF NOT EXISTS (SELECT 1 FROM dbo.productos)
BEGIN
    INSERT INTO dbo.productos (nombre, precio, idCategoria) VALUES
    ('Auriculares Bluetooth', 45999.90, (SELECT idCategoria FROM dbo.categorias WHERE descripcion = 'Tecnología')),
    ('Lámpara LED', 18600.00, (SELECT idCategoria FROM dbo.categorias WHERE descripcion = 'Hogar')),
    ('Mochila urbana', 32450.50, (SELECT idCategoria FROM dbo.categorias WHERE descripcion = 'Accesorios')),
    ('Teclado inalámbrico', 39750.00, (SELECT idCategoria FROM dbo.categorias WHERE descripcion = 'Tecnología')),
    ('Cuaderno A5', 5300.00, (SELECT idCategoria FROM dbo.categorias WHERE descripcion = 'Oficina'));
END;
GO

SELECT p.idProducto, p.nombre, p.precio, c.descripcion AS categoria
FROM dbo.productos AS p INNER JOIN dbo.categorias AS c ON p.idCategoria = c.idCategoria;
