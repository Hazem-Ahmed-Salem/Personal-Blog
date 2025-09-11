from blog import models


def get_author():
    return models.Author.objects.all().first() if models.Author.objects.exists() else None