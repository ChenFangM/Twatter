$(document).ready(function(){
    
  $("ul").on("click", "li", function(){
   $(this).toggleClass("completed");
 });
 
 
 $("ul").on("click", "span", function(event){
   $(this).parent().fadeOut(500,function(){
     $(this).remove();
   });
   event.stopPropagation();
 });
 
 $("input[type='text']").keypress(function(event){
   if(event.which === 13){
     
     var todoText = $(this).val();
     $(this).val("");
   
     $("#list").append("<li><span><i class='fa fa-trash'></i></span> " + todoText + "</li>")
   }
 });
 
 $(".fa-plus").click(function(){
   $("input[type='text']").fadeToggle();
 });   
     
 window.addEventListener("beforeunload", function(event) {
  console.log(document.getElementById("#list"));
  //is null rn must get elements in listos
  
 });
     
});
