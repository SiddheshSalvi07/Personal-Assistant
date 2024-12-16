$(document).ready(function () {
    

    $('.text').textillate({
        loop:true,
        sync:true,
        in:{
            effect:"bounceIn",
        },
        out:{
            effect:"bounceOut",
        }
    });

    //siri configuration using its github
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: 'ios9',
        amplitude: '1',
        speed: '0.20',
        autostart: true,
      });


      // Siri wave Message
      $('.siri-message').textillate({
        loop:true,
        sync:true,
        in:{
            effect:"fadeInUp",
            sync: true,
        },
        out:{
            effect:"fadeOutUp",
            sync: true,
        }
    });

    //mic button click event
    $("#MicBtn").click(function () {
        eel.playAssistantSound() 
        $("#oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.AllCommands()()
        
    });

    function doc_keyUp(e) {
        if (e.key === 's' && e.altKey) {  
            console.log("Alt+S detected!");
            eel.playAssistantSound() 
            $("#oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.AllCommands()()
        }
    }
    document.addEventListener('keyup', doc_keyUp, false);
    
});