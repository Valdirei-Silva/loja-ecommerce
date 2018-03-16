$(document).ready(function() {
  $('.owl-carousel').owlCarousel({
	loop: true,
	margin: 10,
	responsiveClass: true,
	responsive: {
	  0: {
		items: 1,
		nav: true
	  },
	  480: {
		items: 3,
		nav: false
	  },
	  768: {
		items: 4,
		nav: true,
		loop: false,
		margin: 15
	  }
	}
  })
})
