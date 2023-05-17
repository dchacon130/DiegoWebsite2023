$(document).ready(function () {
    var progressBar = $('#progress-bar');
    var width = 0;

    setInterval(function () {
        if (width >= 100) {
            width = 0;
        } else {
            width += 10;
        }

        progressBar.css('width', width + '%');
    }, 500);
});
