function sss() {
    var search_num = { 'search_num': document.getElementById('index-search-text').value }
    $.ajax({
        type: "GET",
        url: "result",
        data: search_num,
        success: function(result) {
            alert(result)
            window.location = "/search/result"
        }
    })
    document.getElementById('index-search-text').value = ""
}