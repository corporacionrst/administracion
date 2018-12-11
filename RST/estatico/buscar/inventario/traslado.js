
function seleccionar_tienda () {
	tienda = document.getElementById('tienda').value
	html='<table class="table table-striped table-bordered table-hover" id="combinacion"><thead><tr><th>i</th><th>Codigo</th><th>Descripcion</th><th>Marca</th><th>cantidad</th><th>quitar</th></tr></thead><table class="table table-striped table-bordered table-hover" id="combinacion"><thead><tr><th>i</th><th>Codigo</th><th>Descripcion</th><th>Marca</th><th>cantidad</th><th>quitar</th></tr></thead></table></table>'
	if (tienda==0){
		$('#combinacion').html("por favor seleccione una tienda");
	}
	else
	{
		page(0)
	}
	
}

function page(pag){
	tienda = document.getElementById('tienda').value
	$.ajax({
		data:{
			"tienda":tienda,
			"pag":pag
		},
		url:"/bodega/traslados/tienda",
		type:"get",
		success:function(data){
			var html = show_table(data,pag)
			$('#combinacion').html(html);
		}
	})
}

function show_table(data,pag){

	var html="<div class='table-responsive'><table class='table table-striped table-bordered table-hover'><tr><th>i</th><th>codigo</th><th>descripcion</th><th>marca</th><th>cantidad</th><th>precio</th><th>quitar</th>"
	largo=4
	for(i=0;i<data.length;i++){
		var codigo 		= (data[i].lista__producto__producto__codigo.length		>16)?data[i].lista__producto__producto__codigo.substr(0,12)+"..."	 :data[i].lista__producto__producto__codigo;
		var descripcion = (data[i].lista__producto__producto__descripcion.length >16)?data[i].lista__producto__producto__descripcion.substr(0,12)+"...":data[i].lista__producto__producto__descripcion;
		var marca 		= (data[i].lista__producto__producto__marca__nombre.length		>16)?data[i].lista__producto__producto__marca__nombre.substr(0,12)+"..."		 :data[i].lista__producto__producto__marca__nombre;
		html+="<tr><td>"+String(i+1)+"</td><td>"+codigo+"</td><td>"+descripcion+"</td><td>"+marca+"</td>";
		html+="<td>"+data[i].lista__cantidad+"</td><td>"+data[i].lista__precio+"</td>"
		html+=" </td><td><button class='btn-danger' onclick='quitar("+data[i].lista__id+")'>-</button></td></tr>";
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

function buscar (val) {
	tienda = document.getElementById('tienda').value
	$.ajax({
		data:{
			'codigo':document.getElementById('consultor_check').value,
			'pag':val,
			'tienda':tienda,
		},
		url:'/bodega/traslados/stock',
		type:'get',
		success:function(data){
			var d=board(data,val);
			$('#cantidad').html(d);
		}
	});
}


function board(data,pag){
	var html="<div class='table-responsive'><table class='table table-striped table-bordered table-hover'><tr><th>i</th><th>codigo</th><th>descripcion</th><th>marca</th><th>venta sugerida</th><th>cantidad</th><th>agregar</th>"
	for(i=0;i<data.length;i++){
		var codigo 		= (data[i].producto__producto__codigo.length		>18)?data[i].producto__producto__codigo.substr(0,14)+"..."	 :data[i].producto__producto__codigo;
		var descripcion = (data[i].producto__producto__descripcion.length >18)?data[i].producto__producto__descripcion.substr(0,14)+"...":data[i].producto__producto__descripcion;
		var marca 		= (data[i].producto__producto__marca__nombre.length		>18)?data[i].producto__producto__marca__nombre.substr(0,14)+"..."		 :data[i].producto__producto__marca__nombre;
		html+="<tr><td>"+String(i+1)+"</td><td>"+codigo+"</td><td>"+descripcion+"</td><td>"+marca+"</td>";
		html+="<td>"+data[i].tarjeta+"</td><td><input placeholder='en stock:"+data[i].cantidad+"'type='text' id='cant_"+data[i].id+"' onkeypress='return event.charCode>=48 && event.charCode<=57'/> </td>"
		html+=" </td><td><button class='btn-success' onclick='load_data("+data[i].id+","+data[i].distribuidor+","+data[i].producto__id+")'>+</button></td></tr>";
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
function load_data (uso,precio,prod) {

	cantidad=document.getElementById("cant_"+uso).value
	tienda = document.getElementById('tienda').value
	$.ajax({
		data:{
			"precio":precio,
			"tienda":tienda,
			"producto":prod,
			"cantidad":cantidad,
			"csrfmiddlewaretoken":mitoken,
		},
		url:"/bodega/traslados/agregar/",
		type:"POST",
		success:function(data){
			page(0)
		}
	})
}

function quitar(identificador){
	tienda = document.getElementById('tienda').value
	if(tienda==0){
		alert("por favor seleccione una tienda antes")
	}else{
		$.ajax({
			data:{
				"tienda":tienda,
				"producto":identificador,
				"csrfmiddlewaretoken":mitoken
			},
			url:"/bodega/traslados/quitar/",
			type:"post",
			success:function(data){
				page(0)

			}
		})
	}
}

function solicitar_traslado(){
	tienda = document.getElementById('tienda').value
	if(tienda==0){
		alert("por favor seleccione una tienda antes")
	}else{
		$.ajax({
			data:{
				"tienda":tienda,
				"csrfmiddlewaretoken":mitoken
			},
			url:"/bodega/traslados/solicitar/",
			type:"post",
			success:function(data){
				if(data=="1"){
					window.location.reload()
				}else{
					alert(data)
				}
			}
		})
	}

}
