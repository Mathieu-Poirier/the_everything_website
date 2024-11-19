let value = 0;

function Increment() {
	
   fetch(`http://127.0.0.1:8000/button?value=${value}`, {
	   method: "POST"
	   
   }).then((response) => response.json()).then((json) => {console.log(json); value = Number(json);});

   
}
