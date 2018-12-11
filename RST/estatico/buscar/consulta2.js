
var typingTimer_set2; 
var doneTypingIntervalsearch2 = 500;

function look_consulta2 () {
	clearTimeout(typingTimer_set2);
	typingTimer_set2 = setTimeout(doneTypingsearch2 ,doneTypingIntervalsearch2);
}

function endcountlook2(){
  clearTimeout(typingTimer_set2);

}

function doneTypingsearch2() {
	combination_query(0);
}

function combination_query (val) {
	$.ajax({
		data:{
			'codigo':document.getElementById('combinacion_check').value,
			'pag':val
		},
		url:'/bodega/producto/consulta/',
		type:'get',
		success:function(data){
			var d=t_cantidad(data,val);
			$('#cantidad').html(d);
		}
	});
}

function t_cantidad (data,pag){
	var html="<div class='table-responsive'><table class='table table-striped table-bordered table-hover'><tr><th>i</th><th>codigo</th><th>descripcion</th><th>marca</th><th>cantidad</th><th>agregar</th></tr>";
	for(i=0;i<data.length;i++){
		var codigo 		= (data[i].producto__codigo.length		>16)?data[i].producto__codigo.substr(0,12)+"..."	 :data[i].producto__codigo;
		var descripcion = (data[i].producto__descripcion.length >16)?data[i].producto__descripcion.substr(0,12)+"...":data[i].producto__descripcion;
		var marca 		= (data[i].producto__marca__nombre.length		>16)?data[i].producto__marca__nombre.substr(0,12)+"..."		 :data[i].producto__marca__nombre;
		html+="<tr><td>"+String(i+1)+"</td><td>"+codigo+"</td><td>"+descripcion+"</td><td>"+marca+"</td>";
		html+="<td><input type='text' id='val_"+data[i].id+"'></td>"
		html+=" </td><td><button class='btn-success' onclick='agregar("+data[i].id+")'>agregar</button></td></tr>";
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

function agregar (combinacion) {
	cant   = document.getElementById("val_"+combinacion).value;
	prod = document.getElementById("global").value;
	$.ajax({
		data:{
			"principal":prod,
			"codigo":combinacion,
			"cantidad":cant,
			"csrfmiddlewaretoken":mitoken,
		},
		url:"/bodega/producto/combinacion/",
		type:"post",
		success:function (retorno) {
			if(retorno=="1"){
				share_set(prod,0)
			}else{
				alert(retorno);

			}
		}

	})
}
