
var nit_timer; 
var done_timer = 200;

function look_nit () {
	clearTimeout(nit_timer);
	nit_timer = setTimeout(done_nit_search, done_timer);
}

function endnit(){
  clearTimeout(nit_timer);

}

function done_nit_search () {
	buscar_por_nit(0);
}


