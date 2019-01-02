$.getJSON("http://api.openweathermap.org/data/2.5/weather?q=tel%20aviv&APPID=13f1f80994cd71ca577de534eddb82af&units=metric%22", function( data ) {
   console.log(data);
   var city = data.name;
  var temp = data.main.temp;
  var humid = data.main.humidity;
  $(".temp").text(temp)
  $(".humid").text(humid + "%")
   });


  $(document).ready(function () {
        $("#myBtn").click(function(){
            if ($(".chat-box.shadowed").css("display") === "none") {
                $(".chat-box.shadowed").css("display", "block");
            } else {
                $(".chat-box.shadowed").css("display", "none")
            }
        });
  });





var scriptElement = document.createElement('script');
scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
vizElement.parentNode.insertBefore(scriptElement, vizElement);