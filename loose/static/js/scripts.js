$(document).ready(function() {
  $.simpleWeather({
    location: 'Austin, TX',
    woeid: '',
    unit: 'f',
    success: function(weather) {
      html = '<p>'+weather.temp+'&deg;'+weather.units.temp+'</p>';
  
      $("#weather").html(html);
    },
    error: function(error) {
      $("#weather").html('<p>'+error+'</p>');
    }
  });
    
  $(".input-charity").hide();
  $(".input-direct").hide();
    
  $( "#btn-rc" ).click(function() {
    $( this ).css("box-shadow", "0 0 10px rgba(22, 77, 221, 1)");
      $(".input-direct").hide();
      $(".input-charity").show();
  });
    
    $( "#btn-direct" ).click(function() {
    $( this ).css("box-shadow", "0 0 10px rgba(22, 77, 221, 1)");
        $(".input-charity").hide();
      $(".input-direct").show();
  });
    
    
});


