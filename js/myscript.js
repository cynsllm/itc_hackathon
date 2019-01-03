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
    $("#myBtn1").click(function () {
        if ($(".chat-box.shadowed").css("display") === "none") {
            $(".chat-box.shadowed").css("display", "block");
        } else {
            $(".chat-box.shadowed").css("display", "none")
        }
    });
    $(".cows").on("click", function () {
        $("#info_cows").css("display", "block");
        $("#info_healthy").css("display", "none");
        $("#info_milk").css("display", "none");
        $("#dash").css("display", "none");
    });
    $(".milk").on("click", function () {
        $("#info_milk").css("display", "block");
        $("#info_healthy").css("display", "none");
        $("#info_cows").css("display", "none");
        $("#dash").css("display", "none");

    });
    $(".healthy").on("click", function () {
        $("#info_healthy").css("display", "block");
        $("#info_milk").css("display", "none");
        $("#info_cows").css("display", "none");
        $("#dash").css("display", "none");

    });
    $(".main_menu").on("click", function () {
        $("#dash").css("display", "flex");
        $("#info_healthy").css("display", "none");
        $("#info_milk").css("display", "none");
        $("#info_cows").css("display", "none");
    });
     $(".logo").on("click", function () {
        $("#dash").css("display", "flex");
        $("#info_healthy").css("display", "none");
        $("#info_milk").css("display", "none");
        $("#info_cows").css("display", "none");
    });
});


