<%@ Page Language="C#" CodeBehind="ModificarProducto.aspx.cs" Inherits="ModificarProducto" %>
    <!DOCTYPE html>
    <html xmlns="http://www.w3.org/1999/xhtml">

    <head runat="server">
        <meta charset="utf-8" />
        <title>Modificar - Tienda Nova</title>
        <link href="Content/site.css" rel="stylesheet" />
    </head>

    <body>
        <header>
            <div class="container">
                <h1>Tienda Nova</h1>
                <p>Modificación de productos</p>
            </div>
        </header>
        <main class="container">
            <form id="form1" runat="server">
                <section class="card">
                    <h2>Buscar y editar</h2>
                    <div class="form-row"><label for="txtId">ID del producto</label>
                        <asp:TextBox ID="txtId" runat="server" TextMode="Number" />
                    </div>
                    <asp:Button ID="btnBuscar" runat="server" Text="Buscar" CssClass="button"
                        OnClick="btnBuscar_Click" />
                    <asp:Panel ID="pnlEdicion" runat="server" Visible="false">
                        <div class="form-row"><label for="txtNombre">Nombre</label>
                            <asp:TextBox ID="txtNombre" runat="server" MaxLength="100" />
                        </div>
                        <div class="form-row"><label for="txtPrecio">Precio</label>
                            <asp:TextBox ID="txtPrecio" runat="server" TextMode="Number" />
                        </div>
                        <div class="form-row"><label for="ddlCategorias">Categoría</label>
                            <asp:DropDownList ID="ddlCategorias" runat="server" DataSourceID="dsCategorias"
                                DataTextField="descripcion" DataValueField="idCategoria" />
                        </div>
                        <asp:Button ID="btnGuardar" runat="server" Text="Guardar cambios" CssClass="button"
                            OnClick="btnGuardar_Click" />
                    </asp:Panel>
                    <asp:Label ID="lblMensaje" runat="server" CssClass="message" Visible="false" />
                    <asp:HyperLink ID="lnkVolver" runat="server" NavigateUrl="~/Default.aspx" CssClass="return">&larr; Volver
                        al inicio</asp:HyperLink>
                    <asp:SqlDataSource ID="dsCategorias" runat="server"
                        ConnectionString="<%$ ConnectionStrings:TiendaOnlineConnection %>"
                        SelectCommand="SELECT idCategoria, descripcion FROM categorias ORDER BY descripcion" />
                    <asp:SqlDataSource ID="dsProducto" runat="server"
                        ConnectionString="<%$ ConnectionStrings:TiendaOnlineConnection %>"
                        SelectCommand="SELECT idProducto, nombre, precio, idCategoria FROM productos WHERE idProducto = @idProducto"
                        UpdateCommand="UPDATE productos SET nombre = @nombre, precio = @precio, idCategoria = @idCategoria WHERE idProducto = @idProducto">
                        <SelectParameters>
                            <asp:Parameter Name="idProducto" Type="Int32" />
                        </SelectParameters>
                        <UpdateParameters>
                            <asp:Parameter Name="nombre" Type="String" />
                            <asp:Parameter Name="precio" Type="Decimal" />
                            <asp:Parameter Name="idCategoria" Type="Int32" />
                            <asp:Parameter Name="idProducto" Type="Int32" />
                        </UpdateParameters>
                    </asp:SqlDataSource>
                </section>
            </form>
        </main>
    </body>

    </html>
