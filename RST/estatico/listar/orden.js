function rechazar (argument) {

	var person = prompt("Por favor escriba el motivo", "Rechazar autorizacion")
	if (person == null || person == "") {
	    alert("no especificaste el motivo")
	} else {
		$.ajax({
			data:{
				"doc":argument,
				"motivo":person,
				"si":"no",
				"csrfmiddlewaretoken":mitoken,
			},
			url:"/admin/autorizar/orden/",
			type:"post",
			success:function (nombre) {
				alert("se le notifico el motivo a "+nombre)
			}
		})
	}

}

function aceptar (argument) {
	$.ajax({
		data:{
			"doc":argument,
			"motivo":"",
			"si":"si",
			"csrfmiddlewaretoken":mitoken,
		},
		url:"/admin/autorizar/orden/",
		type:"post",
		success:function (nombre) {
			alert("autorizado correctamente, se le notifico a "+nombre)
			window.location.reload()
		}
	})
}