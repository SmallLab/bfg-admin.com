$(document).ready( function(){
/*
* Add new CTR data
* */
  $('#add_new_ctr').click(function () {

          var new_name = $('#new_name_ctr').val();
          var new_link = $('#new_link_ctr').val();
          if(new_name == '' || new_link == '' ){
              alert('Enter correct data for new type!!!');
              return false;
          }
          $.get(
              "/ctr/ajaxctr/addnew/",
              {
                  name: new_name,
                  link: new_link,
                  key_ctr: $('#key_ctr').val()
              },
              onAjaxSuccess
            );
            function onAjaxSuccess(data)
            {
              if (data.status){
                    var new_type = '<tr><td></td><td class="text-center">'+new_name+'</td><td class="text-center"><button type="button"'+
                                    'class="btn btn-sm btn-danger" data_info = "'+data.id+'">False</button></td><td class="text-center">'+
                                    ''+new_link+'</td><td class="text-center"><a type="button" data_delete="delete" id="'+data.id+'"'+
                                    'class="btn btn-sm btn-danger" href="/ctr/deletectr/'+data.id+'/">Delete</a></td>';
                    $('#ctr_list').append(new_type);
              }
            }

  });
/*
* Changes 'is_active' field for CTR
* */
  $("tbody").on("click", "button", function () {
    if($(this).attr('data_info')){
          var that = $(this)
          $.get(
              "/ctr/ajaxctr/isactive/"+$(this).attr("data_info")+"/",
              {
                 key_ctr: $('#key_ctr').val()
              },
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
* Delete CTR data
* */
    $("tbody").on("click", "a", function () {
        if($(this).attr('data_delete')){
            $('#is_deleted_ctr').modal();
            $('#delete_type').attr('data_id_type', $(this).attr('href'));
            return false;
         }
         return false;
    });

    $('#cancel_type').click(function () {
        $('#is_deleted_ctr').modal('hide');
        $('#delete_type').attr('data_id_type', '');
        return false;
    });


    $('#delete_type').click(function () {
        $('#is_deleted_ctr').modal('hide');
        var url = $(this).attr('data_id_type')+'?key_ctr='+$('#key_ctr').val();
        $(location).attr('href',url);
    });
});
