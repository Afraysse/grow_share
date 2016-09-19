var map;

var newMarkersArray = [];
var allMarkersArray =[];

var lat;
var lng;


function initMap() {
        var map = new google.maps.Map(document.getElementById('map'), {
          // center: {lat: -34.397, lng: 150.644},
          zoom: 15
        });

        var currentLocIcon = {
          path: fontawesome.markers.MAP_MARKER,
          strokeColor: '#339933',
          strokeOpacity: 1,
          strokeWeight: 3,
          fillColor: '#339933',
          fillOpacity: 0.8,
          scale: 1.4
        }

        var addTagIcon = {url: '/static/img/mark_1.JPG'}

        // var infoWindow = new google.maps.InfoWindow({map: map});

        // HTML 5 GEOLOCATION 
        if (navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(function(position) {
            var pos = {
              lat: position.coords.latitude,
              lng: position.coords.longitude
            };

            // infoWindow.setPosition(pos);
            // infoWindow.setContent('Location found.');
            map.setCenter(pos);

            // write createMarker function later on!!!!
            var geolocationMarker = createMarker(pos, currentLocIcon);


            // setIcon() is called on the marker to customize marker --> per GMAPI
            google.maps.event.addListener(geolocationMarker, 'click', function(event){
              clearClickMarker();
              geolocationMarker.setIcon(addTagIcon);
            })

            google.maps.event.addListener(map, 'click', function(event){
              geolocationMarker.setIcon(currentLocIcon);
            })
          }, function() {
            handleNoGeolocation(true);

        });




