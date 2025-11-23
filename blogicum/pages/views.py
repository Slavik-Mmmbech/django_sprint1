from django.shortcuts import render


# Create your views here.
def about(request):
    """
    Представление для страницы "О проекте"
    Возвращает шаблон с информацией о проекте.
    """
    return render(request, 'pages/about.html')


def rules(request):
    """
    Представление для страницы "Правила"
    Возвращает шаблон с правилами использования.
    """
    return render(request, 'pages/rules.html')
