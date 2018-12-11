
function board(data,pag){
	var html="<div class='table-responsive'><table class='table table-striped table-bordered table-hover'><tr><th>i</th><th>codigo</th><th>descripcion</th><th>marca</th><th>cantidad</th><th>precio</th><th>seleccionar</th></tr>";
	for(i=0;i<data.length;i++){
		var codigo 		= (data[i].producto__codigo.length		>18)?data[i].producto__codigo.substr(0,14)+"..."	 :data[i].producto__codigo;
		var descripcion = (data[i].producto__descripcion.length >18)?data[i].producto__descripcion.substr(0,14)+"...":data[i].producto__descripcion;
		var marca 		= (data[i].producto__marca__nombre.length		>18)?data[i].producto__marca__nombre.substr(0,14)+"..."		 :data[i].producto__marca__nombre;
		html+="<tr><td>"+String(i+1)+"</td><td>"+codigo+"</td><td>"+descripcion+"</td><td>"+marca+"</td>";
		html+="<td><input type='text' id='cant_"+data[i].id+"' onkeypress='return event.charCode>=48 && event.charCode<=57'/> </td><td><input type='text' id='pr_"+data[i].id+"'onkeypress='return event.charCode>=48 && event.charCode<=57 || event.charCode==46'/> </td>"
		html+=" </td><td><button class='btn-success' onclick='load_data("+data[i].id+")'>seleccionar</button></td></tr>";
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
	html = html+"<tr><td colspan='4'></td><td> "+prev+" </td><td> "+next+" </td><td></td> </tr></table></div>";
	return html;

}

function dump_set (info,nombre) {
	var r = confirm("Desea eliminar este elemento de la lista:"+nombre);
    if (r == true) {
    
		$.ajax({
			data:{
				"codigo":info,
				"csrfmiddlewaretoken":mitoken
			},
			type:"POST",
			url:"/ventas/quitar/",
			success:function(data){
				alert(data)
				retabla(0)
				
			}
		})
	}
}

function load_data (info) {
	cantidad=document.getElementById('cant_'+info).value
	precio=document.getElementById('pr_'+info).value
	if (precio!=null && precio!="" && precio>0 && cantidad!=null && cantidad!="" && cantidad>0)
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
			url:"/ventas/agregar/",
			success:function(data){
				if (data!="1"){
					alert(data)
				}else{
					retabla(0)
				}
			}
		})
	}else{
		alert("por favor revise sus casillas, la información no esta correcta")
	}
}

window.onload = function() {
  retabla(0);
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
		prev="<a onclick='retabla("+p+")'>pag"+(p+1)+"<i class='fa fa-arrow-left' aria-hidden='true'></i></a>";
	}
	if(fin==10)
	{
		p=pag+1;
		next="<a onclick='retabla("+p+")'>pag"+(p+1)+"<i class='fa fa-arrow-right' aria-hidden='true'></i></a>";
	}
	html = html+"<tr><td colspan='5'></td><td> "+prev+" </td><td> "+next+" </td><td><b>"+data[fin]+"</b></div></td> </tr></table></div>";
	return html;
}

function retabla (pag) {
	$.ajax({
		data:{"pag":pag},
		type:"get",
		url:"/inventario/compra",
		success:function(data){
			var d=tabla_contenido(data,pag);
			$('#carga').html(d);

		}
	})
}
