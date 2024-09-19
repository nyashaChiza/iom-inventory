from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from accounts.models import CustomUser
from stock.models import Request, Approval
from stock.forms import RequestForm
from django.urls import reverse


# List View
class RequestListView(generic.ListView):
    model = Request
    template_name = 'request/index.html'
    context_object_name = 'requests'

class RequestCreateView(generic.CreateView):
    model = Request
    form_class = RequestForm
    template_name = 'request/create.html'
    
    
    def get_success_url(self) -> str:
        return reverse('transaction_create', kwargs={'request_id': self.object.id})

    def form_valid(self, form):
        # Save the request instance
        request_instance = form.save()
        
        # Create approval entries for all active users with approval roles
        active_users_with_approval_role = self.get_active_users_with_approval_role()
        for user in active_users_with_approval_role:
            Approval.objects.create(request=request_instance, approver=user)

        return super().form_valid(form)

    def get_active_users_with_approval_role(self):
        # Replace this with your actual logic to get active users with approval roles
        return CustomUser.objects.filter(is_active=True, role__name='Approver')  # Adjust as per your user model



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