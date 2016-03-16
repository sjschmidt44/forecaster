$(function() {
  var currentTime = new Date().toString("hh:00 tt");
  $('div[data-time="' + currentTime + '"]').prevAll().remove();
})
