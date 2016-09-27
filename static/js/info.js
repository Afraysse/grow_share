// v|v|v|v|v|v|v| HELPER FUNCTIONS FOR GENERATING & DISPLAYING TAGS v|v|v|v|v|v|v|

/** Display all markers and information for queried foods. */

function displayTags(queriedFoods) {
    var infoDiv = ''
    assignMarkers(queriedFoods);
}

/** Creates a marker for each food tag returned in query and binds related food info. */
function assignMarkers(tags){
    //empty div for new tags 
    $('#tag-div-item').html('');

    // var counter = 0; set up count of tags so it knows when to shift to the next tag div. */ 
    var counterA = 0
    var counterB = 0

    var tag, marker; 

    for (key in tags) {

        counterA++;
        counterB++;

        // because there's only space for one div, if counterA exceeds 1, reset to 1. */
        if (counterA > 1) {
            counterA = 1;
        }

        tag = tags[key]

        pos = new google.maps.LatLng(tag.latitude, lag.longitude)
        marker = createMarker(pos,
                                {path: fontawesome.markers.MAP_PIN,
                                scale: 0.5,
                                strokeColor: 'black',
                                strokeOpacity: 0.5,
                                fillColor: 'black',
                                fillOpacity: 0.5
                            },
                                tag.title)

        allMarkersArray.push(marker) //add to array in order to be emptied in the subsequent query
    }
}

