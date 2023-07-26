let text = document.querySelector('.text')
let gateRight = document.querySelector('.gate-right')
let gateLeft = document.querySelector('.gate-left')
let treeRight = document.querySelector('.tree-right')
let treeLeft = document.querySelector('.tree-left')



window.addEventListener('scroll', () => {
    let value = window.scrollY;
    text.style.marginTop = value * 2.1 + ('px')
    gateRight.style.left = value * 0.8 + ('px')
    gateLeft.style.left = value * -0.8 + ('px')
    treeRight.style.left = value * 0.2 + ('px')
    treeLeft.style.left = value * -0.4 + ('px')
});