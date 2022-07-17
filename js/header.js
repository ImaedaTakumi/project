function header(text="cat"){
    alert(text)
    var reader = new FileReader()
    html = reader.readAsText("../html/header.html")
    html = reader.result
    document.write(html)
    //document.getElementById("header_1").write(html);
    //var user = document.createElement("li")
    //user.textContent = text
    //ul1 = document.getElementById("ul")
    //l1.appendChild(user) 
}