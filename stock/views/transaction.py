from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from stock.models import Transaction, Request, Stock
from django.views import generic
from stock.forms import TransactionForm


# Create View
class TransactionCreateView(generic.CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transaction/create.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['request'] = get_object_or_404(Request, id=self.kwargs.get('request_id'))
        return context
    def get_initial(self):
        initial = super().get_initial()
        request_id = self.kwargs.get('request_id')
        initial['request'] = get_object_or_404(Request, id=request_id)  # Set the request from URL
        return initial

    def form_valid(self, form):
        request_id = self.kwargs.get('request_id')
        form.instance.request = get_object_or_404(Request, id=request_id)  # Associate the request
        response = super().form_valid(form)
        
        # Redirect to the request detail page
        return redirect(reverse('request_details', kwargs={'pk': request_id}))
    
    def get_success_url(self) -> str:
        request_id = self.kwargs.get('request_id')
        return reverse('request_details', kwargs={'pk': request_id})




# Detail View
class TransactionDetailView(generic.DetailView):
    model = Transaction
    template_name = 'transaction_detail.html'
    context_object_name = 'transaction'

# Update View
class TransactionUpdateView(generic.UpdateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transaction_form.html'
    success_url = reverse_lazy('transaction_list')

# Delete View
class TransactionDeleteView(generic.DeleteView):
    model = Transaction
    template_name = 'transaction_confirm_delete.html'
    success_url = reverse_lazy('transaction_list')
    
    
class TransactionListView(generic.ListView):
    model = Transaction
    template_name = 'transaction/index.html'  # Create this template
    context_object_name = 'transactions'

    def get_queryset(self):
        stock_id = self.kwargs.get('stock_id')  # Get the stock ID from the URL
        return Transaction.objects.filter(stock_id=stock_id)  # Filter transactions by stock

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stock_id = self.kwargs.get('stock_id')
        context['stock'] = get_object_or_404(Stock, id=stock_id)  # Get the stock for the context
        return context