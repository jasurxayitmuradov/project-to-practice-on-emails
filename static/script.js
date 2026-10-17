const button = document.querySelector("#helloButton");
const message = document.querySelector("#helloMessage");
button.addEventListener("click", function() {
    message.textContent = "Hello, Jasur";
});
