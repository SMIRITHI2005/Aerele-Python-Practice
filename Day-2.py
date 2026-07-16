def add_item2(item, cart=[]):

    if cart is None:
        cart = []

    cart.append(item)

    return cart
print(add_item2("s"))
print(add_item2("j"))


def add_item(item, cart=None):

    if cart is None:
        cart = []

    cart.append(item)

    return cart
print(add_item("smi"))
print(add_item("smiri"))
def total(a,b,c):
    return a+b+c
print(total(1,2,3))
def total1(*n):
    return(sum(n))
print(total1(1,2,3,4,5))

def create_user(**name):
    print(name)

create_user(
    name="Ammu",
    age=21,
    city="Coimbatore"
)