from .models import Category

def category(request):
    return {'cats': Category.objects.all()} 