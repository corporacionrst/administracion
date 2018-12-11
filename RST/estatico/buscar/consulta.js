
var typingTimer_set; 
var doneTypingIntervalsearch = 500;

function look_consulta () {
	clearTimeout(typingTimer_set);
	typingTimer_set = setTimeout(doneTypingsearch, doneTypingIntervalsearch);
}

function endcountlook(){
  clearTimeout(typingTimer_set);

}

function doneTypingsearch () {
	buscar(0);
}
