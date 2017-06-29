// Rose Meyers for 802Secure

'use strict'

// Some Jquery for duck clicking and subscriber form submit success
$("#containerDuck").addClass('hide');
$("#containerDuck").slideUp(100);
$(".duck").click(function(e) {
  e.preventDefault();
// Toggle the containers
  $("#containerDuck").toggle(100);
  $("#containerMain").toggle(1);

  // Just in case toggle doesn't work
  $("#containerDuck").removeClass('hide');
  $("#containerMain").addClass('hide');
});

// AJAX POST to Send email from form to server to be mailed.
$('form').submit(function(e) {
  e.preventDefault();
  var emailval = $('input#email').val();
  console.log(emailval);
  if (emailval !== "") {
    $.ajax({
      cache: false, // no cache
      url: '/index.html', // url
      type: 'POST', // request method
      dataType: 'json', // json data type
      data: {
        email: emailval // Here's the object with email value
      },
      success: data => {
        console.log('success', data);
        $("#containerDuck").removeClass('hide');
        $("#containerDuck").show(100);
        $("#containerMain").hide(1);
        $(".duck").append("<h1>You subscribed!</h1>");
      },
      error: e => console.log('errors', JSON.stringify(e)),
      fail: () => console.log('fail')
    });
  } else {
    alert("Insert email!");
  }
});
