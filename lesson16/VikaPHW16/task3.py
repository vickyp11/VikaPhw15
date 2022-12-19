"""
Write a class Product that has three attributes:

type
name
price
Then create a class ProductStore, which will have some Products and will operate with all products in the store. All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.

Tips: Use aggregation/composition concepts while implementing the ProductStore class. You can also implement additional classes to operate on a certain type of product, etc.

Also, the ProductStore class must have the following methods:

add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your store(30 percent)
set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by input identifiers (type or name). The discount must be specified in percentage
sell_product(product_name, amount) - removes a particular amount of products from the store if available, in other case raises an error. It also increments income if the sell_product method succeeds.
get_income() - returns amount of many earned by ProductStore instance.
get_all_products() - returns information about all available products in the store.
get_product_info(product_name) - returns a tuple with product name and amount of items in the store.
"""


class Product:
    def __init__(self, types, name, price):
        self.types = types
        self.name = name
        self.price = price

class ProductStore:
    def __init__(self):
        self.products = []
        self.inventory = []
        self.discounts_name = []
        self.discounts_type = []
        self.income = 0

    def add(self, product, amount):
        self.products.append((product.name, amount, product.price))
        print (f'Product has been succesfully added  in the amount of {amount}')

    def set_discount(self, identifier, percentage, identifier_type='name'):
        if identifier_type == 'name':
            self.discounts_name.append((identifier, percentage))
        elif identifier_type == 'type':
            self.discounts_type.append((identifier, percentage))
        else:
            raise ValueError (f'Please make sure to insert type or name!')

    def sell_product(self, product_name, amount_sold):
        for i in self.products:
            if i[0] == product_name:
                if amount_sold > i[1]:
                    raise ValueError (f'Not enough products in stock!')
                elif amount_sold <= i[1]:
                    self.products.remove(i)
                    self.products.append((product_name, i[1]-amount_sold, i[2]))
                    print('Item was successfully sold!')
                    self.income = i[2]*0.3*amount_sold
                else:
                    raise ValueError (f'Product not found')

    def get_income(self):
        return s.income

    def get_all_products(self):
        for i in self.products:
            if i[1] > 0:
                print(i)

    def get_product_info(self, product_search):
        for i in self.products:
            if i[0] == product_search:
                return i


p = Product('Sport', 'Football T-Shirt', 10)
p2 = Product('Food', 'Ramen', 15)

s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
print(s.products)

s.set_discount('Ramen', 25)
s.set_discount('Food', 15, 'type')
print(s.discounts_name, s.discounts_type)


s.sell_product('Ramen', 299)
print(s.products)

print(s.get_income())

s.get_all_products()

print(s.get_product_info('Ramen'))

















