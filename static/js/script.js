var nextBtn = document.getElementById("next");
var firstpage = document.getElementById("firstpage");
var secondpage = document.getElementById("secondpage");
nextBtn.addEventListener("click", function(e) {
    firstpage.style.display = "none";
    secondpage.style.display = "flex";
    e.preventDefault();
});

var selectList = document.getElementById("select-list").children;
var otherinput = document.getElementById("otherinput");
for (var i = 0; i < selectList.length; i++) {
    if (selectList[i].id != 'othertech') {
        selectList[i].addEventListener("click", function() {
            otherinput.style.display = "none";
        })
    } else {
        selectList[i].addEventListener("click", function() {
            otherinput.style.display = "block";
        })
    }
}