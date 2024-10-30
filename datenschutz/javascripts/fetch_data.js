async function db(){
    let response = await fetch("https://umfrage-datenschutz.de/cgi-bin/db.py");
    let jsonData = response.json(); 

     
    jsonData.then((result) => {
    
	
    var $table = $('#table');
    $table.bootstrapTable({data: result
	})});
     };
    
db()