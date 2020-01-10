function sss() {
    var search_num = document.getElementById('index-search-text').value
    $.ajax({
        type: "GET",
        url: "",
        data: search_num,
        success: function(result) {
            $(window).attr("location", "search/result/" + search_num);
        },
        error: function(result) {
            alert("输入不能为空")
        }
    })
    document.getElementById('index-search-text').value = ''
}