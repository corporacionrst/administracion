
function board(data,pag){
	var html="<div class='table-responsive'><table class='table table-striped table-bordered table-hover'><tr><th>i</th><th>codigo</th><th>descripcion</th><th>marca</th><th>seleccionar</th></tr>";
	for(i=0;i<data.length;i++){
		var codigo 		= (data[i].producto__codigo.length		>16)?data[i].producto__codigo.substr(0,12)+"..."	 :data[i].producto__codigo;
		var descripcion = (data[i].producto__descripcion.length >16)?data[i].producto__descripcion.substr(0,12)+"...":data[i].producto__descripcion;
		var marca 		= (data[i].producto__marca__nombre.length		>16)?data[i].producto__marca__nombre.substr(0,12)+"..."		 :data[i].producto__marca__nombre;
		html+="<tr><td>"+String(i+1)+"</td><td>"+codigo+"</td><td>"+descripcion+"</td><td>"+marca+"</td>";
		html+=" </td><td><button class='btn-success' onclick='load_data("+data[i].id+","+'"'+data[i].producto__codigo+'"'+","+'"'+data[i].producto__descripcion+'"'+","+'"'+data[i].producto__marca__nombre+'"'+")'>seleccionar</button></td></tr>";
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
	html = html+"<tr><td colspan='2'></td><td> "+prev+" </td><td> "+next+" </td><td></td> </tr></table></div>";
	return html;

}
function load_data (valor,codigo,descripcion,marca) {
	document.getElementById('global').value=valor
	document.getElementById('codigo').value		=codigo
	document.getElementById('descripcion').value=descripcion
	document.getElementById('marca').value		=marca
	cch=document.getElementById('combinacion_check')
	cch.disabled=false;
	cch.focus();
	html="<div class='table-responsive'><table class='table table-striped table-bordered table-hover'><tr><th>i</th><th>codigo</th><th>descripcion</th><th>marca</th><th>seleccionar</th></tr></table></td>";
	
	$('#productos_a_listar').html(html);
	share_set(valor,0)
}

function share_set (valor,pag) {
	$.ajax({
		data:{"codigo":valor},
		type:"get",
		url:"/bodega/producto/combinacion/",
		success:function(data){
			var d=combinacion(data,0);
			$('#combinacion').html(d);
			document.getElementById("buscacombinacion").display="block"
		}
	})
}

function combinacion(data,pag){
	var html="<div class='table-responsive'><table class='table table-striped table-bordered table-hover'><tr><th>i</th><th>codigo</th><th>descripcion</th><th>marca</th><th>cantidad</th><th>quitar</th></tr>";
	for(i=0;i<data.length;i++){
		var codigo 		= (data[i].producto__codigo.length		>16)?data[i].producto__codigo.substr(0,12)+"..."	 :data[i].producto__codigo;
		var descripcion = (data[i].producto__descripcion.length >16)?data[i].producto__descripcion.substr(0,12)+"...":data[i].producto__descripcion;
		var marca 		= (data[i].producto__marca__nombre.length		>16)?data[i].producto__marca__nombre.substr(0,12)+"..."		 :data[i].producto__marca__nombre;
		html+="<tr><td>"+String(i+1)+"</td><td>"+codigo+"</td><td>"+descripcion+"</td><td>"+marca+"</td><td>"+data[i].cantidad+"</td>";
		html+=" </td><td><button class='btn-danger' onclick='rm_data("+data[i].id+")'>X</button></td></tr>";
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
	html = html+"<tr><td colspan='3'></td><td> "+prev+" </td><td> "+next+" </td><td></td> </tr></table></div>";
	return html;
}

function rm_data (val) {
	prod = document.getElementById("global").value;
	$.ajax({
		data:{
			"principal":prod,
			"codigo":val,
			"csrfmiddlewaretoken":mitoken,
		},
		type:"POST",
		url:"/bodega/producto/combinar/",
		success:function(data){
			if(data=="1"){
				share_set(prod,0)
			}else{
				alert(data);

			}
		}
	})
}