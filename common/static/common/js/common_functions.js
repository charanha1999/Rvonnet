

var mobileMenuBtn = document.querySelector("#mobile-menu-btn");
var mobileMenu = document.querySelector(".mobile-menu");


// Function used for van bar for mobile view 
mobileMenuBtn.addEventListener("click", () => {
    console.log($('#mainContent'));

    if (mobileMenu.style.display === "none") {
        mobileMenu.style.display = "flex";
        mobileMenuBtn.innerHTML = "Close";
    } 
    else {
        mobileMenu.style.display = "none";
        mobileMenuBtn.innerHTML = "Menu";
    }
});



// ajax call used for logging out the user 
