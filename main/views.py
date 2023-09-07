from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Rafi Ardiel Erinaldi',
        'class': 'PBP Int'
    }

    return render(request, 'main.html', context)
