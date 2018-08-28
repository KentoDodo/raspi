import View from '/static/js/widgets/view.js';


export default class TemperatureGraphView extends View {
    constructor(jq, apiPorts) {
        super(jq, 10 * 1000, "/static/js/widgets/temperature_graph.html", {"apiPorts": apiPorts});
    }

    init() {
        this.temperature_min, this.temperature_max = 25;
    }

    create() {
        var canvas = $("<canvas></canvas>");
        $('#temperatureGraphChart').append(canvas);
        var t = this;
        var ctx = canvas[0].getContext('2d');
        var chart = new Chart(ctx, {
            type: 'line',
            data: {
                datasets: [
                    {
                        data: [],
                        label: 'Temperature_min',
                        fill: false,
                        backgroundColor: '#9999FF',
                        borderColor: '#9999FF',
                        borderWidth: 5,
                        pointRadius: 0
                    },
                    {
                        data: [],
                        label: 'Temperature_max',
                        fill: false,
                        backgroundColor: '#FF9999',
                        borderColor: '#FF9999',
                        borderWidth: 5,
                        pointRadius: 0
                    }
                ]
            },
            options: {
                legend: {
                    display: false,
                },
                title: {
                    display: true,
                    text: 'Temperature',
                    fontSize: 24
                },
                scales: {
                    xAxes: [
                        {
                            type: 'realtime',
                            gridLines: {
                                lineWidth: 2
                            },
                            ticks: {
                                fontSize: 18
                            },
                        }
                    ],
                    yAxes: [
                        {
                            gridLines: {
                                lineWidth: 2
                            },
                            ticks: {
                                beginAtZero: true,
                                min: 20,
                                max: 32,
                                fontSize: 18
                            }
                        }
                    ]
                },
                plugins: {
                    streaming: {
                        duration: 30 * 60 * 1000,
                        refresh: 10 * 1000,
                        delay: 3 * 1000,
                        frameRate: 30,
                        pause: false,

                        onRefresh: function(chart) {
                            chart.data.datasets[0].data.push({
                                x: Date.now(),
                                y: t.temperature_min
                            });
                            chart.data.datasets[1].data.push({
                                x: Date.now(),
                                y: t.temperature_max
                            });
                        }
                    }
                }
            }
        });
    }

    update() {
        var t = this;
        $.getJSON("http://" + window.location.hostname + ":" + this.apiPorts.temperature + "/api/temperature", null, function(data, status) {
            t.setTemperatureData(data);
        });
    }

    setTemperatureData(temperatureData) {
        if (temperatureData && temperatureData.temperature && temperatureData.temperature2) {
            this.temperature_min = Math.min(temperatureData.temperature, temperatureData.temperature2);
            this.temperature_max = Math.max(temperatureData.temperature, temperatureData.temperature2);
        }
    }
}
