import random
import string


def get_random_code(length):
    chars = string.ascii_uppercase + string.digits
    code = "".join(random.choice(chars) for i in range(length))

    return code


def generate_unique_code(model_name, length):
    model = None

    from accounts.models import Customer
    from orders.models import Order

    models = {"customer": Customer, "order": Order}
    if model_name in models.keys():
        model = models.get(model_name)
    else:
        raise ValueError("Invalid model type")

    code = get_random_code(length)

    if code:
        if any(j.isdigit() for j in code):
            exists = model.objects.filter(code=code)
            if exists:
                return generate_unique_code()
            else:
                return code
    else:
        return generate_unique_code()
