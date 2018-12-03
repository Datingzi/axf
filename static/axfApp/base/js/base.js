$(function () {
    //设置rem的值,设置为手机屏幕的高度的20分之一
    document.documentElement.style.fontSize = innerHeight/20+"px";

    //      http://59.110.233.209:8000/home/
    var urlStr = location.href;
    var idStr = urlStr.split("/")[3];
    var $span = $(document.getElementById(idStr));
    $span.css("background","url(/static/axfApp/base/img/"+idStr+"1.png)");
    $span.css("background-size","0.9rem")
});