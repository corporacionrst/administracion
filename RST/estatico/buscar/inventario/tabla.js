
function board(data,pag){
	var html="<div class='table-responsive'><table class='table table-striped table-bordered table-hover'><tr><th>i</th><th>codigo</th><th>descripcion</th><th>marca</th><th>cantidad</th>"
	largo=3
	if(ver_costos==true){html+="<th>costo</th>";largo=largo+1}
	if(ver_distribuidor==true){html+="<th>distribuidor</th>";largo=largo+1}
	if(ver_mayorista==true){html+="<th>mayorista</th>";largo=largo+1}
	if(ver_efectivo==true){html+="<th>efectivo</th>";largo=largo+1}
	if(ver_tarjeta==true){html+="<th>tarjeta</th>";largo=largo+1}
	
	html+="<th>mas</th></tr>";
	for(i=0;i<data.length;i++){
		var codigo 		= (data[i].producto__producto__codigo.length		>16)?data[i].producto__producto__codigo.substr(0,12)+"..."	 :data[i].producto__producto__codigo;
		var descripcion = (data[i].producto__producto__descripcion.length >16)?data[i].producto__producto__descripcion.substr(0,12)+"...":data[i].producto__producto__descripcion;
		var marca 		= (data[i].producto__producto__marca__nombre.length		>16)?data[i].producto__producto__marca__nombre.substr(0,12)+"..."		 :data[i].producto__producto__marca__nombre;
		html+="<tr><td>"+String(i+1)+"</td><td>"+codigo+"</td><td>"+descripcion+"</td><td>"+marca+"</td>";
		html+="<td>"+data[i].cantidad+"</td>"
		if(ver_costos==true){html+="<td>"+data[i].costo+"</td>"}
		if(ver_distribuidor==true){html+="<th>"+data[i].distribuidor+"</th>"}
		if(ver_mayorista==true){html+="<th>"+data[i].mayorista+"</th>"}
		if(ver_efectivo==true){html+="<th>"+data[i].efectivo+"</th>"}
		if(ver_tarjeta==true){html+="<th>"+data[i].tarjeta+"</th>"}
		html+=" </td><td><button class='btn-success' onclick='detalle("+data[i].id+")'>+</button></td></tr>";
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