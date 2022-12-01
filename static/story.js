document.querySelectorAll('.button1').forEach((newitem) => {
    newitem.addEventListener('click', () => {
        document.querySelectorAll('.commentContainer').forEach((newitem) => {
            newitem.classList.toggle('change')

        })
    })
})