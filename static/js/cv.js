console.log("zsadfgh")

$(document).on("click", "a", function() {
    //this == the link that was clicked
    console.log(4567)
    var href = $(this).attr("href");
    if(href==="#sec-3")
    {
        setTimeout(function() {
            // Code to be executed after the delay
        $("#sec-3").load(location.href+" #sec-3","");

          }, 400);
    }
   // alert(" 1 You're trying to go to " + href);
});
