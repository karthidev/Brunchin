

$( document ).ready(function() {
    $.ajax({
        type: 'GET',
        url: "getcartdetails",
        success: function (res) {
            console.log(res.context)
            $('.cls_carts').html('('+res.context+')')
        },
        error: function (xhr, err) {
            console.log(xhr.responseText);
        },
    });
});


$('.cls_nonvegfilters').on('change',function(){

console.log($(this).val())
$.ajax({
    type: 'POST',
    url: "brunchfilter/"+$(this).val(),
    data:$(this).val(),
    success: function (res) {
        $('.food_items').remove();
        $.each(res.context, function(key,val){
     console.log(val.food_name)
        html=(`
   <div class="col col-sm-3 food_items d-flex justify-content-center">
  <div class="col">
   <div class="card" style="width:300px">
   <img class="card-img-top food_img" src="/static/${val.food_img}" alt="Card image" width="200px" height="200px">
   <h6 class="card-title">${val.food_name}</h6
   <h6 class="card-title">₹${val.food_price}</h6>
   </div>
   <div class="col">
   <p class="card-text">${val.food_restaurant}</p>
    </div>
   <div class="col">
   <a href="" class="btn btn-danger cls_addcart">Add</a>
   </div>
 </div>
 </div>`);
 $('.cls_footcats').append(html);
        });
        //console.log(res.context)
    },
    error: function (xhr, err) {
       // console.log(xhr.responseText);
    },
});
});


$('.cls_addcart').on('click',function() {
    
})
