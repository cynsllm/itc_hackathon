$.getJSON("http://api.openweathermap.org/data/2.5/weather?q=tel%20aviv&APPID=13f1f80994cd71ca577de534eddb82af&units=metric", function( data ) {
   console.log(data);
   var city = data.name;
  var temp = data.main.temp;
  //var temp = data.main.temp - 273;
  //var rounded = temp.toFixed(1);
  //console.log(rounded)
  var humid = data.main.humidity;
  $(".temp").text(temp)
  $(".humid").text(humid + "%")
   });





$(document).ready(function () {
    $("#myBtn").click(function () {
        if ($(".chat-box.shadowed").css("display") === "none") {
            $(".chat-box.shadowed").css("display", "block");
        } else {
            $(".chat-box.shadowed").css("display", "none")
        }
    });
    $(".cows").on("click", function () {
            $("#dash").css("display", "none");
            $(".milk-data").css("display", "none")
            $(".health-data").css("display", "none")
            $(".cows-data").css("display", "block")
    });
    $(".milk").on("click", function () {
            $("#dash").css("display", "none");
            $(".cows-data").css("display", "none")
            $(".health-data").css("display", "none")
            $(".milk-data").css("display", "block")
    });
    $(".healthy").on("click", function () {
            $("#dash").css("display", "none");
            $(".cows-data").css("display", "none")
            $(".milk-data").css("display", "none")
            $(".health-data").css("display", "block")
    });
     $(".home").on("click", function () {
        $("#dash").css("display", "block");
        $(".health-data").css("display", "none")
        $(".milk-data").css("display", "none")
        $(".cows-data").css("display", "none")
    });
    //$(".cows").on("click", function () {
        //if($("#dash").css("display") === "block"){
            //$("#dash").css("display", "none");
    //}else{
        //$("#dash").css("display", "block");}
    //});
    //$(".close").on("click", function () {
        //$("#info_cows").css("display", "none");
    //});
    //$(".milk").on("click", function () {
        //$("#info_milk").css("display", "block");
    //});
    //$(".close").on("click", function () {
        //$("#info_milk").css("display", "none");
    //});
    //$(".healthy").on("click", function () {
        //$("#info_healthy").css("display", "block");
    //});
    //$(".close").on("click", function () {
        //$("#info_healthy").css("display", "none");
    //});
});




//$("#dash").html("<div>HELLO WORLD</div>")


var scriptElement = document.createElement('script');
scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
vizElement.parentNode.insertBefore(scriptElement, vizElement);