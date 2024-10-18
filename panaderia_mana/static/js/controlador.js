document.addEventListener('DOMContentLoaded', function() {


    const proveedores = document.getElementById('proveedores');

    console.log(proveedores);

    proveedores.addEventListener('change', function() {
        // Obtener el valor seleccionado
        const seleccionado = proveedores.options[proveedores.selectedIndex].value;
        
        // Mostrar el nombre del proveedor seleccionado
       // document.getElementById('proveedorSeleccionado').value = seleccionado;

        // Mostrar el código del proveedor seleccionado

        //const proveedorSeleccionado= document.getElementById('proveedorSeleccionado').value
        const insumos= document.getElementById('insumos')
        const divCantidad= document.getElementById('divCantidad')
        console.log(insumos);

        if (this.value !== 'Seleccionar...') {
            this.disabled = true;
        }

        if (seleccionado === "arcor"){
  
            insumos.innerHTML = `
            
                <span class="input-group-text bg-faded" id="basic-addon1">Insumo:</span>
                <select id="insumo" name="insumo" class="form-select bg-faded" required>
                    
                    <option value="azucar">Azucar</option>
                    <option value="chispas">Chispas de chocolate</option>
                    <option value="dulceMembrillo">Dulce de Membrillo</option>
                    <option value="dulceLeche">Dulce de Leche</option>
                </select>
            `
          //insumos.style.display = 'block';
        }else if (seleccionado === "beraca"){
            insumos.innerHTML = `
                <span class="input-group-text bg-faded" id="basic-addon1">Insumo:</span>
                <select id="insumo" name="insumo" class="form-select bg-faded" required>
                    
                    <option value="azucar">Azucar</option>
                    <option value="lecheEntera">leche Entera</option>
                    <option value="lechedescremada">leche Descremada</option>
                    <option value="dulceLeche">Dulce de Leche</option>
                    <option value="chocolate">Chocolate</option>
                    <option value="harina">Harina</option>
                    <option value="manteca">Manteca</option>
                    <option value="agua">Agua</option>
                    <option value="sal">Sal</option>
                    <option value="crema">Crema</option>
                    <option value="levadura">Levadura</option>
                </select>
            `
 //            insumos.style.display = 'block';
        }else if (seleccionado === "molino"){
  //           insumos.style.display = 'block';
 //            insumos.className ="input-group mb-3 container"
            insumos.innerHTML = `
                <span class="input-group-text bg-faded" id="basic-addon1">Insumo:</span>
                <select id="insumo" name="insumo" class="form-select bg-faded" required>
                    
                    <option value="harina">Harina Leudante x 50kg</option>
                    <option value="harina">Harina Comun x 50kg</option>
                    <option value="harina">Harina Leudante x 25kg</option>
                    <option value="harina">Harina Comun x 25kg</option>
                </select>
            `
            
        }else if (seleccionado === "vea"){
            insumos.innerHTML = `
                <span class="input-group-text bg-faded" id="basic-addon1">Insumo:</span>
                <select id="insumo" name="insumo" class="form-select bg-faded" required>
                    
                    <option value="azucar">Azucar</option>
                    <option value="lecheEntera">leche Entera</option>
                    <option value="lechedescremada">leche Descremada</option>
                    <option value="dulceLeche">Dulce de Leche</option>
                    <option value="chocolate">Chocolate</option>
                    <option value="harina">Harina</option>
                    <option value="manteca">Manteca</option>
                    <option value="agua">Agua</option>
                    <option value="sal">Sal</option>
                    <option value="crema">Crema</option>
                    <option value="levadura">Levadura</option>
                    <option value="anis">Anis</option>
                </select>
            `
   //          insumos.style.display = 'block';

        }
        divCantidad.innerHTML = `
        <span class="input-group-text bg-faded" id="basic-addon1">Cantidad:</span>
        <input type="number" id="cantidad" name="cantidad" class="form-control bg-faded" required>
        <input type="button" value="Agregar" class="btn bg-primary" id="btnAgregar">
    `

    const tablaproductos= document.getElementById('tablaproductos')
    tablaproductos.style.display = 'block';
    tablaproductos.innerHTML += `
        <table class="table table-striped " >
        <thead>
            <tr>
            <th scope="col">Orden</th>
            <th scope="col">Insumo</th>
            <th scope="col">Cantidad</th>
            <th scope="col">Precio</th>
            </tr>
        </thead>
        <tbody id="listaproductos2">

        </tbody>
        </table>`
        
    //divCantidad.style.display = 'block';

    const btnAgregar= document.getElementById('btnAgregar')
    /*
    btnAgregar.addEventListener('click', function() {
        const insumo= document.getElementById('insumo').value
        const cantidad= document.getElementById('cantidad').value

        const listaproductos= document.getElementById('listaproductos')


        listaproductos.innerHTML += `
            <span class="input-group-text bg-faded" id="basic-addon1">Insumo: ${insumo}</span>
            <span class="input-group-text bg-faded" id="basic-addon1">Cantidad: ${cantidad}</span>
    `

    });
    */

    //para la lista faltaria agregar los precios 
    let contador=0;
        btnAgregar.addEventListener('click', function() {
            contador++;
            const insumo= document.getElementById('insumo').value
            const cantidad= document.getElementById('cantidad').value

            const listaproductos2= document.getElementById('listaproductos2')
            
            listaproductos2.innerHTML += `
                <tr>
                    <th scope="row">${contador}</th>
                    <td>${insumo}</td>
                    <td>${cantidad}</td>
                    <td> 000 </td>
                    </tr>`

        });


    });


    const fecha_Solicitud = document.getElementById('fecha_Solicitud');
    
    fecha_Solicitud.addEventListener('change', function() {
        const fechaActual = new Date();
        const fechaIngresada = new Date(this.value);
    
        if (fechaIngresada < fechaActual) {
            alert('La Fecha selecionada debe ser Mayor a la Fecha Actual');
        }
    });



});



/**
 * 


 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * btnAgregar.addEventListener('click', function() {
        const nombre = document.getElementById(`nombre${insumos.selectedIndex + 1}`).value;
        const cantidad = document.getElementById('cantidad').value;
        const precio = document.getElementById(`precio${insumos.selectedIndex + 1}`).value;
        const total = parseFloat(precio) * parseInt(cantidad);
        const fila = document.createElement('tr');
        fila.innerHTML = `
            <td>${nombre}</td>
            <td>${cantidad}</td>
            <td>${precio}</td>
            <td>${total}</td>
            <td><button type="button" class="btn btn-danger" onclick="eliminarFila(this)">X</button></td>
            <input type="hidden" name="nombre${insumos.selectedIndex + 1}" value="${nombre}">
            <input type="hidden" name="precio${insumos.selectedIndex + 1}" value="${precio}">
            <input type="hidden" name="total${insumos.selectedIndex + 1}" value="${total}">
            <input type="hidden" name="insumo${insumos.selectedIndex + 1}" value="${insumos.options[insumos.selectedIndex].value}">
            <input type="hidden" name="proveedor${insumos.selectedIndex + 1}" value="${proveedores.options[proveedores.selectedIndex].value}">
            <input type="hidden" name="index${insumos.selectedIndex + 1}" value="${insumos.selectedIndex + 1}">
        `



    
    });
 */