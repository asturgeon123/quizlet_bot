$(document).ready(function () {

  $("#link_box").hide();
  $("#question_box").hide();



  $("form").submit(function (event) {

    request_search()


    event.preventDefault();
  });

});

function request_search() {

      var formData = {
      question: $("#question").val()
    };


    $('#main_box').addClass('animated-gradient');
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

      $("#answer_box").text(data['final_answer']);
      $('#main_box').removeClass('animated-gradient');

      //$("#link_box").text("Link: "+data["answer_link"]);
      $("#link_box").attr("href", data["answer_link"])

      $("#question_box").text("Question: "+data["final_question"]);

      $("#question_box").show();
      $("#link_box").show();

    });
}