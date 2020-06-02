(function() {

    "use strict";

    var dropZone = document.getElementById("drop-zone");


    dropZone.ondragover = function(){
        this.className = 'drag-area-on-drop rounded-lg';
        return false;
    };

    dropZone.ondragleave = function(){
        this.className = 'drag-area rounded-lg';
        return false;
    };

}());

