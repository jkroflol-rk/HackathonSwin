function deleteAnimation(){
	const hello = document.querySelectorAll(".hello");
	const button2 = document.querySelectorAll(".test_btn");
	button2.forEach((button, index) => {
		button.addEventListener('click', () => {
		  const card = hello[index];
		  card.classList.add('move-hello');
	  
		  setTimeout(() => {
			card.remove();
		  }, 800);
		});
	});
}

function collapseAnimation(){
    var coll = document.getElementsByClassName("collapsible");
    var i;

    for (i = 0; i < coll.length; i++) {
        coll[i].addEventListener("click", function() {
            // alert();
            this.classList.toggle("active2");
            var content = this.nextElementSibling;
            if (content.style.maxHeight){
                content.style.maxHeight = null;
            } else {
                content.style.maxHeight = content.scrollHeight + "px";
            }
        });
    }
}

function init(){
	deleteAnimation();
    collapseAnimation();

}


window.onload = init;