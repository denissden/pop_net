function $id(id) {
    return document.getElementById(id);
}


function SendCredentials() {
    let xhr = new XMLHttpRequest();
	let formData = new FormData();

    var login = $id("login");
    var email = $id("email");
    var first_name = $id("first_name");
    var last_name = $id("last_name");
    var password = $id("password");
    var password2 = $id("password2");

    var message = $id("message")

    if(email.value.length < 1) {
        message.style = "display: flex";
        message.textContent = "please enter email address"
        return;
    }

        if(email.value.length < 1) {
        message.style = "display: flex";
        message.textContent = "please enter login"
        return;
    }

    if(first_name.value.length < 1) {
        message.style = "display: flex";
        message.textContent = "please enter first name"
        return;
    }

    if(last_name.value.length < 1) {
        message.style = "display: flex";
        message.textContent = "please enter last name"
        return;
    }

    if(password.value.length < 6) {
        message.style = "display: flex";
        message.textContent = "password is too short"
        return;
    }

    if(password.value != password2.value) {
        message.style = "display: flex";
        message.textContent = "passwords do not match"
        return;
    }
    
    xhr.onreadystatechange = state => { 
        if (xhr.readyState == XMLHttpRequest.DONE) {
            message.style = "display: flex";
            message.textContent = xhr.responseText;
        }
    } 

    formData.append("login", login.value)
    formData.append("email", email.value)
    formData.append("first_name", first_name.value)
    formData.append("last_name", last_name.value)
    formData.append("password", password.value)

    xhr.open("POST", '', true);
	xhr.send(formData);
}