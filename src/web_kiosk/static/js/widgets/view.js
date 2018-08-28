export default class View {
    constructor(jq, updateInterval, htmlPath, params) {
        var t = this;
        setTimeout(function(){t._constructor(jq, updateInterval, htmlPath, params)}, 0);
    }

    _constructor(jq, updateInterval, htmlPath, params) {
        this._setParams(params);
        this.init();
        this._loadHtml(jq, htmlPath);
        this.create();
        this.update();
        this.updateInterval = updateInterval;
    }

    get updateInterval() {
        return this._updateInterval;
    }

    set updateInterval(value) {
        if (this.interval) window.clearInterval(this.interval);
        var t = this;
        this.interval = setInterval(function(){t.update()}, value);
        this._updateInterval = value;
    }

    _setParams(params) {
        for (let key in params) {
            this[key] = params[key];
        }
    }

    _loadHtml(jq, htmlPath) {
        if (!htmlPath) return;
        $.ajax({ type: "GET",   
            url: htmlPath,   
            async: false,
            success : function(text){
                $(jq).append(text);
            }
        });
    }

    init() {
    }

    create() {
    }

    update() {
    }
}
