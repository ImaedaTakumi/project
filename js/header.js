function header(text="cat"){
    var reader = new FileReader()
    html = reader.readAsText("../html/header.html")
    html = reader.result
    document.write(html);
    var user = document.createElement("li")
    user.textContent = text
    ul1 = document.getElementById("ul")
    l1.appendChild(user)   
}