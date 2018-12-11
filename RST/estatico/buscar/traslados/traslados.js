function imprimir (traslado) {
	$.ajax({
		data:{
			"traslado":traslado,
			"csrfmiddlewaretoken":mitoken,
		},
		type:"post",
		url:"/bodega/traslados/autorizar/",
		success:function(data){

		}
	})
	var win = window.open("/bodega/traslados/pdf/"+traslado, '_blank');
	window.location.reload();
	win.focus();
  
}