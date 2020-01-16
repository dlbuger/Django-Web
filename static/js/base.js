function showToast() {
    var x = document.getElementById('toast')
    x.classList.add("show")
    setTimeout(function () {
        x.classList.remove("show")
    }, 3000)
}

// Refresh when back is clicked!
var perfEntries = performance.getEntriesByType("navigation");
if (perfEntries[0].type === "back_forward") {
    location.reload(true);
}