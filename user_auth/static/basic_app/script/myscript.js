console.log('hello there!!');
$('.nav .nav-link').click(function(){
  console.log('clicked a link')
  $(this).toggleClass("active");
  })
