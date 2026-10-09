# Parcial 1 - Tienda Online

Proyecto ASP.NET Web Forms para Visual Studio, desarrollado con `SqlDataSource` y SQL Server.

## Puesta en marcha

1. Abrí SQL Server Management Studio y ejecutá `Database/01_Crear_TiendaOnlineParcial1.sql`.
2. En Visual Studio Community 2026, abrí `Parcial1TiendaOnline.slnx` (no la carpeta ni el archivo `.sln`). Es el formato de solución que usa tu instalación y carga el proyecto con IIS Express.
3. Verificá la cadena `TiendaOnlineConnection` de `Web.config`:
   - LocalDB: `(LocalDB)\MSSQLLocalDB` (configurada por defecto).
   - SQL Server Express: `localhost\SQLEXPRESS`.
   - Otra instancia: reemplazá solamente el valor de `Data Source`.
4. Ejecutá con IIS Express (`F5`) y usá `Default.aspx` como página inicial.

## Qué cubre de la consigna

- Esquema relacional: `productos` y `categorias`, con clave primaria, identidad, clave foránea y datos de ejemplo.
- Alta: formulario con `TextBox`, `DropDownList` y `SqlDataSource.Insert()`.
- Consulta: `GridView` enlazado a una consulta `INNER JOIN`.
- Modificación: búsqueda por ID, edición de producto/categoría y validación de cambio previo.
- Baja: `GridView` que elimina solo de `productos`, con confirmación en el navegador.
- Navegación: `HyperLink` desde el inicio a las cuatro páginas y retorno en todas ellas.
- Estilos: hoja externa en `Content/site.css`.

El proyecto se entrega como una **solución ASP.NET Web Forms** estándar, igual al formato de los proyectos de clase: incluye `.sln` y `.csproj`.
