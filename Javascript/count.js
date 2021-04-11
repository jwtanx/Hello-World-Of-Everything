function add() {
  document.querySelector("h1").innerHTML++;
  check(document.querySelector("h1").innerHTML);
}
function minus() {
  document.querySelector("h1").innerHTML--;
  check(document.querySelector("h1").innerHTML);
}
function check(num) {
  if (num % 10 === 0) {
    // alert(f'Now is {num}'); <-- NOT LIKE THIS, we use ` this instead
    alert(`Now is ${num}`);
  }
}

// <-- Trigger when all the DOM (All of the objects) are done loaded
// document.addEventListener("DOMContentLoaded", functionName);

// Below is the other way called anonymous function
document.addEventListener("DOMContentLoaded", function () {
  document.querySelector("button", (id = "add")).onclick = add; // <-- Without the parentheses, just like python, will not work with this line only, you can put it after the button below or do the previous line of code.
  document.querySelector("button", (id = "minus")).onclick = minus; // <-- Without the parentheses, just like python, will not work with this line only, you can put it after the button below or do the previous line of code.
  // OR
  // document.querySelector("button").addEventListener("click", minus);
});

// document.addEventListener("click"); // <-- can be when click, scroll
// document.addEventListener("scroll");
