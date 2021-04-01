function $id(id) {
    return document.getElementById(id);
}


function SendCredentials() {
    let xhr = new XMLHttpRequest();
	let formData = new FormData();

    var email = $id("email");
    var password = $id("password");

    var message = $id("message")

    if(email.value.length < 1) {
        message.style = "display: flex";
        message.textContent = "please enter email address"
        return;
    }

    if(password.value.length < 6) {
        message.style = "display: flex";
        message.textContent = "password is too short"
        return;
    }
    
    xhr.onreadystatechange = state => { 
        if (xhr.readyState == XMLHttpRequest.DONE) {
            message.style = "display: flex";
            message.textContent = xhr.responseText;
        }
    } 

    formData.append("email", email.value)
    formData.append("password", password.value)

    xhr.open("POST", '', true);
	xhr.send(formData);
}