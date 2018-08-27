import View from '/static/js/widgets/view.js';


export default class TrainDepartureView extends View {
    constructor(jq, apiPorts) {
        super(jq, 1000, "/static/js/widgets/train_departure.html", {"apiPorts": apiPorts});
    }

    init() {  
        this.trainDepartures;
        this.trainDeparturesData;
        this.trainDepartureIndex = 0;
    }

    create() {
        var t = this;
        setInterval(function(){t.getTrainDeparturesData()}, 60 * 1000);
        setInterval(function(){t.increaseTrainDepartureIndex()}, 10 * 1000);
    }

    update() {
        if (!this.trainDeparturesData) {
            $.ajaxSetup({ async: false });
            this.trainDeparturesData = this.getTrainDeparturesData();
            $.ajaxSetup({ async: true });
        }
        this.setTrainDeparturesData();
    }

    setTrainDeparturesData() {
        var index = this.trainDepartureIndex % this.trainDepartures.length;
        var _trainDeparture = this.trainDepartures[index];
        var _trainDepartureData = this.trainDeparturesData[index];

        $("#trainLine").html(_trainDeparture.line);
        $("#trainDirection").html(_trainDeparture.direction);

        var now = new Date();
        var hour = now.getHours();
        if (hour < 4) hour += 24;
        var minute = now.getMinutes();
        var next_train_index = 0;
        for (var i in _trainDepartureData) {
            var train = _trainDepartureData[i];
            if ((train.hour == hour && train.minute > minute) || train.hour > hour) {
                next_train_index = parseInt(i);
                break;
            }
        }

        $("#train_departure").html("");
        for (var i = 0; i < 3; i++) {
            var index = next_train_index + i;
            if (index >= _trainDepartureData.length) break;
            var next_train = _trainDepartureData[index];
            var _hour = next_train.hour;
            var _minute = next_train.minute;
            if (_hour < 10) _hour = "0" + _hour;
            if (_minute < 10) _minute = "0" + _minute;
            $("#train_departure").append("<tr><td>" + _hour + ":" + _minute + "</td><td>" + next_train.go_to + "</td></tr>");
        }
    }

    getTrainDeparturesData() {
        if (!this.trainDepartures) {
            var t = this;
            $.getJSON("http://raspberrypi.local:" + this.apiPorts.train + "/api/departure", null, function(data, status) {
                t.trainDepartures = data;
            });
        }

        var _trainDeparturesData = [];
        for (var i in this.trainDepartures) {
            $.getJSON("http://raspberrypi.local:" + this.apiPorts.train + "/api/departure/" + this.trainDepartures[i]._id, null, function(data, status) {
                _trainDeparturesData.push(data);
            });
        }
        
        return _trainDeparturesData;
    }

    increaseTrainDepartureIndex() {
        this.trainDepartureIndex += 1;
    }
}
