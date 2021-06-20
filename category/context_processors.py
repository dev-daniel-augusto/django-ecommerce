from category.models import Category


def menu(request):
    links = Category.objects.all()
    return dict(categories=links)
