$(document).ready(function () {

    // Display Speak message
    eel.expose(DisplayMessage)
    function DisplayMessage(message) {

        $(".siri-message li:first").text(message);
        $(".siri-message").textillate("start");
    }

    //Display Main Ui
    eel.expose(ShowUi)
    function ShowUi(){
        $( "#oval").attr("hidden",false);
        $("#SiriWave").attr("hidden", false);
    }
});