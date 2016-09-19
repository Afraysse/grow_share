//// v|v|v|v|v|v|v|v|v HELPER FUNCTIONS FOR MAP COMPONENTS v|v|v|v|v|v|v|v|v|v|

/** if geolocation fails, set default map to center and raise error flag. */
function handleNoGeolocation(errorFlag) {
    var content; 

    if (errorFlag) {
        content = "Error: Geolacation service failed.";
    } else {
        content = "Error: Your browser does not support geolocation.";
    }

    var options = {
        map: map,
        position: new google.maps.LatLng(37.7749, -122.4194),
        content: content
    };

    var infowindow = new google.maps.InfoWindow(options);
    map.setCenter(options.position);
}

/** Markers are cleared from previous query. */ 
function clearMarkers() {
    for (var i = 0; i <allMarkersArray.length; i++ ) {
        allMarkersArray[i].setMap(null);
    }
    allMarkersArray.length = 0;
}

/** Toggles on-off for new tag food markers */ 
function clearClickMarker() {
    for (var i = 0; i < newMarkersArray.length; i++ ) {
        newMarkersArray[newMarkersArray.length - 1].setMap(null);
    }
    newMarkersArray.length = 0;
}