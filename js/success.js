// ページが読み込まれたらすぐに
$(window).on('load', function () {
    var html = location.href; //URL取得
    if(html == "http://192.168.119.128/project-5/cgi/login_success.cgi"){
        setTimeout(() => {
            window.location.href = "http://192.168.119.128/project-5/cgi/reservation.cgi";
        }, 3000)
    }
    else{
        if(html == "http://192.168.119.128/project-5/cgi/add_success.cgi"){
            setTimeout(() => {
                window.location.href = "http://192.168.119.128/project-5/cgi/login.cgi";
            }, 3000)
        }
    }
});