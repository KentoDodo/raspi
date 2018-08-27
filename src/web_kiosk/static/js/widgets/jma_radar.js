import View from '/static/js/widgets/view.js';


export default class JmaRadarView extends View {
    constructor(jq, apiPorts) {
        super(jq, 6 * 1000, "/static/js/widgets/jma_radar.html", {"apiPorts": apiPorts});
    }

    update() {
        var t = this;
        $.getJSON("http://raspberrypi.local:" + this.apiPorts.weather + "/api/jma_radar", null, function(data, status) {
            t.setJmaRararData(data);
        });
    }

    setJmaRararData(jmaRararData) {
        $(".jma-radar").each(function(index, element) {
            $(element).attr('src', jmaRararData["image_url"]);
        });
    }
}
