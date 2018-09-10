$("#menu-toggle").click(function (event) {
    event.preventDefault();
    $("#wrapper").toggleClass("toggled");

    if ($('.overlay').attr('data-element') === 'navbar-toggler-icon') {
        $('.overlay').hide();
        $('.overlay').attr('data-element', '');
    } else {
        $('.overlay').show();
        $('.overlay').attr('data-element', 'navbar-toggler-icon');

    }
});
