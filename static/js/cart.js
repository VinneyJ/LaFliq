// function add_to_cart(item_id) {
//     $.ajax({
//       url: '/cart/add-to-cart/' + item_id + '/',
//       type: 'POST',
//       dataType: 'json',
//       success: function(response) {
//         // Update the cart count and total in the header
//         $('#cart-count').text(response.cart_count);
//         $('#cart-total').text(response.cart_total);
        
//         // Display a success message
//         alert('Item added to cart');
//       },
//       error: function(xhr, status, error) {
//         // Display an error message
//         alert('There was a problem adding the item to the cart');
//       }
//     });
//   }
  