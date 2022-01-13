from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse

from django.contrib import messages
from products.models import Product

# Create your views here.

def view_bag(request):
    """ A view that renders a shoping bag contents page """

    return render(request, 'bag/bag.html')

def add_to_mybag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id) 
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    warranty = None
    if 'product_warranty' in request.POST:
        warranty = request.POST['product_warranty']
    bag = request.session.get('bag', {})

    if warranty:
        if item_id in list(bag.keys()):
            if warranty in bag[item_id]['items_by_warranty'].keys():
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

def adjust_mybag(request, item_id):
    """ Adjust the quantity of the specified product to the shopping bag """
    
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    warranty = None
    if 'product_warranty' in request.POST:
        warranty = request.POST['product_warranty']
    bag = request.session.get('bag', {})

    if warranty:
        if quantity > 0:
            bag[item_id]['items_by_warranty'][warranty] = quantity
            messages.success(
                    request, f'Updated warranty {warranty.upper()} {product.name} quantity to {bag[item_id]["items_by_warranty"][warranty]}')
        else:
            del bag[item_id]['items_by_warranty'][warranty]
            if not bag[item_id]['items_by_warranty']:
                bag.pop(item_id)
            messages.success(request, f'Removed warranty {warranty.upper()} {product.name} from your bag')           
        
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
            
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')           

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_mybag(request, item_id):
    """ Remove the specified product to the shopping bag """

    try:
        product = get_object_or_404(Product, pk=item_id)
        warranty = None
        if 'product_warranty' in request.POST:
            warranty = request.POST['product_warranty']
        bag = request.session.get('bag', {})

        if warranty:
            del bag[item_id]['items_by_warranty'][warranty]
            if not bag[item_id]['items_by_warranty']:
                bag.pop(item_id)
            messages.success(request, f'Removed warranty {warranty.upper()} {product.name} from your bag')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
