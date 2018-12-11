function enviar(tipo){
	$.ajax({
		data:{
			"pagina":pagina,
			"tipo":tipo,
		},
		url:"/ventas/facturacion/"+pagina,
		type:"POST",
		success:function(data){

		}
	})
}

function imprimir () {
	$.ajax({
		data:{
			"pagina":pagina,
			"tipo":tipo,
		},
		url:"/ventas/facturacion/"+pagina,
		type:"POST",
		success:function(data){

		}
	})
}