$(document).ready(function(){

  const newTasks = [];
  const finTasks = [];

  $("ul").on("click", "li", function(){
   $(this).toggleClass("completed");
 });


 $("ul").on("click", "span", function(event){
   $(this).parent().fadeOut(500,function(){
     finTasks.push((this).textContent);
     $(this).remove();
   });
   event.stopPropagation();
 });

 $("input[type='text']").keypress(function(event){
   if(event.which === 13){

     var todoText = $(this).val();
     newTasks.push(todoText);
     
     $(this).val("");

     $("#list").append("<li><span><i class='fa fa-trash'></i></span> " + todoText + "</li>")
   }
 });

 $(".fa-plus").click(function(){
   $("input[type='text']").fadeToggle();
 });

 window.addEventListener("beforeunload", function(event) {
  event.returnValue = null;

  console.log("New");
  if (newTasks.length > 0){
    for (task in newTasks) {
      console.log(newTasks[task]); //Must "coerce" element into string?
      $.ajax({
        url: "/updating",
        type: "GET",
        data: {
          task : newTasks[task]
        }
      })
    }
  }

  console.log("Old");
  if (finTasks.length > 0){
    for (task in finTasks) {
      console.log(finTasks[task]);
    }
    $.ajax({
      url: "/updating",
      type: "POST",
      data: {
        task : finTasks[task]
      }
    })
  }
  //is null rn must get elements in listos

 });


});
