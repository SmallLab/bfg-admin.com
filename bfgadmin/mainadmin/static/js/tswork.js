$(document).ready( function(){
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
                    var new_type = '<tr><td></td><td class="text-center">'+new_name+'</td><td class="text-center"><button type="button"'+
                                    'class="btn btn-sm btn-danger" data_info = "'+data.id+'">False</button></td><td class="text-center">'+
                                    ''+new_link+'</td><td class="text-center"><a type="button" data_delete="delete" id="'+data.id+'"'+
                                    'class="btn btn-sm btn-danger" href="/typesent/deleteset/'+data.id+'/">Delete</a></td>';
                    $('#type_s_list').append(new_type);
              }
            }

  });
/*
* Changes 'is_active' field for type sentense data
* */
  $('td').on('click', 'button', function (e) {
      console.log('3000$');
      e.preventDefault();
      return false;
      if($(this).attr('data_info')){
          var that = $(this)
          $.get(
              "/typesent/ajaxts/isactive/"+$(this).attr("data_info")+"/",
              onAjaxIsActive
            );
            function onAjaxIsActive(data)
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
* Delete type sentense data
* */
    $('[data_delete=delete]').click(function () {
        $('#is_deleted_ts').modal();
        $('#delete_type').attr('data_id_type', $(this).attr('href'));
        return false;
    });

    $('#cancel_type').click(function () {
        $('#is_deleted_ts').modal('hide');
        $('#delete_type').attr('data_id_type', '');
        return false;
    });


    $('#delete_type').click(function () {
        $('#is_deleted_ts').modal('hide');
        var url = $(this).attr('data_id_type');
        $(location).attr('href',url);
    });
});
