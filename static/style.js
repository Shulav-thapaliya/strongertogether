// navigation bar 













// section1 changing words 
const item = document.querySelectorAll('.section1div h1')

// changing the words slide slow 
let i = 1
setInterval(() => {
    i++
    const items = document.querySelector('h1.change')
    items.classList.remove('change')
    if (i > item.length) {
        item[0].classList.add('change')
        i = 1
    } else {

        items.nextElementSibling.classList.add('change')

    }








}, 2000)

// end of section1 changing words