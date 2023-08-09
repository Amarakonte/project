// Créer un observateur d'intersection
const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        console.log(entry);
        if (entry.isIntersecting) {
            entry.target.classList.add('show');
        } else {
            entry.target.classList.remove('show');
        }
    });
});

// Sélectionner tous les éléments cachés à observer
const hiddenElements = document.querySelectorAll('.hidden');
hiddenElements.forEach((el) => {
    observer.observe(el);
});

// Bouton retour haut de page
const btn = document.querySelector('.btn')
btn.addEventListener('click', ()=> {
  window.scrollTo({
    top: 0,
    left: 0,
    behavior: "smooth"
  })
})