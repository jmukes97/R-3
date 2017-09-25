function donate(){
    var cash = document.getElementById("money");
    var url = "https://www.redcross.org/donate/disaster-relief?donmt=" + cash;
    window.location.replace(url);
}