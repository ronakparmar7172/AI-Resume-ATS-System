const input = document.getElementById("resumeInput");
const fileNamesDiv = document.getElementById("fileNames");

input.addEventListener("change", function () {
    fileNamesDiv.innerHTML = "";
    for (let file of input.files) {
        const p = document.createElement("p");
        p.textContent = "✔ " + file.name;
        fileNamesDiv.appendChild(p);
    }
});
