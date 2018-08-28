import View from '/static/js/widgets/view.js';


export default class TemperatureView extends View {
    constructor(jq, apiPorts) {
        super(jq, 5 * 1000, "/static/js/widgets/temperature.html", {"apiPorts": apiPorts});
    }

    update() {
        var t = this;
        $.getJSON("http://" + window.location.hostname + ":" + this.apiPorts.temperature + "/api/temperature", null, function(data, status) {
            t.setTemperatureData(data);
        });
    }

    setTemperatureData(temperatureData) {
        if (temperatureData && temperatureData.temperature && temperatureData.temperature2) {
            var avg = (temperatureData.temperature + temperatureData.temperature2) / 2;
            var min = Math.min(temperatureData.temperature, temperatureData.temperature2);
            var max = Math.max(temperatureData.temperature, temperatureData.temperature2);
            $("#temperature_avg").html(avg.toFixed(1));
            $("#temperature_min").html(min.toFixed(1));
            $("#temperature_max").html(max.toFixed(1));
        }
        if (temperatureData.humidity) $("#humidity").html(temperatureData.humidity.toFixed(0));
    }
}
