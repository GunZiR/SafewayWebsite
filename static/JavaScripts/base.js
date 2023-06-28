document.addEventListener("DOMContentLoaded", function(){
		
    window.addEventListener('scroll', function() {
       
        if (window.scrollY > 500) {
            document.getElementById('navbar_top').classList.add('fixed-top');
            // add padding top to show content behind navbar
            navbar_height = document.querySelector('.navbar').offsetHeight;
            document.body.style.paddingTop = navbar_height + 'px';
        } else {
             document.getElementById('navbar_top').classList.remove('fixed-top');
             // remove padding top from body
            document.body.style.paddingTop = '0';
        } 
    });
});
var TxtType = function(el, fullTxt, period) {
    this.fullTxt = fullTxt[0];
    this.el = el;
    this.period = parseInt(period, 10) || 2000;
    this.txt = '';
    this.tick();
    this.delta = 500;
    this.total = 0;
};

TxtType.prototype.tick = function() {
    this.txt = this.fullTxt.substring(0, this.txt.length + 1);
    this.el.innerHTML = '<span class="wrap">' + this.txt + '</span>';

    var that = this;
    var delta = this.delta;
    
    
    if (this.txt === this.fullTxt) {
        delta = this.period;
        console.log('last: ');
        this.txt = '';
    }
    this.total += delta;
    console.log('total: ' + this.total);

    setTimeout(function() {
        that.tick();
    }, delta);
};


window.onload = function() {
    var elements = document.getElementsByClassName('typewrite');
    for (var i=0; i<elements.length; i++) {
        var toRotate = elements[i].getAttribute('data-type');
        var period = elements[i].getAttribute('data-period');
        if (toRotate) {
            new TxtType(elements[i], JSON.parse(toRotate), period);
        }
    }
};