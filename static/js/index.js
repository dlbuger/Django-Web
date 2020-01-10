function sss() {
    var search_num = document.getElementById('index-search-text').value
    if (search_num == "")
        alert("输入不能为空")
    else{
        $.ajax({
            type: "GET",
            url: "",
            data: search_num,
            success: function(result) {
                $(window).attr("location", "search/result/" + search_num);
            },
        })
        document.getElementById('index-search-text').value = ''
    }

}

function showToast() {
    var x = document.getElementById('toast')
    x.classList.add("show")
    setTimeout(function(){
        x.classList.remove("show")
    },3000)
}