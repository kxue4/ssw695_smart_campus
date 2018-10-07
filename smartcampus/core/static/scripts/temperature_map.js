// map center
var myLatlng = new google.maps.LatLng(40.742770, -74.026230);
// map options,
var myOptions = {
    zoom: 16,
    center: myLatlng
};
// standard map
map = new google.maps.Map(document.getElementById("map-canvas"), myOptions);
// heatmap layer
heatmap = new HeatmapOverlay(map, 
    {
    // radius should be small ONLY if scaleRadius is true (or small radius is intended)
    "radius": 25,
    "maxOpacity": 1, 
    // scales the radius based on map zoom
    "scaleRadius": false, 
    // if set to false the heatmap uses the global maximum for colorization
    // if activated: uses the data maximum within the current map boundaries 
    //   (there will always be a red spot with useLocalExtremas true)
    "useLocalExtrema": true,
    // which field name in your data represents the latitude - default "lat"
    latField: 'lat',
    // which field name in your data represents the longitude - default "lng"
    lngField: 'lng',
    // which field name in your data represents the data value - default "value"
    valueField: 'count'
    }
);

var testData = {
    max: 3,
    data: [{lat: 40.742770, lng:-74.026230, count: 3},{lat: 40.745459, lng:-74.022585, count: 5}]
};

heatmap.setData(testData);