
function board(data,pag){
	var html="<div class='table-responsive'><table class='table table-striped table-bordered table-hover'><tr><th>i</th><th>codigo</th><th>descripcion</th><th>marca</th>"
	largo=3
	if(ver_costos==true){html+="<th>costo</th>";largo=largo+1}
	if(ver_distribuidor==true){html+="<th>distribuidor</th>";largo=largo+1}
	if(ver_mayorista==true){html+="<th>mayorista</th>";largo=largo+1}
	if(ver_efectivo==true){html+="<th>efectivo</th>";largo=largo+1}
	html+="<th>cantidad</th><th>tarjeta</th>";largo=largo+1
	
	html+="<th>mas</th></tr>";
	for(i=0;i<data.length;i++){
		var codigo 		= (data[i].producto__producto__codigo.length		>16)?data[i].producto__producto__codigo.substr(0,12)+"..."	 :data[i].producto__producto__codigo;
		var descripcion = (data[i].producto__producto__descripcion.length >16)?data[i].producto__producto__descripcion.substr(0,12)+"...":data[i].producto__producto__descripcion;
		var marca 		= (data[i].producto__producto__marca__nombre.length		>16)?data[i].producto__producto__marca__nombre.substr(0,12)+"..."		 :data[i].producto__producto__marca__nombre;
		html+="<tr><td>"+String(i+1)+"</td><td>"+codigo+"</td><td>"+descripcion+"</td><td>"+marca+"</td>";
		if(ver_costos==true){html+="<td>"+data[i].costo+"</td>"}
		if(ver_distribuidor==true){html+="<th>"+data[i].distribuidor+"</th>"}
		if(ver_mayorista==true){html+="<th>"+data[i].mayorista+"</th>"}
		if(ver_efectivo==true){html+="<th>"+data[i].efectivo+"</th>"}
		html+="<td><input type='text' placeholder='stock:"+data[i].cantidad+"' id='cant_"+data[i].id+"'></td>"
		html+="<th><input type='text' value='"+data[i].tarjeta+"' id='pr_"+data[i].id+"'> </th>"
		html+=" </td><td><button class='btn-success' onclick='load_data("+data[i].distribuidor+","+data[i].id+")'>+</button></td></tr>";
	}
	var prev="", next="";
	if (pag!=0){
		p = pag-1;
		prev="<a onclick='page("+p+")' class='pull-right'><i class='fa fa-arrow-left pull-right' aria-hidden='true'></i></a>";
	}
	if(data.length==10)
	{
		p=pag+1;
		next="<a onclick='page("+p+")'><i class='fa fa-arrow-right' aria-hidden='true'></i></a>";
	}
	html = html+"<tr><td colspan='"+largo+"'></td><td> "+prev+" </td><td> "+next+" </td><td></td> </tr></table></div>";
	return html;

}

function dump_set (info,nombre) {
	var r = confirm("Desea eliminar este elemento de la lista:"+nombre);
    if (r == true) {
    
		$.ajax({
			data:{
				"codigo":info,
				"pagina":pagina,
				"csrfmiddlewaretoken":mitoken
			},
			type:"POST",
			url:"/ventas/remover/",
			success:function(data){
				alert(data)
				cargar_lista(0)
				
			}
		})
	}
}

function load_data (minimo,info) {
	cantidad=document.getElementById('cant_'+info).value
	precio=document.getElementById('pr_'+info).value
	if (precio!=null && precio!="" && precio>minimo && cantidad!=null && cantidad!="" && cantidad>0)
	{
		$.ajax({
			data:{
				"codigo":info,
				"cantidad":cantidad,
				"precio":precio,
				"pagina":pagina,
				"csrfmiddlewaretoken":mitoken
			},
			type:"POST",
			url:"/ventas/cargar/",
			success:function(data){
				if (data!="1"){
					alert(data)
				}else{
					cargar_lista(0)
				}
			}
		})
	}else{
		alert("por favor revise sus casillas, la información no esta correcta")
	}
}

window.onload = function() {
  cargar_lista(0);
};

function tabla_contenido(data,pag){
	var html="<div class='table-responsive'><table class='table table-striped table-bordered table-hover'><tr><th></th><th>Código</th><th>Descripción</th><th>Marca</th><th>Cantidad</th><th>Unitario</th><th>Total</th><th>quitar</th></tr>";
	var fin=data.length-1
	for (i =0;i<fin;i++){
		var codigo =data[i].producto__producto__codigo;
		var descripcion =data[i].producto__producto__descripcion;
		var marca =data[i].producto__producto__marca__nombre;
		var cantidad =data[i].cantidad;
		var precio =data[i].precio;
		html+="<tr><td>"+String(i+1)+"</td><td>"+codigo+"</td><td>"+descripcion+"</td><td>"+marca+"</td><td>"+cantidad+"</td><td>"+precio+"</td><td>"+data[i].total+"</td>"
		
		html+="<td><button class='btn btn-lg btn-danger' onclick='dump_set("+'"'+data[i].id+'","'+data[i].producto__producto__codigo+'"'+")'><i class='fa fa-trash-o' aria-hidden='true'></i></button></td></tr>";
	}
	var prev="", next="";
	if (pag!=0){
		p = pag-1;
		prev="<a onclick='cargar_lista("+p+")'>pag"+(p+1)+"<i class='fa fa-arrow-left' aria-hidden='true'></i></a>";
	}
	if(fin==10)
	{
		p=pag+1;
		next="<a onclick='cargar_lista("+p+")'>pag"+(p+1)+"<i class='fa fa-arrow-right' aria-hidden='true'></i></a>";
	}
	html = html+"<tr><td colspan='5'></td><td> "+prev+" </td><td> "+next+" </td><td><b>"+data[fin]+"</b></div></td> </tr></table></div>";
	return html;
}

function cargar_lista (pag) {
	$.ajax({
		data:{
			"pag":pag,
			"pagina":pagina},
		type:"get",
		url:"/inventario/venta",
		success:function(data){
			var d=tabla_contenido(data,pag);
			$('#carga').html(d);

		}
	})
}
