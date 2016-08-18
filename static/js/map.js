
/* FUNCTIONS FOR MAP ON DASHBOARD.HTML */

 function initMap() {

  var styledMapType = new google.maps.StyledMapType(
    [
      { 
        stylers: [
          { hue: '#00ffe6'},
          { saturation: -20 }
        ]
      }, {
        featureType: 'road',
        elementType: 'geometry',
        stylers: [
          { lightness: 100},
          { visibility: 'simplified'}
        ]
      }, {
        featureType: 'road',
        elementType: 'labels',
        stylers: [
          {visibility: 'off'}
        ]
      }
    ],
    {name: 'Styled Map'});

  var map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: -34.397, lng: 150.644},
    scrollwheel: true,
    zoom: 14,
    zoomControl: true,
    panControl: false,
    mapTypeControlOptions: {
      mapTypeIds: ['roadmap', 'satellite', 'hybrid', 'terrain',
                    'styled_map']
    }

  });


  // ASSOCIATE STYLED MAP TO MAP ID

  map.mapTypes.set('styled_map', styledMapType);
  map.setMapTypeId('styled_map');

  // SET GEOLOCATION FOR USER
  var infoWindow = new google.maps.InfoWindow({map: map});

  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var pos = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };

      infoWindow.setPosition(pos);
      infoWindow.setContent('found you!');
      map.setCenter(pos);
    }, function() {
      handleLocationError(true, infoWindow, map.getCenter());
    });
  } else {

    // BROWSER DOESN'T SUPPORT GEOLOCATION
    handleLocationError(false, infoWindow, map.getCenter());
  }
}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
  infoWindow.setPosition(pos);
  infoWindow.setContent(browserHasGeolocation ?
                        'Error: The Geolocation service failed.' :
                        'Error: Your browser doesn\'t support geolocation.');
}








