from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ A view that renders a shoping bag contents page """

    return render(request, 'bag/bag.html')

def add_to_mybag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    warranty = None
    if 'product_warranty' in request.POST:
        warranty = request.POST['product_warranty']
    bag = request.session.get('bag', {})

    if warranty:
        if item_id in list(cart.keys()):
            if warranty in cart[item_id]['items_by_warranty'].keys():
                bag[item_id]['items_by_warranty'][warranty] += quantity
                messages.success(
                    request, f'Updated warranty {warranty.upper()} {product.name} quantity to {bag[item_id]["items_by_warranty"][warranty]}')
            else:
                bag[item_id]['items_by_warranty'][warranty] = quantity
                messages.success(
                    request, f'Added warranty {warranty.upper()} {product.name} to your bag.')
        else:
            bag[item_id] = {'items_by_warranty': {warranty: quantity}}
            messages.success(
                request, f'Added warranty {warranty.upper()} {product.name} to your bag.')
    else:
        if item_id in list(bag.keys()):
          bag[item_id] += quantity
        else:
          bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
# Create your views here.
