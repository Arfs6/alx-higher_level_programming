$(document).ready(function() {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
    const movies = data.results;
    const listMovies = $('#list_movies');
    
    // Loop through the movies and add each title to the list
    movies.forEach(function(movie) {
      const listItem = $('<li></li>').text(movie.title);
      listMovies.append(listItem);
    });
  });
});
