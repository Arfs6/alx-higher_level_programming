$(document).ready(function() {
  $.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    method: 'GET',
    dataType: 'jsonp',
    success: function() {
      console.error(data);
      $('#hello').text(data.hello);
      $('footer').text(data);
    }
  })
});
