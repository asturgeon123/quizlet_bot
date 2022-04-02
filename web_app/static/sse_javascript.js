 //Client-side Javascript code for handling clipboard queries
$(document).ready(function(){

    //Server Side - Without using socketIO
    var last_data;
    var intervalId = window.setInterval(function(){
      $.ajax({
        url: '/clipboard',
        type: "GET",
        dataType: "json",
        success: function (data) {

            if (data.data !== last_data) {
                console.log("Received new query" + data.data);
                $("#question").val(data.data)
                last_data = data.data
                request_search()
                
            }

        },
        error: function (error) {
            console.log(`Error ${error}`);
        }
        });
    }, 800);
});






