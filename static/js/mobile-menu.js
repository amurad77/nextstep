menuBtn = document.getElementById("menu-bar");
mobileMenu = document.getElementById("mobile-menu");

if (screen.width <= 1200) {
    mobileMenu.style.display = "none";
}

menuBtn.addEventListener("click", function(e) {
    if (mobileMenu.style.display == "none") {
        mobileMenu.style.display = "block";
    } else {
        mobileMenu.style.display = "none";
    }

    e.preventDefault();
});