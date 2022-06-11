(function($){
  $(function(){

    $('.sidenav').sidenav();
    $('.parallax').parallax();
    // Search Modal
    $('.modal').modal();
    $('.tooltipped').tooltip();



    $(".dropdown-trigger").dropdown();
  }); // end of document ready
})(jQuery); // end of jQuery name space


// document.addEventListener('DOMContentLoaded', function () {
//   var elems = document.querySelectorAll('.modal');
//   var instances = M.Modal.init(elems, options);
// });

// Or with jQuery

$(document).ready(function () {
  $('.modal').modal();
  $('.tooltipped').tooltip();
  $(".dropdown-trigger").dropdown();


});
