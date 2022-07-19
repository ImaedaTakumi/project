// ページが読み込まれたらすぐに
$(window).on('load', function () {
    var html = location.href; //URL取得
    if(html == "http://192.168.229.128/project/cgi/login_success.cgi"){
        setTimeout(() => {
            window.location.href = "http://192.168.229.128/project/cgi/reservation.cgi";
        }, 3000)
    }
    else{
        if(html == "http://192.168.229.128/project/cgi/add_success.cgi"){
            setTimeout(() => {
                window.location.href = "http://192.168.229.128/project/cgi/login.cgi";
            }, 3000)
        }
    }
});