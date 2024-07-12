from django.shortcuts import render,redirect
from list.models import Tovar
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

def index(r):
    tovari = Tovar.objects.all()
    print(tovari [1].comments.all())
    numbers = [1,2,3,4,5]
    return render(r, 'index.html', {'tovari': tovari, 'numbers': numbers, 'comments': tovari [1].comments.all()})
def buy(r):
    print(r.GET.get("name"))
    return redirect("home")

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Tovar
    context_object_name = 'product'




    
# Create your views here.
