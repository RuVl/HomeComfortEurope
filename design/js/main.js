
$(document).ready(function() {
	

	$('.rangeCategory').hover(function() {
	    $('.rangeImageContainer').hide();
	    var id = this.id;
		$('.rangeImageContainer[data-order="'+id+'_0"]').show();
	});
	
	$('.rangeHover').hover(function() {
		$('.rangeImageContainer').hide();
  		var id = this.id;
  		$('.rangeImageContainer#' + id).show();
  		console.log('.rangeImageContainer#' + id);
	});





	$('.slider-multi').slick({
        dots: true,
        infinite: true,
        speed: 9000
        
    });
   $('.srchWrp a.srch').click(function(){
		$('.srchWrp span').addClass('show');
	});
	
	$('.srchWrp a.close').click(function(){
		$('.srchWrp span').removeClass('show');
	});
	
	$('.nav-mob').click(function() {
        $('.botSec ul.nav').slideToggle('slow');
    });
	
	$('.multiple-items').slick({
   	infinite: true,
  	slidesToShow: 5,
  	slidesToScroll: 5
    });
    $(".mob-search").hide();
	$('.srchWrp a.mob-account').click(function(){
        $( ".mob-search" ).toggle( "slow" );
	});
	$('.responsive').slick({
        dots: true,
        infinite: true,
        speed: 500,
        slidesToShow: 1,
        slidesToScroll: 1,
		autoplay: true,
		fade: true,
		focusOnSelect: true,
		lazyLoad: 'ondemand',
	  	autoplaySpeed: 5000,
		asNavFor : '.slideContent',
        mobileFirst : true,
		onBeforeChange: function() {
                $('.slick-active > .display').addClass('animated fadeInDown');
                $('.slick-active > .display').addClass('hidden');
            },
            onAfterChange: function() {
                $('.slick-active > .display').removeClass('hidden');
                $('.slick-active > .display').addClass('animated fadeInDown');
            }
    });
	
	
	
	$(".mob-menu").click(function() {
		if($(".dropdown").hasClass("show")){
			$(".dropdown").removeClass("show");
			$(".mob-menu").removeClass("show");
		}else{
			$(".dropdown").addClass("show");
			$(".mob-menu").addClass("show");
		}
	});
	
	if($(window).innerWidth() < 820){
		$('li.bg').click(function(e) { 
			$(this).parent().toggleClass("mob-collection");
			if ($(this).parent().is('.mob-collection')) {
				$(this).removeClass("bg").addClass("bg-minus");
			} else {
				$(this).removeClass("bg-minus").addClass("bg");
			}

			e.stopPropagation();
			if($(this).find('.submenu').hasClass('show')){
				$(this).find('.submenu').removeClass('show');
				$(this).find('.submenu').hide();

			}else{
				$('.bg').find('.submenu').removeClass('show');
				$('.bg').find('.submenu').hide();
				$(this).find('.submenu').addClass('show');
				$(this).find('.submenu').slideDown('fast');	
			}
		});
		
		
		$('.sub-submenu > li').click(function(e) {
            e.stopPropagation();
        });		
	}
	
	
	$("nav ul.top-links li.account, li.account a.mob-account").click(function() {
		if($(".dropdownL").hasClass("show")){
			$(".dropdownL").removeClass("show");
			$("nav ul.top-links li.account").removeClass("show");
		}else{
			$(".dropdownL").addClass("show");
			$("nav ul.top-links li.account").addClass("show");
		}
	});

		
	$(".view_basket .row.basket-view").click(function() {
		if($(".dropdownT").hasClass("show")){
			$(".dropdownT").removeClass("show");
			$(".view_basket .row.basket-view").removeClass("show");
		}else{
			$(".dropdownT").addClass("show");
			$(".view_basket .row.basket-view").addClass("show");
		}
	});
	
$(".searchS, .close_form").click(function() {
		if($(".searchWrp").hasClass("show")){
			$(".searchWrp").removeClass("show");
			$(".searchS").removeClass("show");
		}else{
			$(".searchWrp").addClass("show");
			$(".searchS").addClass("show");
		}
	});
	
	$('.toggle').on('click', function() {
  $('.loginMiddle').stop().addClass('active');
});

$('.close').on('click', function() {
  $('.loginMiddle').stop().removeClass('active');
});

$(window).load(function() {
	  $('.flexslider').flexslider({
		animation: "slide",
		itemWidth: 90,
		controlNav: false,
		itemMargin: 5
	  });
	});
	
});



