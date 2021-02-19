import random
import string


def get_random_code(length):
    chars = string.ascii_uppercase + string.digits
    code = "".join(random.choice(chars) for i in range(length))

    return code


def unique_code():
    code = get_random_code(5)

    if code and any(j.isdigit() for j in code):
        from accounts.models import Customer

        exists = Customer.objects.filter(code=code)
        if exists:
            return unique_code()
        else:
            return code
    else:
        return unique_code()


def unique_order_no():
    code = get_random_code(7)

    if code and any(j.isdigit() for j in code):
        from orders.models import Order

        exists = Order.objects.filter(number=code)
        if exists:
            return unique_order_no()
        else:
            return code
    else:
        return unique_order_no()
