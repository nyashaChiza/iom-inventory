from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from stock.models import Transaction, Request
from django.views import generic
from stock.forms import TransactionForm


# List View
class TransactionListView(generic.ListView):
    model = Transaction
    template_name = 'transaction_list.html'
    context_object_name = 'transactions'

# Create View
class TransactionCreateView(generic.CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transaction/create.html'

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
        return redirect(reverse('request_detail', kwargs={'pk': request_id}))




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