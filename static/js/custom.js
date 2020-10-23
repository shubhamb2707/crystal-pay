

$=jQuery

$( document ).ready(function() {





});

















$(window).scroll(function() {
    if ($(this).scrollTop() > 300){  
        $('header.main_header').addClass("sticky");
    }
    else{
        $('header.main_header').removeClass("sticky");
    }
});


 

function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}

 


(function(){
    /* Mobile */
    $('#menu-wrap').prepend('<div id="menu-trigger">Menu</div>');   
    $("#menu-trigger").on("click", function(){
      $("#menu").slideToggle();
    });

    // iPad
    var isiPad = navigator.userAgent.match(/iPad/i) != null;
    if (isiPad) $('#menu ul').addClass('no-transition');      
})();   





