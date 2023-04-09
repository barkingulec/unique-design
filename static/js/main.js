let track = document.getElementById("image-track");
let nextPercentage = -0.1;
let arr = track.getElementsByClassName("image");
let imageTransformX = ((arr[0].offsetWidth / 2) / (arr.length * arr[0].offsetWidth)) * 100;
let text = document.getElementById("img-name");
let temp = (100 - (2 * imageTransformX));


if ( window.location.pathname == '/' ){
    document.getElementsByTagName("body")[0].style.overflow = `hidden`;

} else {
    document.getElementsByTagName("body")[0].style.overflow = `visible`;
}
console.log(document.getElementsByTagName("body")[0].style.overflow, window.location.pathname);

function init() {
    track.style.transform = `translate(-${imageTransformX}%, -50%)`;
    for (let i = 0; i < arr.length; i += 1){
        arr[i].style.objectPosition = `${nextPercentage + 100 - imageTransformX * 2}% 50%`
    }
}

init()

let onDown;
window.onmousedown = e => {
    track.dataset.mouseDownAt = e.x - 100;
    onDown = e.x;
}

window.onmousemove = e => {
    if (!clickedBool) {
        if (track.dataset.mouseDownAt === "0") return;

        const mouseDelta = parseFloat(track.dataset.mouseDownAt) - e.x;
        const maxDelta = window.innerWidth / 1.75;
        const percentage = (mouseDelta / maxDelta) * -100;
        nextPercentage = parseFloat(track.dataset.prevPercentage) + percentage - imageTransformX;
        if (nextPercentage > -imageTransformX){
            nextPercentage = -imageTransformX;
        }
        if (nextPercentage < -(100 - imageTransformX)){
            nextPercentage = -(100 - imageTransformX);
        }
        track.dataset.percentage = nextPercentage;
        
        track.animate({
            transform: `translate(${nextPercentage}%, -50%)`
        }, { duration: 1500, fill: "forwards" });
        
        for (let i = 0; i < arr.length; i += 1){
            arr[i].animate({
                objectPosition: `${nextPercentage + 100 - imageTransformX}% 50%`
            }, { duration: 1500, fill: "forwards" });
            if (Math.abs(nextPercentage) * temp / 100 > temp / arr.length * i && Math.abs(nextPercentage) * temp / 100 < temp / arr.length * (i+1)){
                text.innerHTML = arr[i].dataset.name
            }
        }
    }  
}
let clickedBool = false;
let cur;
let pointer_1 = document.getElementById("pointer_1");
let pointer_2 = document.getElementById("pointer_2");
let courseFullName = document.getElementById("course-name");
let deviceWidth = document.documentElement.clientWidth;
function isClicked(element) {
    if (onUp === onDown) {
        cur = element;
        clickedBool = true;
        text.innerHTML = element.dataset.name.toUpperCase();
        let backBtn = document.getElementById("back-btn");
        for (let img of arr) {
            if (img != element) {
                img.style.width = `0vw`;
                img.style.height = `0vh`;
            }
        }
        courseFullName.innerHTML = element.dataset.fullname.toUpperCase();
        courseFullName.href = element.dataset.id;
        courseFullName.style.top = `40%`;
        courseFullName.style.opacity = `1`;
        courseFullName.style.left = `-${temp + nextPercentage + 45}%`;
        element.style.width = `${deviceWidth + 300}px`;
        element.style.height = `100vh`;
        element.style.position = `absolute`;
        element.style.left = `0%`;
        element.style.top = `0%`;
        element.style.transform = `translate(-47%, -50%)`;
        element.style.objectPosition = `50%, 50%`;
        pointer_1.style.height = `0px`;
        pointer_2.style.height = `0px`;
        backBtn.style.left = `0%`;

        if (selectcoursediv.style.opacity === "1") {
            selectcoursediv.style.top = `150%`;
            selectcoursediv.style.opacity = `0`;
        }

        //track.style.width = `105vw`;
        //track.style.height = `100vh`;
        //track.style.left = `0%`;
        //track.style.top = `100%`;
        //track.style.transform = `translate(-50%, -50%)`;
    }
}

let onUp;

window.onmouseup = e => {
    track.dataset.mouseDownAt = "0";
    track.dataset.prevPercentage = track.dataset.percentage;
    onUp = e.x;
}

function btnClicked(element) {
    for (let img of arr) {
        img.style.width = `40vmin`;
        img.style.height = `56vmin`;
    }
    cur.style.removeProperty('position');
    cur.style.removeProperty('left');
    cur.style.removeProperty('top');
    cur.style.removeProperty('transform');
    cur.style.objectPosition = `94%, 50%`;
    pointer_1.style.height = `20px`;
    pointer_2.style.height = `20px`;
    element.style.left = `-20%`;
    courseFullName.style.top = `-40%`;
    courseFullName.style.opacity = `0`;
    clickedBool = false;
}
