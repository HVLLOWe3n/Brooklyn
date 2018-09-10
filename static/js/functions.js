$("#menu-toggle").click(function (event) {
    event.preventDefault();
    $("#wrapper").toggleClass("toggled");
});

$(document).on('click', '.navbar-toggler-icon', function(e){
  e.preventDefault();
  $('.overlay').show();
  $('.overlay').data('element', 'navbar-toggler-icon');
});
