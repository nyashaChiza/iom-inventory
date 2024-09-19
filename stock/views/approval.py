from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404
from stock.models import Approval, Request
from stock.forms import ApprovalForm  # Make sure to create this form

class ApprovalUpdateView(generic.UpdateView):
    model = Approval
    form_class = ApprovalForm
    template_name = 'approvals/update.html'  # Create this template
    success_url = reverse_lazy('request_index')  # Redirect to the approval list after updating

    def get_object(self, queryset=None):
        # Get the approval object using the primary key from the URL
        return get_object_or_404(Approval, pk=self.kwargs['pk'])
    
    
class ApprovalListView(generic.ListView):
    model = Approval
    template_name = 'approvals/index.html'  # Create this template
    context_object_name = 'approvals'

    def get_queryset(self):
        request_id = self.kwargs.get('request_id')  # Get the request ID from the URL
        return Approval.objects.filter(request_id=request_id)  # Filter approvals by request ID

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request_id = self.kwargs.get('request_id')
        context['object'] = get_object_or_404(Request, id=request_id)  # Add the request to the context
        return context