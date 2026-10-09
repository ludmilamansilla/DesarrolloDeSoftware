<%@ Page Language="C#" CodeBehind="AltaProducto.aspx.cs" Inherits="AltaProducto" %>
    <!DOCTYPE html>
    <html xmlns="http://www.w3.org/1999/xhtml">

    <head runat="server">
        <meta charset="utf-8" />
        <title>Alta - Tienda Nova</title>
        <link href="Content/site.css" rel="stylesheet" />
    </head>

    <body>
        <header>
            <div class="container">
                <h1>Tienda Nova</h1>
                <p>Alta de productos</p>
            </div>
        </header>
        <main class="container">
            <form id="form1" runat="server">
                <section class="card">
                    <h2>Nuevo producto</h2>
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
                    <asp:Button ID="btnConfirmar" runat="server" Text="Confirmar" CssClass="button"
                        OnClick="btnConfirmar_Click" />
                    <asp:Label ID="lblMensaje" runat="server" CssClass="message" Visible="false" />
                    <asp:HyperLink ID="lnkVolver" runat="server" NavigateUrl="~/Default.aspx" CssClass="return">&larr; Volver
                        al inicio</asp:HyperLink>
                    <asp:SqlDataSource ID="dsCategorias" runat="server"
                        ConnectionString="<%$ ConnectionStrings:TiendaOnlineConnection %>"
                        SelectCommand="SELECT idCategoria, descripcion FROM categorias ORDER BY descripcion" />
                    <asp:SqlDataSource ID="dsProductos" runat="server"
                        ConnectionString="<%$ ConnectionStrings:TiendaOnlineConnection %>"
                        InsertCommand="INSERT INTO productos (nombre, precio, idCategoria) VALUES (@nombre, @precio, @idCategoria)">
                        <InsertParameters>
                            <asp:Parameter Name="nombre" Type="String" />
                            <asp:Parameter Name="precio" Type="Decimal" />
                            <asp:Parameter Name="idCategoria" Type="Int32" />
                        </InsertParameters>
                    </asp:SqlDataSource>
                </section>
            </form>
        </main>
    </body>

    </html>
