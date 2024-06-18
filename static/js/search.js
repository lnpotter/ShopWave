document.addEventListener('DOMContentLoaded', function() {
    const searchForm = document.getElementById('searchForm');
  
    searchForm.addEventListener('submit', function(event) {
      event.preventDefault();
     
      const formData = new FormData(searchForm);
      const query = formData.get('q');
     
      fetch(`/search/?q=${query}`)
        .then(response => response.json())
        .then(data => {
          const resultsContainer = document.querySelector('.row.wow.fadeIn');
          resultsContainer.innerHTML = '';
  
          data.items.forEach(item => {
            const cardHTML = `
              <div class="col-lg-3 col-md-6 mb-4">
                <div class="card">
                  <div class="view overlay">
                    <img src="${item.image}" class="card-img-top">
                    <a href="${item.url}">
                      <div class="mask rgba-white-slight"></div>
                    </a>
                  </div>
                  <div class="card-body text-center">
                    <a href="" class="grey-text">
                      <h5>${item.category}</h5>
                    </a>
                    <h5>
                      <strong>
                        <a href="${item.url}" class="dark-grey-text">${item.title}</a>
                      </strong>
                    </h5>
                    <h4 class="font-weight-bold blue-text">
                      <strong>$${item.price}</strong>
                    </h4>
                  </div>
                </div>
              </div>
            `;
            resultsContainer.innerHTML += cardHTML;
          });
        })
        .catch(error => console.error('Error fetching search results:', error));
    });
  });