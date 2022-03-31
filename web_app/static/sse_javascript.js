 //Client-side Javascript code for handling clipboard queries
$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    var numbers_received = [];

    //receive details from server

    socket.on('newquery', function(msg) {
        console.log("Received Query" + msg.query);
        $("#question").val(msg.query)
        request_search()
});
});