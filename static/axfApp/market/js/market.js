$(function () {
//http://59.110.233.209:8000/market/103638/
    console.log("hello");
    var urlStr = location.href;
    var categoryId ="yellow" + urlStr.split("/")[4];
    var $span = $(document.getElementById(categoryId));
    $span.addClass("yellow")
});