let inp = document.getElementById("in1")
let btn = document.getElementById("btn")

function showPassword () {
    inp.type = "text";
}

btn.addEventListener("click", showPassword)