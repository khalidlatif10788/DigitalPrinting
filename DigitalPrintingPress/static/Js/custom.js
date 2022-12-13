$(document).ready(function(){
  $(".service-menue").mouseenter(function(){
    $(".mega-menue-wrapper").toggleClass("mega-menue-wrapper-visible");
    // $("div").addClass("important");
  });
  $(".shop-menue").mouseenter(function(){
    $(".mega-menue-wrapper").toggleClass("mega-menue-wrapper-visible");
    // $("div").addClass("important");
  });
  // Selection slider
  var slider = document.getElementById("myRange");
  var output = document.getElementById("selection-area");
  output.style.width = slider.value;
  output.style.height = slider.value;

  slider.oninput = function() {
  output.style.width = this.value;
  output.style.height = this.value;
}
// end slider width-height
var slider = document.getElementById("top-possition");
  var output = document.getElementById("selection-area");
  output.style.top = slider.value;
  

  slider.oninput = function() {
  output.style.top = this.value;
  
}
//  end top
var slider = document.getElementById("lef-possition");
  var output = document.getElementById("selection-area");
  output.style.left = slider.value;
  

  slider.oninput = function() {
  output.style.left = this.value;
  
}
// end left
});

  // $(document).ready(function(){

$(document).ready(function(){
const swiper = new Swiper('.swiper', {
    // Optional parameters
    direction: 'horizontal',
    loop: true,
  
    // If we need pagination
    pagination: {
      el: '.swiper-pagination',
    },
    autoplay: {
      delay: 5000,
    },
    // Navigation arrows
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
  
    // And if we need scrollbar
    scrollbar: {
      el: '.swiper-scrollbar',
    },
  });
});
  $(document).ready(function(){
  // color btn
  var listpdes=[]
  var finalvalue="";
  var checksplit=[]
  var cheksub=[]
  var checktitle=""

  
  // Select size,color etc.
  var allclasses=[]
  $(".coloredbtn").click(function(){
    // add active/colored class to current selected btn
    var ptitle= $(this).parents(".coloredbtnwrapperbtn").siblings(".pTitle").text();
    var joinclass= ptitle+"-btn"
    var name=$("."+joinclass);
     if(allclasses.includes(ptitle))
     {
     var name=$(".coloredbtn").attr("class");
     var splitClassNam= name.split(" ")
     if ($("."+joinclass).hasClass("colorchangbtn"))
       {
        $("."+joinclass).removeClass("colorchangbtn")
        $(this).addClass("colorchangbtn")
       }
     }
     else{
      $(this).addClass("colorchangbtn")
      allclasses.push(ptitle)
    }
     // added current selected title and description into listdes array
      var pdes= $(this).text();
    var desTitle= ptitle+"-"+pdes
    var chekvar= desTitle.split("-")
   
      if (checksplit.includes(chekvar[0],0)!=true)
      {
        checksplit.push(chekvar[0])
        listpdes.push(desTitle)
      }
      else{
       for(i=0; i<listpdes.length; i++)
         var cklist = listpdes[i].split("-")
        cheksub.push(cklist[0])
        
      }
      if(cheksub.includes(chekvar[0],0)==true)
      {
        listpdes.pop(listpdes[i])
        listpdes.push(desTitle)
      }
     
  
  });

  //   // add to cart button
  
    $(".addtocartbtn").click(function(e){
      // data get for input
      e.preventDefault();
      
      var productId= document.getElementById("pid").value
      var product_id=parseInt(productId)
      //var customerId=2
      var productQtv= document.getElementById("qtybox").value
      var product_qty=parseInt(productQtv)
      var productTotalAmount= document.getElementById("totalAmount").innerText
      var productTextPrint= document.getElementById("textid").value
     
      // end data get for input
   
      for(i=0;i<listpdes.length;i++)
      {
        if (i==0)
        {
          finalvalue = listpdes[i]
        }
        else{
          finalvalue = finalvalue +"*"+ listpdes[i]
        }  
      }
      console.log(product_qty)
      if(finalvalue.length<4)
      {
        window.alert("Please select Size and Color of the Product")
      }
       else {
        if (isNaN(product_qty)) {
          window.alert("Please select Qty")
          
        }
        else{
      
     
      console.log(finalvalue.length)
    var dataForm = new FormData();
   // dataForm.append("productId",productId,"productDetail",finalvalue,"productQtv",productQtv,"productTotalAmount",productTotalAmount,"productTextPrint",productTextPrint);
  
   dataForm.append("productId",product_id);
   dataForm.append("productDetail",finalvalue);
   dataForm.append("productQtv",product_qty);
   dataForm.append("productTotalAmount",productTotalAmount);
   dataForm.append("productTextPrint",productTextPrint);

    dataForm.append('product_image',$("#file")[0].files[0]);
    $.ajax({
        type:'POST',
        url: '/addToCart/',
        data: dataForm,
        processData: false,
        contentType: false,
        dataType:'json',
        cache:false,
       
       success: function (data) {
        console.log(data)
         window.location=data.cartURL
       /* elm.text(data.qty)
        d.text(data.total)
        carttotal.text(data.withoutshipping)
        cartshipping.text(data.shippingCharges)
        totalamount.text(data.gtotal)*/
         
    }
    
    });
  }}
    
     }); 

  //    /* input data end */
  //    /* increase qty and total amount */

     $("#qtybox").click(function(){
     
      var productQtv= document.getElementById("qtybox").value
      var productTotalAmount= document.getElementById("pamount").value
      var totalAmount= productTotalAmount * productQtv
      document.getElementById("totalAmount").innerText = totalAmount
      console.log(totalAmount);
  

    });

    //  qty increase code
    $('.plus').click(function(){
     
      var id_q= $(this).attr('pid')
       console.log(id_q)
       var elm= $(this).siblings("span");
       var d = $(this).parents("td").siblings("#totalA");
       var carttotal= $('#cart_total')
       var cartshipping= $('#shippingCharges')
       var totalamount= $('#withShippingCharges')
       $.ajax({
          type:'GET',
          url: '/increaseqty/',
          data:{
          idq:id_q
           },
           success: function (data) {
           console.log(data)
           elm.text(data.qty)
           d.text(data.total)
           carttotal.text(data.withoutshipping)
           cartshipping.text(data.shippingCharges)
           totalamount.text(data.gtotal)
            
       }
      
       });
      
        });

  // // qty decrease code
    $('.minus').click(function(){
       
      var id_q= $(this).attr('pid')
       console.log(id_q)
       var elm= $(this).siblings("span");
       var d = $(this).parents("td").siblings("#totalA");
       var carttotal= $('#cart_total')
       var cartshipping= $('#shippingCharges')
       var totalamount= $('#withShippingCharges')
        
    $.ajax({
       type:'GET',
       url: '/decreaseqty/',
       data:{
       idq:id_q
      },
      success: function (data) {
        console.log(data)
        elm.text(data.qty)
        d.text(data.total)
        carttotal.text(data.withoutshipping)
        cartshipping.text(data.shippingCharges)
        totalamount.text(data.gtotal)
        
   }
   
   });
   
    });
    // delete cart Record
    // $('#delete').click(function(){
    //   /* var id_q= $(this).siblings('#cartd').children('.box').children('.minus').attr('pid')*/
    //   var id_q= $(this).attr('pid')
    //   console.log(id_q)
   
    //  var cartdel = $(this).parent()
    // //   var elm= $(this).siblings("span");
    // //   var d = $(this).parents("td").siblings("#totalA");
    // //   var carttotal= $('#cart_total')
    //   var cartshipping= $('#shippingCharges')
    //    var totalamount= $('#withShippingCharges')
         
    //  $.ajax({
    //      type:'GET',
    //      url: '/cartdel/',
    //      data:{
    //      idq:id_q
    //     },
    //     success: function (data) {
        
    //     cartdel.remove();
    //      console.log(data)
    //      elm.text(data.qty)
    //      d.text(data.total)
    //      carttotal.text(data.withoutshipping)
    //      cartshipping.text(data.shippingCharges)
    //      totalamount.text(data.gtotal)
         
    //  }
     
    //  });
    //  });

    
  //    // checkout


     $("#checkoutbtn").click(function(e){
      // data get for input
      e.preventDefault();
      
      var totalAmount= document.getElementById("totalamount").innerText;
      var total_Amount= parseInt(totalAmount)
      var addressid = $("input[name='rad']:checked").val();
      var address_id=parseInt(addressid) 
      if(isNaN(address_id))
      {
        window.alert("Please Select shipping adress")
      }
      else{
      var dataForm = new FormData();
      dataForm.append("totalAmount",total_Amount);
      dataForm.append("AddressId",address_id);
      
       $.ajax({
           type:'POST',
           url: '/goToCheckout/',
           data: dataForm,
           processData: false,
           contentType: false,
           dataType:'json',
           cache:false,
          
          success: function (data) {
           console.log(data)
           window.location=data.purl
          /* elm.text(data.qty)
           d.text(data.total)
  
           carttotal.text(data.withoutshipping)
           cartshipping.text(data.shippingCharges)
           totalamount.text(data.gtotal)*/
            
       }
       
       });}
       
        }); 
   
        // $("#service-menue").mouseenter(function(){
        //   $("mega-menue-wrapper").addClass("mega-menue-wrapper-visible");
        //   // window.alert("Please select Size and Color of the Product")
        
        //   // $("div").addClass("important");
        // });
     });
    
     
     $('.delete').click(function(){
      /* var id_q= $(this).siblings('#cartd').children('.box').children('.minus').attr('pid')*/
      var idq= $(this).attr('pid')
      var id_q= parseInt(idq)
      console.log(id_q)
   
     var cartdel = $(this).parent()
      var elm= $(this).siblings("span");
       var d = $(this).parents("td").siblings("#totalA");
       var carttotal= $('#cart_total')
      var cartshipping= $('#shippingCharges')
       var totalamount= $('#withShippingCharges')
         
     $.ajax({
         type:'GET',
         url: '/cartdel/',
         data:{
         idq:id_q
        },
        success: function (data) {
        
        cartdel.remove();
         console.log(data)
          elm.text(data.qty)
          d.text(data.total)
         carttotal.text(data.withoutshipping)
         cartshipping.text(data.shippingCharges)
         totalamount.text(data.gtotal)
         
     }
     
     });
     });
