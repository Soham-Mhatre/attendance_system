document.addEventListener("DOMContentLoaded", function() {
    var startScanButton = document.getElementById("startScanButton");
    startScanButton.addEventListener("click", function() {
        // Execute the start_scan logic only when the "Start Scan" button is clicked
        startScan();
    });
});

function startScan() {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/start_scan/", true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                console.log("Scan started successfully.");
            } else {
                console.error("Error starting scan:", xhr.status + ": " + xhr.responseText);
            }
        }
    };
    xhr.send();
}

