function header(text="cat"){
    $.ajax({
        url:"../html/header.html",
        cache:false,
        success:function(html){
            document.write(html);
            var user = document.createElement("li")
            user.textContent = text
            ul1 = document.getElementById("ul")
            ul1.appendChild(user)   
        }
    });
}