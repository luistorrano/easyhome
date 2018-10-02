var map;
 
function initialize() {
    var latlng = new google.maps.LatLng(-18.8800397, -47.05878999999999);
    var options = {
        zoom: 5,
        center: latlng,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    google.maps.event.addDomListener(window, "resize", function() {
        var center = map.getCenter();
        google.maps.event.trigger(map, "resize");
        map.setCenter(center); 
    });
    
    var input = document.getElementById('id_endereco');
    map = new google.maps.Map(document.getElementById("mapa"), options);
    var autocomplete = new google.maps.places.Autocomplete(input);
    autocomplete.bindTo('bounds', map);
    google.maps.event.addListener(autocomplete, 'place_changed', function() {


    
        // chama outra função para setar os valores os inputs
        fillGeolocFields(autocomplete.getPlace().geometry.location);
    }); 

    

}

google.maps.event.addDomListener(window,'load',initialize)

function fillGeolocFields(location) {
    $('#id_latitude').val(location.lat());
    $('#id_longitude').val(location.lng());
}

