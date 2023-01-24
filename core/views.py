from django.views.generic import View
from django.shortcuts import render


# Esta es una vista con clase
# Tambien hay vistas con funciones


class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'index.html', context)
