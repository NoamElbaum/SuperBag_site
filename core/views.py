from django.shortcuts import render

from django.views.generic import ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Item, OrderItem, Order, CATEGORY_CHOISES

# Create your views here.
class HomeView(ListView):
    model = Item
    paginate_by = 1
    template_name = 'core/home.html'

    def get_paginate_by(self, queryset):
        self.paginate_by = 1
        return self.paginate_by

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_list'] = CATEGORY_CHOISES
        return context

# class CatHomeView(ListView):

#     model = Item
#     paginate_by = 1
#     template_name = 'core/home.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['cat_list'] = CATEGORY_CHOISES
#         context['object_list'] = Item.objects.filter(category=self.kwargs['cat'])
        # return context
def CatHomeView(request, **kwargs):
    pag_by = 1
    products = Item.objects.filter(category=kwargs['cat'])
    context = {'cat_list': CATEGORY_CHOISES, 'cat': kwargs['cat']}
    if len(products) > pag_by:
        context['is_paginated'] = True
    else:
        context['is_paginated'] = False
    paginator = Paginator(products, pag_by)
    page_number = request.GET.get('page') or 1
    context['page_obj'] =  paginator.get_page(page_number)
    context['object_list'] = paginator.get_page(page_number)
    return render(request, 'core/home.html', context)

class OrderSummaryView(LoginRequiredMixin, View ):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, is_ordered=False)
        except ObjectDoesNotExist:
             messages.error(self.request,'You do not have an active order')
             return redirect('/')
        else:
            context = {'object':order}
            return render(self.request, 'core/order_summary.html', context)

class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"

