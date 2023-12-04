from django.core.exceptions import ValidationError


def title_validate(title):
    if len(title.split(" ")) < 2:
        raise ValidationError("O título deve conter pelo menos 2 palavras.")
