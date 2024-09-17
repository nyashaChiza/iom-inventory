from django.urls import reverse_lazy
from stock.models import Stock
from django.views import generic
from stock.forms import StockForm
# List View
class StockListView(generic.ListView):
    model = Stock
    template_name = 'stock/index.html'
    context_object_name = 'stocks'

# Create View
class StockCreateView(generic.CreateView):
    model = Stock
    form_class = StockForm
    template_name = 'stock/create.html'
    success_url = reverse_lazy('stock_list')

# Detail View
class StockDetailView(generic.DetailView):
    model = Stock
    template_name = 'stock/details.html'
    context_object_name = 'stock'

# Update View
class StockUpdateView(generic.UpdateView):
    model = Stock
    form_class = StockForm
    template_name = 'stock/update.html'
    success_url = reverse_lazy('stock_list')

# Delete View
class StockDeleteView(generic.DeleteView):
    model = Stock
    template_name = 'stock/delete.html'
    success_url = reverse_lazy('stock_list')