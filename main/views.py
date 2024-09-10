from django.shortcuts import render

def show_main(request):
    context = {
        'application_name': 'Vortex Vision',
        'class': 'PBD KKI',
        'name': 'Adiena Nimeesha Adiwinastwan',
    }

    return render(request, "main.html", context)
