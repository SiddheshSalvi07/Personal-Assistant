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

   function PlayAssistant(message){

        if (message != ""){

            $("#oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.AllCommands(message);
            $("#chatbox").val("")
            $("#MicBtn").attr("hidden", false);
            $("#SendBtn").attr("hidden", true);
        }
   }
    
   function showHideButton(message){
        if(message.length == 0){
            $("#MicBtn").attr('hidden', false);
            $("#SendBtn").attr('hidden', true);
        }
        else {
            $("#MicBtn").attr('hidden', true);
            $("#SendBtn").attr('hidden', false);

        }

   }
   $("#chatbox").keyup(function () { 
        let message = $("#chatbox").val();
        showHideButton(message)
    
   });

   $("#SendBtn").click(function () {
        let message = $("#chatbox").val()
        PlayAssistant(message)
   });

   $("#chatbox").keypress(function (e) { 
        key = e.which;
        if (key == 13){
            let message = $("#chatbox").val()
            PlayAssistant(message)
        }
   });

   
});