$(document).ready(function(){
    $( '.func1 button' ).click(function() {
        $('.func1 p').addClass('red');
    });
    $('.butSlide').click(function(){
        $('.imgSlide').slideToggle('slow');
    });
    $('.butTog').click(function(){
        $('.imgTog').toggle('slow');
    });
    $( ".butDown" ).click(function() {
        $( ".imgDown" ).slideDown( "slow");
    });
    $( ".butUp" ).click(function() {
        $( ".imgDown" ).slideUp( "slow");
    });
    $('.butBefore').click(function() {
        $('.func3 p').before(' and then?');
    });
    $('.butAppend').click(function() {
        $('.func3 p').append(' and then?');
    });
    $('.butAfter').click(function() {
        $('.func3 p').after(' and then?');
    });
});