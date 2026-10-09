using System;
public partial class AltaProducto : System.Web.UI.Page
{
    protected void btnConfirmar_Click(object sender, EventArgs e)
    {
        decimal precio;
        if (String.IsNullOrWhiteSpace(txtNombre.Text) || !Decimal.TryParse(txtPrecio.Text, out precio) || precio < 0)
        { Mostrar("Ingresá un nombre y un precio válido."); return; }
        dsProductos.InsertParameters["nombre"].DefaultValue = txtNombre.Text.Trim();
        dsProductos.InsertParameters["precio"].DefaultValue = precio.ToString();
        dsProductos.InsertParameters["idCategoria"].DefaultValue = ddlCategorias.SelectedValue;
        dsProductos.Insert();
        txtNombre.Text = txtPrecio.Text = String.Empty;
        Mostrar("El producto se cargó correctamente.");
    }
    private void Mostrar(string texto) { lblMensaje.Text = texto; lblMensaje.Visible = true; }
}
