$(function () {
//http://59.110.233.209:8000/market/103638/
    console.log("hello");
    var urlStr = location.href;
    var categoryId ="yellow" + urlStr.split("/")[4];
    var $span = $(document.getElementById(categoryId));
    $span.addClass("yellow")



    //  点击分类和排序
    var $typeBtn = $("#typeBtn");
    var $sortBtn = $("#sortBtn");
    var $typeDiv = $("#typeDiv");
    var $sortDiv = $("#sortDiv");

    $typeBtn.bind("click",function () {
        $typeDiv.toggle();
        $sortDiv.hide();
    });
    $sortBtn.bind("click",function () {
        $sortDiv.toggle();
        $typeDiv.hide()
    });
    //点击空白区域，隐藏
    function func() {
        $(this).hide();
    }
    $typeDiv.bind("click",func);
    $sortDiv.bind("click",func);
});