function $id(id) {
    return document.getElementById(id);
}


function SendMessage() {
    let xhr = new XMLHttpRequest();
	let formData = new FormData();

    var to = $id("to");
    var text = $id("text");

    var message = $id("message")
    message.textContent = "";

    xhr.onreadystatechange = state => { 
        if (xhr.readyState == XMLHttpRequest.DONE) {
            message.style = "display: flex";
            message.textContent = xhr.responseText;
        }
    } 

    formData.append("to", to.value)
    formData.append("message", text.value)

    xhr.open("POST", '', true);
	xhr.send(formData);
}