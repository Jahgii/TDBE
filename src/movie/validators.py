from django.core.exceptions import ValidationError


def validate_studio_capital(value):
    if value[0].isupper():
        return value
    else:
        raise ValidationError("Studio must be initialized with a capital letter!")
