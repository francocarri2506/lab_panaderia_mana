document.addEventListener('DOMContentLoaded', function() {
    
    //Fecha de venta: la fecha ingresada no puede ser superior a la fecha actual.
    //Mensaje de error: "Fecha de venta debe ser menor o igual a la Fecha Actual".
    
    const fechaVenta = document.getElementById('fechaVenta');
    
    fechaVenta.addEventListener('change', function() {
        const fechaActual = new Date();
        const fechaIngresada = new Date(this.value);
        
        if (fechaIngresada > fechaActual) {
            alert("Fecha de venta debe ser menor o igual a la Fecha Actual");
        }
        console.log(fechaActual);
        console.log(fechaIngresada);

    });

    const tipoPagoSelect = document.getElementById('tipo_pago');
    
    tipoPagoSelect.addEventListener('change', function() {

        const tipoVentaSelect = document.getElementById('tipo_venta');
        const formaDePago = tipoPagoSelect.value;
    
        // Limpia todas las opciones del select "Tipo de Venta"
        tipoVentaSelect.innerHTML = '';
    
            // Agrega las opciones correspondientes dependiendo del valor seleccionado en "Forma de Pago"
            if (formaDePago === 'Efectivo') {
                tipoVentaSelect.innerHTML = '<option value="Contado">Contado</option>';
            } else if (formaDePago === 'Tarjeta') {
                tipoVentaSelect.innerHTML = '<option value="Credito">Crédito</option><option value="Debito">Débito</option>';
            } else if (formaDePago === 'Transferencia') {
                tipoVentaSelect.innerHTML = '<option value="Debito">Débito</option>';
            }
    });


});

