
//  Select revelant sub category in select tag
$(document).ready(function(){
  $("#id_product_main_category_id").change(function () {
     var url ="/admin/DigitalPrintingPress/product/my_ajax/"
  

 
    var main_cat_Id = $(this).val();  
    $('#id_product_sub_category_id').html('');
     $.ajax({   
      type:'GET',                  
      url: url,              
       data: {
        'mainCategoryID':main_cat_Id 
      },
      success: function (data) { 
        console.log(data)
        var dataHandler = $("#id_product_sub_category_id");
        dataHandler.append('<option value="">--------</option>');
        for(var key  in data) {
          var value = data[key];
          for(var k  in value) {
            var val = value[k];
            var newRow = $('<option value="'+k+'">');
            newRow.html(' '+val+'');
            dataHandler.append(newRow);
             
          }
         
        }

      }
     });

  });
});
