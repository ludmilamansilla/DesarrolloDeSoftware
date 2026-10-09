<%@ Page Language="C#" CodeBehind="BajaProducto.aspx.cs" Inherits="BajaProducto" %>
    <!DOCTYPE html>
    <html xmlns="http://www.w3.org/1999/xhtml">

    <head runat="server">
        <meta charset="utf-8" />
        <title>Baja - Tienda Nova</title>
        <link href="Content/site.css" rel="stylesheet" />
    </head>

    <body>
        <header>
            <div class="container">
                <h1>Tienda Nova</h1>
                <p>Baja de productos</p>
            </div>
        </header>
        <main class="container">
            <form id="form1" runat="server">
                <section class="card">
                    <h2>Eliminar un producto</h2>
                    <p class="hint">La eliminación afecta solamente a la tabla <em>productos</em>; las categorías se
                        conservan.</p>
                    <asp:GridView ID="gvProductos" runat="server" DataSourceID="dsProductos" DataKeyNames="idProducto"
                        AutoGenerateColumns="False" CssClass="grid" AllowPaging="True" PageSize="8"
                        OnRowDeleted="gvProductos_RowDeleted">
                        <Columns>
                            <asp:BoundField DataField="idProducto" HeaderText="ID" />
                            <asp:BoundField DataField="nombre" HeaderText="Producto" />
                            <asp:BoundField DataField="precio" HeaderText="Precio" DataFormatString="{0:C}" />
                            <asp:BoundField DataField="categoria" HeaderText="Categoría" />
                            <asp:CommandField ShowDeleteButton="True" DeleteText="Eliminar" ButtonType="Button" />
                        </Columns>
                    </asp:GridView>
                    <asp:Label ID="lblMensaje" runat="server" CssClass="message" Visible="false" />
                    <asp:HyperLink ID="lnkVolver" runat="server" NavigateUrl="~/Default.aspx" CssClass="return">&larr; Volver
                        al inicio</asp:HyperLink>
                    <asp:SqlDataSource ID="dsProductos" runat="server"
                        ConnectionString="<%$ ConnectionStrings:TiendaOnlineConnection %>"
                        SelectCommand="SELECT p.idProducto, p.nombre, p.precio, c.descripcion AS categoria FROM productos p INNER JOIN categorias c ON c.idCategoria = p.idCategoria ORDER BY p.idProducto"
                        DeleteCommand="DELETE FROM productos WHERE idProducto = @idProducto">
                        <DeleteParameters>
                            <asp:Parameter Name="idProducto" Type="Int32" />
                        </DeleteParameters>
                    </asp:SqlDataSource>
                </section>
            </form>
        </main>
        <script>document.addEventListener('click', function (e) { if (e.target.value === 'Eliminar' && !confirm('¿Confirmás la eliminación del producto seleccionado?')) e.preventDefault(); });</script>
    </body>

    </html>
