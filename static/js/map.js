
function initMap() {
        var map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: -34.397, lng: 150.644},
          zoom: 11
        });

        var infoWindow = new google.maps.InfoWindow({
          maxWidth: 250
        });

        // Try HTML5 geolocation.
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
          // Browser doesn't support Geolocation
          handleLocationError(false, infoWindow, map.getCenter());
        }
    }

      function handleLocationError(browserHasGeolocation, infoWindow, pos) {
        infoWindow.setPosition(pos);
        infoWindow.setContent(browserHasGeolocation ?
                              'Error: The Geolocation service failed.' :
                              'Error: Your browser doesn\'t support geolocation.');
      }

      // v|v|v|v|v|v|v|v|v|v| NEARBY POINTS ON LOAD v|v|v|v|v|v|v|v|v|v|v|v|v|v|

      // var iconImage = '/static/img/map_marker.png';

      // $.get(tags_json, function (tags) {
      //   // For every tag_food entry in db, specify details and place markers.
      //   for (var key in tags) {
      //     var tag = tags[key];

      //     var foodTagDetails = '<div class="media">' + 
      //     '<div class="media-left">' +
      //     '<img class="media-object" src="' + tag.imgage + '" alt="Image for' + tag.title + '">' +
      //     '</div>' + 
      //     '<div class="media-body">' + 
      //     '<h5 class="media-heading">' + tag.title + '</h5>' +
      //     '</div>' + 
      //     '</div>';

      //     // Specify marker coordinates with the restaurant's coordinates
      //     var markerLatLng = {lat: pos.lat, lng: pos.lng};

      //     var marker = new google.maps.Marker({
      //       position: markerLatLng,
      //       map: map,
      //       title: 'Sale: ' + tag.title,,
      //       html: foodTagDetails,
      //       icon: iconImage

      //     });

      //   } 

      // });









