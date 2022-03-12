$(document).ready(function () {
  $("form").submit(function (event) {
    var formData = {
      question: $("#question").val()
    };


    $('#answer_box').addClass('animated-gradient');
    $.ajax({
      type: "POST",
      url: "/question",
      data: formData,
      dataType: "json",
      encode: true,
    }).done(function (data) {
      console.log(data);
      //$('form').reset();
      $("#form").trigger('reset');
      $("#answer_box").text(data);
      $('#answer_box').removeClass('animated-gradient');
    });

    event.preventDefault();
  });
});

