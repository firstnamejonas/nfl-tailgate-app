/*
    Eventlistener to the refresh button to reload the page when clicked.
*/
document.getElementById("refresh-button").addEventListener("click", function() {
    location.reload();
});


/*
    Navigates the user back to the previous page in the browser history.
*/
function goBack() {
    window.history.back();
}