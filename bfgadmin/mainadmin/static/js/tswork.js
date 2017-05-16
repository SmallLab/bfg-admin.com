$(document).ready( function(){
/*
* Changes 'is_active' field for type sentense data
* */
  $('button[type=button]').click(function () {
      if($(this).attr('data_info')){
          var that = $(this)
          $.get(
              "/typesent/ajaxts/isactive/"+$(this).attr("data_info")+"/",
              onAjaxSuccess
            );
            function onAjaxSuccess(data)
            {
              if (data.status == true){
                  that.text("True").removeClass("btn-danger").addClass("btn-success")
              }
              else{
                  that.text("False").removeClass("btn-success").addClass("btn-danger")
              }
            }
      }
  });
  /*
* Add new type sentense data
* */
  $('#add_new_type').click(function () {

          var new_name = $('#new_name_type_s').val();
          var new_link = $('#new_link_type_s').val();
          if(new_name == '' || new_link == '' ){
              alert('Enter correct data for new type!!!');
              return false;
          }

          $.get(
              "/typesent/ajaxts/addnew/",
              {
                  name: new_name,
                  link: new_link,
              },
              onAjaxSuccess
            );
            function onAjaxSuccess(data)
            {
              if (data.status){

              }
            }

  });

/*
* Delete type sentense data
* */
    $('[data_delete=delete]').click(function () {
        $('#is_deleted_ts').modal();
        $('#delete_type').attr('data_id_type', $(this).attr('href'));
        return false;
    })
    $('#cancel_type').click(function () {
        $('#is_deleted_ts').modal('hide');
        $('#delete_type').attr('data_id_type', '');
        return false;
    })

    $('#delete_type').click(function () {
        $('#is_deleted_ts').modal('hide');
        var url = $(this).attr('data_id_type');
        $(location).attr('href',url);
    })
});
