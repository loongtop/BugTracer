from django.views.generic.base import View
from django.shortcuts import render
from web.forms.account import RegisterModelForm


class RegisterView(View):
    def post(self, request):
        form = RegisterModelForm()
        return render(request, 'register.html', {'form': form})

    def get(self, request):
        form = RegisterModelForm()
        return render(request, 'register.html', {'form': form})