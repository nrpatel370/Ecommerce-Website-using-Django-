from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func, ExpressionWrapper, DecimalField
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from store.models import Product, Customer, OrderItem, Promotion, Order, Collection, Cart, CartItem
from django.contrib.contenttypes.models import ContentType
from tags.models import TaggedItem
# Create your views here.
#req->res request handler


def say_hello(req):


    #products = Product.objects.filter(id__in = OrderItem.objects.values('id').distinct()).order_by('title')
    # orders = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    # orders = Order.objects.filter(customer__id ='1').aggregate(count=Count('id'))
    # querySet = Customer.objects.annotate(is_new = Value(True))
    # discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    # querySet = Product.objects.annotate(
    #    discounted_price = discounted_price
        
    # content_type = ContentType.objects.get_for_model(Product)
    # querySet = TaggedItem.objects.select_related('tag').filter(
    #     content_type = content_type,
    #     object_id = 1
    # )

    # collection = Collection()
    # collection.title = 'video'
    # collection.featured_product = Product(pk=1)
    # collection.save()
   
    # cart = Cart()
    # cart.id = 1
    # cart.save()

    

    # cartItem = CartItem()
    # cartItem.id = 1
    # cartItem.quantity = 2
    # cartItem.save()

    # cartItem.quantity.update(1)
    # cartItem.save()

    # cart = Cart(pk = 1)
    # cart.delete()

    return render(req, 'hello.html')