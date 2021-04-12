function $id(id) {
    return document.getElementById(id);
}


function SendMessage() {
    let xhr = new XMLHttpRequest();
	let formData = new FormData();

    var text = $id("text");

    var message = $id("message")
    message.textContent = "";

    xhr.onreadystatechange = state => { 
        if (xhr.readyState == XMLHttpRequest.DONE) {
            message.style = "display: flex";
            message.textContent = xhr.responseText;
        }
    } 

    formData.append("message", text.value)

    xhr.open("POST", '', true);
	xhr.send(formData);
}

function EventLoop() {
    let xhr = new XMLHttpRequest();

    console.log("Start loop")

    xhr.onreadystatechange = state => { 
        if (xhr.readyState == XMLHttpRequest.DONE) {
            message.style = "display: flex";
            message.textContent = xhr.responseText;

            ProcessEvents(xhr.responseText)

            console.log("Response")
            xhr.open("GET", document.location.origin + "/get_status", true);
            xhr.send();
        }
    }

    xhr.open("GET", document.location.origin + "/get_status", true);
    xhr.send();
}

function ProcessEvents(events) {
    var events_json = JSON.parse(events)
    console.log(events_json);
    for (var e in events_json) {
        var event = events_json[e]
        if (event.type == "Message") {
            AddMessage(event.text)
        }
    }
}

function AddMessage(message) {
    console.log("message: " + message)
    var container = $id("messages")
    var tag = document.createElement("p")
    var text = document.createTextNode("" + message);
    tag.appendChild(text)
    container.appendChild(tag)
}