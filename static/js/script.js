var nextBtn = document.getElementById("next");
var firstname = document.getElementById("id_name");
var surname = document.getElementById("id_surname");
var email = document.getElementById("id_email");
var number = document.getElementById("id_number");
var firstpage = document.getElementById("firstpage");
var secondpage = document.getElementById("secondpage");

nextBtn.addEventListener("click", function(e) {
    if (firstname.value=="" || surname.value=="" || email.value=="" || number.value=="") {
        document.getElementById("alert").style.display = "inline-block";
        setTimeout(() => {
            document.getElementById("alert").style.display = "none";
        }, "3000");
    } else {
        firstpage.style.display = "none";
        secondpage.style.display = "flex";
    }
    e.preventDefault();
});