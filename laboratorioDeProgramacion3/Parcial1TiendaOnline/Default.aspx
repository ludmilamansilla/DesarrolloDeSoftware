<%@ Page Language="C#" %>
  <!DOCTYPE html>
  <html xmlns="http://www.w3.org/1999/xhtml">

  <head runat="server">
    <meta charset="utf-8" />
    <title>Tienda Nova - Inicio</title>
    <link href="Content/site.css" rel="stylesheet" />
  </head>

  <body>
    <header style="background-color: #571b78; color: #ffffff;">
      <div class="container">
        <h1 style="color: #ffffff;">Tienda Nova</h1>
        <p style="color: #ffffff;">Administración de productos y categorías</p>
      </div>
    </header>
    <main class="container">
      <form id="form1" runat="server">
        <section class="dashboard">
          <figure class="storefront">
            <img src="Images/tienda-nova.jpeg" alt="Frente de Tienda Nova" />
            <figcaption>Tienda Nova · productos para todos los días</figcaption>
          </figure>
        </section>
        <nav class="quick-actions" aria-label="Operaciones del catálogo">
          <asp:HyperLink ID="lnkAlta" runat="server" NavigateUrl="~/AltaProducto.aspx"><span class="action-number">01</span><span>Alta de productos</span></asp:HyperLink>
          <asp:HyperLink ID="lnkConsulta" runat="server" NavigateUrl="~/ConsultaProductos.aspx"><span class="action-number">02</span><span>Consulta de productos</span></asp:HyperLink>
          <asp:HyperLink ID="lnkModificacion" runat="server" NavigateUrl="~/ModificarProducto.aspx"><span class="action-number">03</span><span>Modificar producto</span></asp:HyperLink>
          <asp:HyperLink ID="lnkBaja" runat="server" NavigateUrl="~/BajaProducto.aspx"><span class="action-number">04</span><span>Baja de productos</span></asp:HyperLink>
        </nav>
      </form>
    </main>
  </body>

  </html>
