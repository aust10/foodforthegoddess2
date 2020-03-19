from django.shortcuts import render
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy
from django.views import generic
from recipe_app.models import Favorite


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

    def get(self, request):
        form = self.form_class()
        users = users.objects.all()
        favorite_recipes = Favorite.objects.get_or_create(current_user=request.user)
        return render(request, self.template_name, {'form': form, 'users': users})


    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()    
            return render(request, self.template_name, {'form': form})
