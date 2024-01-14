from .models import Product
from decimal import Decimal


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart_key')

        if 'cart_key' not in request.session:
            cart = self.session['cart_key'] = {}

        self.cart = cart
        print(self.cart)

    def add(self, product):
        '''
        ADDING AND UPDATING THE USERS BASKET SESSION
        product is the product from the database
        '''

        product_id = product.id

        print(self.cart)
        # if item exist in basket
        if str(product_id) in self.cart:
            # check if it is an update of quantity increase quantity of the product in cart
            self.increment(product)
            print('THIS BLOC EXECUTED')
        else:
            print('new product added')
            self.cart[product_id] = {
                'id': product_id,
                'slug': product.slug,
                'price': float(product.price),
                'image': str(product.image_url),
                'name': str(product.name),
                'quantity': 1,
            }

        self.session.modified = True

    def increment(self, product):
        self.cart[str(product.id)]['quantity'] += 1
        print(self.cart)
        print('quantity increased')

        self.session.modified = True

    def calculate_total(self, product):
        quantity = self.cart[str(product.id)]['quantity']
        price = self.cart[str(product.id)]['price']
        return price * quantity

    def decrement(self, product):
        if self.cart[str(product.id)]['quantity'] > 1:
            self.cart[str(product.id)]['quantity'] -= 1
        else:
            self.remove(product)
        self.session.modified = True

    def remove(self, product):
        '''
            remove item from list
        '''
        product_id = product.id

        print(self.cart)
        # if item exist in basket
        if str(product_id) in self.cart:
            # check if it is an update of quantity increase quantity of the product in cart
            del self.cart[str(product_id)]
            print('THIS BLOC EXECUTED')

        self.session.modified = True

    def get_cart_total(self):
        return sum([item['price'] * item['quantity'] for item in self.cart.values()])

    def __len__(self):
        return sum([item['quantity'] for item in self.cart.values()])

    def __iter__(self):
        """ function to display all items in the cart"""

        return iter([item for item in self.cart.values()])
