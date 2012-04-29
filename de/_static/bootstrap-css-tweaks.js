jQuery(function($) {
  $('table.docutils').addClass('table table-striped table-bordered');
  $('table.docutils').removeClass('docutils');

  $('.admonition').addClass('alert alert-block');
  $('.admonition.note').addClass('alert-info');
  $('.admonition.warning').addClass('alert-error');
});
