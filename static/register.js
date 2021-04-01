function $id(id) {
    return document.getElementById(id);
}


function SendCredentials() {
    let xhr = new XMLHttpRequest();
	let formData = new FormData();

    var login = $id("login");
    var email = $id("email");
    var password = $id("password");
    var password2 = $id("password2");

    if(password.value != password2.value) {
        $id("message").style = "display: flex";
        return;
    }
    
    xhr.onreadystatechange = state => { 
        if (xhr.readyState == XMLHttpRequest.DONE) {
            login.value = xhr.responseText;
        }
    } 

    formData.append("login", login.value)
    formData.append("email", email.value)
    formData.append("password", password.value)

    xhr.open("POST", '', true);
	xhr.send(formData);
}