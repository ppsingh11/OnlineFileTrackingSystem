
  
function popup(id1) 
{ 
	
        window.alert(id1);
  		
}


 function changeFunc() {
    var f1sem = document.getElementById("f1sem");
    var selectedValue = f1sem.options[f1sem.selectedIndex].value;
    if(selectedValue=="Other")
    document.getElementById('id01').style.display='block'
   }
   var modal = document.getElementById('id01');
   window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
} 
 