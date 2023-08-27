function displayHostsOption(){
	var departments = document.getElementById("departments");
	var enterhosts = document.getElementById("enterhosts");
	departments.addEventListener("input", function() {
		if (this.value > 5) {
			this.value = 5;
		}
		enterhosts.innerHTML = "";
		if (isInt(parseInt(departments.value))){
			enterhosts.innerHTML += "<p>Enter the number of Host for each Department:</p>";
			var i=0;
			while (i<departments.value){
				enterhosts.innerHTML += ("<h3 style='color: white'>Department " + String(i + 1) + "</h3>");

				enterhosts.innerHTML += ("<label for='name' " + String(i + 1) + ">Name: "+ "</label>\n <input type='text' name='name[]' class='' placeholder='Name of your department' required>");

				enterhosts.innerHTML += ("<label for='host' " + String(i + 1) + ">Hosts: "+ "</label>\n <input type='number' name='host[]' class='hosts_department' placeholder='Maximum number of hosts per department is 21' max='21' required>");
				i++;
			}
		}else{
			enterhosts.innerHTML = "";
		}
	});
	
	var hostsDepartment = document.getElementsByClassName("hosts_department");  /*this is an array*/
	enterhosts.addEventListener("input", function(){
		for (var i=0; i < hostsDepartment.length; i++) {
			hostsDepartment[i].addEventListener("input", function(){
				if (this.value > 21){
						this.value = 21;
				}
			});
		}

	});
		
		
		
		

}

function secondFunction(){

}

function isInt(number){
	return number % 1 === 0;
}


function init(){
	var form = document.getElementById("form");
	displayHostsOption();
}


window.onload = init;


