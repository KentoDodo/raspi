import View from '/static/js/widgets/view.js';


export default class ClockView extends View {
    constructor(jq) {
        super(jq, 1000, "/static/js/widgets/clock.html");
    }

    update() {
        var now_strings = this.getNowStrings();

        $("#year").html(now_strings.year);
        $("#month").html(now_strings.month);
        $("#day").html(now_strings.day);
        $("#week").html(now_strings.week);
        $("#hour").html(now_strings.hour);
        $("#minute").html(now_strings.minute);
        $("#second").html(now_strings.second);
    }

    getNowStrings() {
        var weeks = ["Sun", "Mon", "Thu", "Wed", "Thr", "Fri", "Sat"];
        var now = new Date();

        var now_strings = {};
        now_strings.year = now.getFullYear();
        now_strings.month = now.getMonth() + 1;
        now_strings.day = now.getDate();
        now_strings.week = weeks[now.getDay()];
        now_strings.hour = now.getHours();
        now_strings.minute = now.getMinutes();
        now_strings.second = now.getSeconds();

        if (now_strings.month < 10) now_strings.month = "0" + now_strings.month;
        if (now_strings.day < 10) now_strings.day = "0" + now_strings.day;
        if (now_strings.hour < 10) now_strings.hour = "0" + now_strings.hour;
        if (now_strings.minute < 10) now_strings.minute = "0" + now_strings.minute;
        if (now_strings.second < 10) now_strings.second = "0" + now_strings.second;

        return now_strings;
    }
}
