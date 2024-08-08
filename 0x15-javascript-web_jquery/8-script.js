$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    success: function (data) {
      const movies = data.results;
      movies.forEach(movie => {
        $('#list_movies').append('<li>' + movie.title + '</li>');
      });
    }
  });
});
