async function db(){
    let response = await fetch("https://teilnahme-gewinnspiel.de/cgi-bin/db_umfragen.py");
    let jsonData = response.json(); 

     
    jsonData.then((result) => {
    
	
    var $table = $('#table');
    $table.bootstrapTable({data: result
	})});
     };
    
db()