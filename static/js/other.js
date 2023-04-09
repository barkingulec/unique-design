let selectcoursediv = document.getElementById("selectcoursediv");

function showEnroll() {
    if (!clickedBool) {
        if (selectcoursediv.style.opacity === "1") {
            selectcoursediv.style.top = `150%`;
            selectcoursediv.style.opacity = `0`;
        }
        else {
            selectcoursediv.style.top = `50%`;
            selectcoursediv.style.opacity = `1`;
        }
    }

}

function closeEnroll() {
    selectcoursediv.style.top = `150%`;
    selectcoursediv.style.opacity = `0`;
}