showMore = document.getElementById("show-more");
moreTrainers = document.getElementById("show-more-trainers");

showMore.addEventListener("click", function(e) {
    moreTrainers.style.display = "flex";
    showMore.style.display = "none";

    e.preventDefault();
});