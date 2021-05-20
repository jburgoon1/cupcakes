
$('.delete-cupcake').click(delete_cupcake);

async function delete_cupcake(){
const id = $(this).data('id')
await axios.delete(`/api/cupcakes/${id}`)
$(this).parent().remove()
};


$('make-cupcake').click(make_cupcake)

async function make_cupcake(e){
    const flavor = $('.flavor').val();
    const size = $('.size').val()
    const rating = $('.rating').val()
    const image = $('.image').val()
    await axios.post('/api/cupcakes', {flavor: flavor, size: size, rating: rating, image: image})
    $('ul').append(this)
}
