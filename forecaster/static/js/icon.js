// TODO: Revise icons based on time of day - AM vs. PM

$(function() {
  $('span[data-summary="Drizzle"]').addClass('climacon drizzle');
  $('span[data-summary*="Rain"]').addClass('climacon rain');
  $('span[data-summary*="Cloud"]').addClass('climacon cloud');
  $('span[data-summary*="Snow"]').addClass('climacon snow');
  $('span[data-summary*="Overcast"]').addClass('climacon cloud');
  $('span[data-summary*="Clear"]').addClass('climacon sun');

})
