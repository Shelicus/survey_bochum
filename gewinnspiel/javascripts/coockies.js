$('#win_form').on('submit', function() {
  	
    let alreadyFiltout = getCookie();
    if(alreadyFiltout !== '1'){
        if (document.getElementById('selector').value === '0'){
          setCoockie();
        }
        return true;
    }else {
      	
        window.location.replace("https://teilnahme-gewinnspiel.de/unsuccessful.html");
      	return false;
        
    }


    
});

function setCoockie(){
    const d = new Date();
    d.setTime(d.getTime() + (3*365*24*60*60*1000));
    let expires = "expires="+ d.toUTCString();
    document.cookie = "alreadyFiltout=1;"+expires+";path=/";
}

function getCookie(){
    const name = "alreadyFiltout";
    let ca = document.cookie.split(';');
  for(let i = 0; i < ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length+1, c.length);
    }
  }
  return "";
}