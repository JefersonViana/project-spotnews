from django.core.exceptions import ValidationError


def validate_sigle_title(value):
    if " " not in value:
        raise ValidationError("O título deve conter pelo menos 2 palavras.")
