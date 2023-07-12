var myCarousel = document.querySelector('#carouselExampleControls')
var myModalEl = document.getElementById('popupImage')

myModalEl.addEventListener('show.bs.modal', function (event) {
    const trigger = event.relatedTarget
    var bsCarousel = bootstrap.Carousel.getInstance(myCarousel)
    bsCarousel.to(trigger.dataset.bsSlideTo)
})