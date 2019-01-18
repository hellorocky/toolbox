import string
import random

def random_string(length, salt=False):
    salt = "!@#$%^&*()><?"
    if salt:
        return "".join(random.choices(string.ascii_letters+string.digits, k=length-1)) + random.choice(salt)
    else:
        return "".join(random.choices(string.ascii_letters+string.digits, k=length))


if __name__ == "__main__":
    print(random_string(15, True))
