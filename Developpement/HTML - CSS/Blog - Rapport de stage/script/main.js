// Récupérer la référence de l'élément de recherche dans le HTML
const searchInput = document.querySelector('#search-input');

// Récupérer tous les articles une seule fois au chargement de la page
const articles = document.querySelectorAll('#articles-container article');

// Récupérer l'élément du message d'absence de résultats
const noResultsMessage = document.querySelector('#no-results-message');

// Récupérer la première section
const firstSection = document.querySelector('.entreprise');

// Écouter l'événement de saisie de l'utilisateur dans la zone de recherche
searchInput.addEventListener('input', function() {
  const searchTerm = searchInput.value.toLowerCase();
  let foundResults = false; // Variable pour vérifier si des résultats ont été trouvés

  // Parcourir tous les articles et afficher ou masquer en fonction du terme de recherche
  articles.forEach(function(article) {
    const title = article.querySelector('h2').textContent.toLowerCase();
    const content = article.querySelector('p').textContent.toLowerCase();

    if (title.includes(searchTerm) || content.includes(searchTerm)) {
      article.style.display = 'block';
      foundResults = true; // Des résultats ont été trouvés
      firstSection.style.display = 'flex'
    } else {
      article.style.display = 'none';
      firstSection.style.display = 'none'
    }
  });

  // Afficher ou masquer le message d'absence de résultats
  if (foundResults) {
    noResultsMessage.style.display = 'none';
  } else {
    noResultsMessage.style.display = 'block';
  }
});