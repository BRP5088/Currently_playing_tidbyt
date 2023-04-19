
console.log('document.getElementsByClassName("person_table") === ', document.getElementsByClassName("person_table") );

document.getElementsByClassName("person_table")[0].addEventListener("input", function () {
    document.getElementById("log").value += "input event fired\n";
}, false);
