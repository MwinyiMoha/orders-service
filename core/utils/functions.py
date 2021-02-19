import random
import string


def unique_code():
    chars = string.ascii_uppercase + string.digits
    code = "".join(random.choice(chars) for i in range(5))

    if code and any(j.isdigit() for j in code):
        from accounts.models import Customer

        exists = Customer.objects.filter(code=code)
        if exists:
            return unique_code()
        else:
            return code
    else:
        return unique_code()
