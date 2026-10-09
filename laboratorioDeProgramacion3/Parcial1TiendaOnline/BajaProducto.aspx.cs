using System;
using System.Web.UI.WebControls;
public partial class BajaProducto : System.Web.UI.Page
{
    protected void gvProductos_RowDeleted(object sender, GridViewDeletedEventArgs e)
    {
        lblMensaje.Visible = true;
        lblMensaje.Text = e.Exception == null && e.AffectedRows == 1 ? "El producto seleccionado fue eliminado." : "No se pudo eliminar el producto.";
        if (e.Exception != null) { e.ExceptionHandled = true; }
    }
}
