
$(document).ready(function(){

$('.delete-cupcake').click(delete_cupcake);

async function delete_cupcake(){
const id = $(this).data('id')
await axios.delete(`/api/cupcakes/${id}`)
$(this).parent().remove()
};


$('#create_form').on('submit', make_cupcake)

async function make_cupcake(e){
    e.preventDefault();
    const flavor = $('.flavor').val();
    const size = $('.size').val()
    const rating = $('.rating').val()
    const image = $('.image').val()
    await axios.post('/api/cupcakes', {flavor: flavor, size: size, rating: rating, image: image})
    $('#cupcake-list').append(data)

    
}
})
