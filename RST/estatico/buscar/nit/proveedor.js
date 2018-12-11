function check_nit () {
	nit=(document.getElementById('id_nit').value).toUpperCase()
	$.ajax({
		data:{"nit":nit},
		type:"GET",
		url:"/admin/persona/buscar_proveedor",
		success:function(data){
			try {
				document.getElementById("id_nombre").value=data[0].persona__nombre
				document.getElementById("id_direccion").value=data[0].persona__direccion
			}
			catch(err) {
				modal.style.display="block";
				document.getElementById("id_nit_a_registrar").value=nit
			
			}
		}
	})
}
function usar (nit,nombre,direccion) {
	document.getElementById("id_nit").value=nit
	document.getElementById("id_nombre").value=nombre
	document.getElementById("id_direccion").value=direccion

}
function city(){
	document.getElementById("id_direccion_a_registrar").value="CIUDAD"
}

function solicitar_autorizacion(){
	nit 	= document.getElementById("id_nit").value
	nombre 	= document.getElementById("id_nombre").value
	if (nit==null || nit =="" || nombre==null || nombre==""){
		alert("los datos no estan completos")
	}else{
		$.ajax({
			data:{
				"nit":nit,
				"csrfmiddlewaretoken":mitoken},
			url:"/ventas/orden_de_compra/",
			type:"POST",
			success:function(data){
				if(data=="1"){
					alert("la solicitud fue enviada correctamente")
					window.location.reload()
				}else{
					alert(data)
				}
			}
		})
	}
}