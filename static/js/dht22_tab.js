$(function() {
    function fetchArduinoData() {
        $.get("/plugin/dht22_tab/arduino_data", function(data) {
            $("#dht22_tab iframe").contents().find('body').html(data);
            $("#dht22_topbar").html(data);
        });
    }

    fetchArduinoData();
    setInterval(fetchArduinoData, 10000);  // Refresh every 10 seconds
});
