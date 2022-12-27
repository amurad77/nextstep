var selectOption = document.getElementById("id_what_idea");
setTimeout(function () {
    selectOption.children[0].setAttribute("value", "");
    selectOption.children[0].setAttribute("disabled", "");
    document.getElementById("id_hours").setAttribute("required", "");
    document.getElementById("id_hours").children[0].setAttribute("value", "");
    document.getElementById("id_hours").children[0].setAttribute("disabled", "");
    document.getElementById("id_people").setAttribute("required", "");
    document.getElementById("id_people").children[0].setAttribute("value", "");
    document.getElementById("id_people").children[0].setAttribute("disabled", "");
    document.getElementById("id_more_information").setAttribute("maxlength", "600");
}, 2000);

var value = "";
selectOption.addEventListener("change", function() {
    value = selectOption.options[selectOption.selectedIndex].value;
});

function ValidateEmail(input) {
    var validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    if (input.value.match(validRegex)) {
      return true;
    } else {
      return false;
    }
}

var nextBtn = document.getElementById("next");
var firstname = document.getElementById("id_name");
var surname = document.getElementById("id_surname");
var email = document.getElementById("id_email");
var number = document.getElementById("id_number");
var firstpage = document.getElementById("firstpage");
var secondpage = document.getElementById("secondpage");

nextBtn.addEventListener("click", function (e) {
    if (firstname.value == "" || surname.value == "" || email.value == "" || number.value == "" || value == "" || ValidateEmail(email) == false) {
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