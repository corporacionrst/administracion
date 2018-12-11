// Buscar
function buscar (val) {
	$.ajax({
		data:{
			'codigo':document.getElementById('consultor_check').value,
			'pag':val
		},
		url:'/bodega/producto/bodega/',
		type:'get',
		success:function(data){
			var d=board(data,val);
			$('#productos_a_listar').html(d);
		}
	});
}