console.log('Hello please work')

$(document).ready(function () {

    console.log('Testing ')
    $('.banner-slider').slick({
        dots: true,
        infinite: true,
        speed: 300,
        slidesToShow: 1,
        adaptiveHeight: true
    });
});