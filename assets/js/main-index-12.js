(function ($) {

    /*================================
        YTplayer Video Active
    ================================*/
    $(".youtube-bg").YTPlayer({
        videoURL: "https://youtu.be/elOLEDKFbf0",
        containment: '.youtube-bg',
        mute: true,
        loop: true,
        showControls: false

    });

})(jQuery);
