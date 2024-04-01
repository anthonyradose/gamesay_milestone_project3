document.addEventListener('DOMContentLoaded', function() {
    let flashes = document.querySelectorAll('.flashes');

    flashes.forEach(function(flash) {
        setTimeout(function() {
            flash.style.display = 'none';
        }, 3000);
    });
});
