from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Item
from django.contrib import messages


class IndexView(View):

    def get(self, request):
        search_query = request.GET.get('search', '')
        if search_query:
            items = Item.objects.filter(
                Q(for_sale=True) &
                Q(name__icontains=search_query) |
                Q(description__icontains=search_query)
            )
            return render(request, 'main/index.html', context={'items': items})
        items = Item.objects.filter(for_sale=True)[:8]
        return render(request, 'main/index.html', context={'items': items})


class ItemDetailView(DetailView):
    model = Item
    template_name = 'main/item.html'


class CreateItemView(CreateView):
    model = Item
    template_name = 'main/create.html'
    fields = ['name', 'img', 'description', 'price', 'for_sale', 'address', 'seller', 'phone', 'pin_code']

    def get_success_url(self):
        return reverse('detail_item_url', kwargs={'pk': self.object.id})


class UpdateItemView(UpdateView):
    model = Item
    template_name = 'main/edit.html'
    fields = ['name', 'img', 'description', 'price', 'for_sale', 'address', 'seller', 'phone', 'pin_code']

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.pin_code = None
        return self.render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if int(self.request.POST['pin_code']) != self.object.pin_code:
            messages.error(request, 'Не удалось сохранить, неверный пинкод')
            return self.render_to_response(self.get_context_data())
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('detail_item_url', kwargs={'pk': self.object.id})
