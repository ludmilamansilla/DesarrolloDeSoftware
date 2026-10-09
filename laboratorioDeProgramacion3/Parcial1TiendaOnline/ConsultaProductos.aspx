<%@ Page Language="C#" %>
    <!DOCTYPE html>
    <html xmlns="http://www.w3.org/1999/xhtml">

    <head runat="server">
        <meta charset="utf-8" />
        <title>Consulta - Tienda Nova</title>
        <link href="Content/site.css" rel="stylesheet" />
    </head>

    <body>
        <header>
            <div class="container">
                <h1>Tienda Nova</h1>
                <p>Consulta de productos</p>
            </div>
        </header>
        <main class="container">
            <form id="form1" runat="server">
                <section class="card">
                    <h2>Listado del catálogo</h2>
                    <p class="intro">Consulta que relaciona productos con su categoría asignada.</p>
                    <asp:GridView ID="gvProductos" runat="server" DataSourceID="dsConsulta" AutoGenerateColumns="False"
                        CssClass="grid" AllowPaging="True" PageSize="8" AllowSorting="True"
                        EmptyDataText="No hay productos cargados.">
                        <Columns>
                            <asp:BoundField DataField="idProducto" HeaderText="ID" SortExpression="idProducto" />
                            <asp:BoundField DataField="nombre" HeaderText="Producto" SortExpression="nombre" />
                            <asp:BoundField DataField="precio" HeaderText="Precio" DataFormatString="{0:C}"
                                SortExpression="precio" />
                            <asp:BoundField DataField="categoria" HeaderText="Categoría" SortExpression="categoria" />
                        </Columns>
                    </asp:GridView>
                    <asp:HyperLink ID="lnkVolver" runat="server" NavigateUrl="~/Default.aspx" CssClass="return">&larr; Volver
                        al inicio</asp:HyperLink>
                    <asp:SqlDataSource ID="dsConsulta" runat="server"
                        ConnectionString="<%$ ConnectionStrings:TiendaOnlineConnection %>"
                        SelectCommand="SELECT p.idProducto, p.nombre, p.precio, c.descripcion AS categoria FROM productos AS p INNER JOIN categorias AS c ON c.idCategoria = p.idCategoria ORDER BY p.idProducto" />
                </section>
            </form>
        </main>
    </body>

    </html>
