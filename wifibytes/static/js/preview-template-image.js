/* Anadir image en admin para previsualizar una imagen en templates */

function addPreviewImageToTemplate(){
  if(window.location.hash) {
      var hash = window.location.hash.substring(1);
      var style_img_preview = {
        width: '35%',
        margin: '10px',
        float: 'right',
      };
      var id_template = hash.substr(hash.length - 1);
      if(hash == 'template'+id_template && $( "#preview-template"+id_template ).length <=0){
        $( "#id_template"+id_template+"_articulo-0-pretitulo" ).parent().parent().parent().before('<img id="preview-template'+id_template+'" src="/static/img/templates-preview/template'+id_template+'-preview.png">');
        $( "#preview-template"+id_template ).css(style_img_preview);
      }
  }
}

$(document).ready(function() {
  addPreviewImageToTemplate();
});

$(window).on('hashchange', function(e){
  addPreviewImageToTemplate();
});
