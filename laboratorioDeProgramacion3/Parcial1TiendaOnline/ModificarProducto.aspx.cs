using System;
using System.Data.SqlClient;
using System.Web.UI;
using System.Web.UI.WebControls;
public partial class ModificarProducto : Page
{
    protected void btnBuscar_Click(object sender, EventArgs e)
    {
        int id; if (!Int32.TryParse(txtId.Text, out id)) { Mensaje("Ingresá un ID válido."); return; }
        dsProducto.SelectParameters["idProducto"].DefaultValue = id.ToString(); dsProducto.DataSourceMode = SqlDataSourceMode.DataReader;
        using (SqlDataReader datos = (SqlDataReader)dsProducto.Select(DataSourceSelectArguments.Empty))
        {
            if (!datos.Read()) { pnlEdicion.Visible = false; Mensaje("No existe un producto con ese ID."); return; }
            txtNombre.Text = datos["nombre"].ToString(); txtPrecio.Text = datos["precio"].ToString();
            ddlCategorias.DataBind(); ddlCategorias.SelectedValue = datos["idCategoria"].ToString();
        }
        ViewState["nombreOriginal"] = txtNombre.Text; ViewState["precioOriginal"] = txtPrecio.Text; ViewState["categoriaOriginal"] = ddlCategorias.SelectedValue;
        pnlEdicion.Visible = true; lblMensaje.Visible = false;
    }
    protected void btnGuardar_Click(object sender, EventArgs e)
    {
        decimal precio; if (!pnlEdicion.Visible || !Decimal.TryParse(txtPrecio.Text, out precio) || String.IsNullOrWhiteSpace(txtNombre.Text)) { Mensaje("Completá nombre y precio válido."); return; }
        if (txtNombre.Text.Trim() == (string)ViewState["nombreOriginal"] && txtPrecio.Text == (string)ViewState["precioOriginal"] && ddlCategorias.SelectedValue == (string)ViewState["categoriaOriginal"]) { Mensaje("Modificá al menos un campo antes de guardar."); return; }
        dsProducto.UpdateParameters["idProducto"].DefaultValue = txtId.Text; dsProducto.UpdateParameters["nombre"].DefaultValue = txtNombre.Text.Trim(); dsProducto.UpdateParameters["precio"].DefaultValue = precio.ToString(); dsProducto.UpdateParameters["idCategoria"].DefaultValue = ddlCategorias.SelectedValue;
        Mensaje(dsProducto.Update() == 1 ? "Los cambios fueron guardados." : "No se pudo actualizar el producto.");
    }
    private void Mensaje(string texto) { lblMensaje.Text = texto; lblMensaje.Visible = true; }
}
