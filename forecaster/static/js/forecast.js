$(function() {
  Array.prototype.toObj = function(values){
    var some;
    values = values || this.map(function(v){
      return true;
    });

    this .map(function(v) {
      return [v, this.shift()];
    }, values)
    .map(function(v) {
      this[v[0]] = v[1];
    }, some = {});
    return some;
  };

  function zip() {
    var reverseTemps = {};
    var tempIn = [];
    var tempOut = [];
    for (var i = -15; i < 116; i++) {
      tempIn.push(i);
    }
    for (var j = 115; j > -16; j--) {
      tempOut.push(j);
    }
    reverseTemps = tempIn.toObj(tempOut);
    return reverseTemps
  };

  $('.container div').each(function() {
    var zipTemps = zip();
    var $temp = Math.round($(this).data("temp"));
    $(this).css('background-color', function() {
      return 'hsla(' + zipTemps[$temp] * 2.5 + ', 70%, 50%, 1)';
    });
  });
})
