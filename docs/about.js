transition=document.getElementById('about');

function aboutAnimation() {
    setInterval(() => {
        transition.style.transform='translateY(0px)';
        transition.style.opacity='1';    
    },10)
}