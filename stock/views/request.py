from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from stock.models import Request
from stock.forms import RequestForm
from django.urls import reverse


# List View
class RequestListView(generic.ListView):
    model = Request
    template_name = 'request/index.html'
    context_object_name = 'requests'

# Create View
class RequestCreateView(generic.CreateView):
    model = Request
    form_class = RequestForm
    template_name = 'request/create.html'
    success_url = reverse_lazy('request_index')  # This can be used for other redirects if needed

    def form_valid(self, form):
        # Call the parent class's form_valid method to save the request
        response = super().form_valid(form)
        
        # Redirect to the TransactionCreateView with the new request ID
        return redirect(reverse('transaction_create', kwargs={'request_id': self.object.id}))

# Detail View
class RequestDetailView(generic.DetailView):
    model = Request
    template_name = 'request/details.html'
    context_object_name = 'request'

# Update View
class RequestUpdateView(generic.UpdateView):
    model = Request
    form_class = RequestForm
    template_name = 'request/update.html'
    success_url = reverse_lazy('request_list')

# Delete View
class RequestDeleteView(generic.DeleteView):
    model = Request
    template_name = 'request/delete.html'
    success_url = reverse_lazy('request_list')