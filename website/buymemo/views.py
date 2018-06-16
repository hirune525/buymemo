from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import BuyItem


@method_decorator(login_required, name='dispatch')
class IndexView(ListView):
    template_name = 'buymemo/index.html'
    model = BuyItem


@method_decorator(login_required, name='dispatch')
class DetailView(DetailView):
    model = BuyItem

