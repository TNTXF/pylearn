document.addEventListener("DOMContentLoaded", function() {
    const button = document.getElementById("coolButton");
    const message = document.getElementById("message");

    button.addEventListener("click", function() {
        message.classList.toggle("hidden");
    });
});
