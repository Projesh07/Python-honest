$(function(){
    var tables = ['payment','adminuser','siteuser','category','campaign']
    $.each( tables, function( i, val ) {
        
        $('body').on( 'init.dt','#'+ val +'table', function () {
           // alert('ofi')
            $(".glyphicon-search").addClass("ti-search").removeClass("glyphicon-search")
            
            var x = $( $("#"+ val +"table_wrapper")[0] ).children(".row")
            var y = $( x[1] )
            y.addClass("col-sm-12")
            $( y.children()[1] ).removeClass().addClass("col-sm-8")
        } );

    });
 
    

});

// var form = $("#example-advanced-form").show();
// //$('#wizard').show();
 
// form.steps({
//     headerTag: "h4",
//     bodyTag: "fieldset",
//     transitionEffect: "slideLeft",
//     onStepChanging: function (event, currentIndex, newIndex)
//     {
//         // Allways allow previous action even if the current form is not valid!
//         if (currentIndex > newIndex)
//         {
//             return true;
//         }
//         // Forbid next action on "Warning" step if the user is to young
//         if (newIndex === 3 && Number($("#age-2").val()) < 18)
//         {
//             return false;
//         }
//         // Needed in some cases if the user went back (clean up)
//         if (currentIndex < newIndex)
//         {
//             // To remove error styles
//             form.find(".body:eq(" + newIndex + ") label.error").remove();
//             form.find(".body:eq(" + newIndex + ") .error").removeClass("error");
//         }
//         form.validate().settings.ignore = ":disabled,:hidden";
//         return form.valid();
//     },
//     onStepChanged: function (event, currentIndex, priorIndex)
//     {
//         // Used to skip the "Warning" step if the user is old enough.
//         if (currentIndex === 2 && Number($("#age-2").val()) >= 18)
//         {
//             form.steps("next");
//         }
//         // Used to skip the "Warning" step if the user is old enough and wants to the previous step.
//         if (currentIndex === 2 && priorIndex === 3)
//         {
//             form.steps("previous");
//         }
//     },
//     onFinishing: function (event, currentIndex)
//     {
//         // form.validate().settings.ignore = ":disabled";
//         return form.valid();
//     },
//     onFinished: function (event, currentIndex)
//     {
//         var form = $(this);

//             // Submit form input

//             form.submit();
//     }
// }).validate({
//     errorPlacement: function errorPlacement(error, element) { element.before(error); },
//     rules: {
//         confirm: {
//             equalTo: "#password-2"
//         }
//     }
// });

// $('#wizard_load').show();


  $(document).ready(function() {

        var max_fields      = 10;
        var wrapper         = $(".containerx1");
        var wrapper2        = $(".containerx2");
        var add_button      = $(".add_link_field");

        var selected_val=$('#id_content_type :selected').text()
        
        $('#id_content_type').change(function(){
            selected_val=$('#id_content_type :selected').text();
            $(wrapper).html('');
              
        });
  
       
       // alert('lol')
        var x = 0;
        $(".add_link_field").on("click",function(e){

            console.log('lol')
            // e.preventDefault();

                if(x < max_fields){
                    x++; 

                    $(wrapper).append('<div class="form-inline" style="margin: 5px auto;"><div class="form-group"><input type="text" class="form-control" name="link[]" placeholder="Link '+x+'"><span class="delete" style=""><i class="fa fa-trash-o" aria-hidden="true"></i></span></div></div>');  //add input box
                    
                }
              else
              {
                alert('You Reached the limits')
              }
        });

        var y = 0;
        $(".add_videolink_field").on("click",function(e){

            console.log('lol')
            // e.preventDefault();

                if(y < max_fields){
                    y++; 

                    $(wrapper2).append('<div class="form-inline" style="margin: 5px auto;"><div class="form-group"><input type="text" class="form-control" name="vidlink[]" placeholder="Link '+y+'"><span class="delete" style=""><i class="fa fa-trash-o" aria-hidden="true"></i></span></div></div>');  //add input box
                    
                }
              else
              {
                alert('You Reached the limits')
              }
        });

        $("[class*='containerx']").on("click",".delete", function(e){
            e.preventDefault(); $(this).parent('div').remove(); 
            x--;
            console.log("down")
        })
    });

    // alert('ol')



