    function emergency(){
        var data = new FormData();
        data.append("To", "13136551850");
        data.append("From", "13137278191");
        data.append("Body", "I am in immediate danger.  You are recieving this text because this contack=ct has listed you as an emergency contact. If you believe this to be life threating please call the police. ");

        var xhr = new XMLHttpRequest();
        xhr.withCredentials = true;

        xhr.addEventListener("readystatechange", function () {
            console.log(this.readyState);
  if (this.readyState === 4) {
    console.log(this.responseText);
  }
            
});

xhr.open("POST", "https://api.twilio.com/2010-04-01/Accounts/AC8e1de6b5082dd869e0a6f3399d267527/Messages.json");
xhr.setRequestHeader("authorization", "Basic QUM4ZTFkZTZiNTA4MmRkODY5ZTBhNmYzMzk5ZDI2NzUyNzo0NjhmZWQ1ZmFiYTNkY2I1MmI2MzcyZDUwYjQxNDA5NQ==");
xhr.setRequestHeader("cache-control", "no-cache");
xhr.setRequestHeader("postman-token", "b11fe187-c85a-9004-3b56-ea318e385d07");

xhr.send(data);
console.log(xhr.status);
        
        
    }




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
   
    // Panic Button
    

    
    
    
 /*   document.getElementById("id_Author").placeholder = "Author"; 
    document.getElementById("id_Title").placeholder = "Title";
    document.getElementById("id_Text").placeholder = "Update my status...";  
   
*/   
});


