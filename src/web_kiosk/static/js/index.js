import ClockView from '/static/js/widgets/clock.js';
import TemperatureView from '/static/js/widgets/temperature.js';
import JmaRadarView from '/static/js/widgets/jma_radar.js';
import TrainDepartureView from '/static/js/widgets/train_departure.js';
import TemperatureGraphView from '/static/js/widgets/temperature_graph.js';


$(function() {
    var clockView = new ClockView("#clockView");
    var temperatureView = new TemperatureView("#temperatureView", apiPorts);
    var trainDepartureView = new TrainDepartureView("#trainDepartureView", apiPorts);
    var jmaRadarView = new JmaRadarView("#jmaRadarView", apiPorts);
    var temperatureGrpahView = new TemperatureGraphView("#temperatureGraphView", apiPorts);
});
