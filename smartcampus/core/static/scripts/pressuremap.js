// map center
var myLatlng = new google.maps.LatLng(40.742770, -74.026230);
// map options,
var myOptions = {
    zoom: 16,
    center: myLatlng
};
// standard map
map = new google.maps.Map(document.getElementById("pressure_map"), myOptions);
// heatmap layer
heatmap = new HeatmapOverlay(map, 
    {
    // radius should be small ONLY if scaleRadius is true (or small radius is intended)
    "radius": 30,
    "maxOpacity": 1, 
    // scales the radius based on map zoom
    "scaleRadius": false, 
    // if set to false the heatmap uses the global maximum for colorization
    // if activated: uses the data maximum within the current map boundaries 
    //   (there will always be a red spot with useLocalExtremas true)
    "useLocalExtrema": false,
    // which field name in your data represents the latitude - default "lat"
    latField: 'lat',
    // which field name in your data represents the longitude - default "lng"
    lngField: 'lng',
    // which field name in your data represents the data value - default "value"
    valueField: 'value'
    }
);

var presValue = parseInt(document.getElementById("pres_value").innerHTML);
var testData = {
    max: 1200,
    data: [{lat: 40.743427, lng:-74.0272672, value: presValue}]
};

heatmap.setData(testData);