from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404
from .models import CustomUser
from .forms import UserRegistrationForm  # Assuming you have this form

# List View
class UserListView(generic.ListView):
    model = CustomUser
    template_name = 'users/index.html'  # Create this template
    context_object_name = 'users'

# Create View
class UserCreateView(generic.CreateView):
    model = CustomUser
    form_class = UserRegistrationForm  # Use the registration form
    template_name = 'users/create.html'  # Create this template
    success_url = reverse_lazy('user_index')  # Redirect to user list after creation

# Update View
class UserUpdateView(generic.UpdateView):
    model = CustomUser
    form_class = UserRegistrationForm  # Use the registration form
    template_name = 'users/update.html'  # Same template as for creation
    success_url = reverse_lazy('user_index')  # Redirect to user list after update

    def get_object(self, queryset=None):
        return get_object_or_404(CustomUser, pk=self.kwargs['pk'])

# Delete View
class UserDeleteView(generic.DeleteView):
    model = CustomUser
    template_name = 'user_confirm_delete.html'  # Create this template
    success_url = reverse_lazy('user_list')  # Redirect to user list after deletion

    def get_object(self, queryset=None):
        return get_object_or_404(CustomUser, pk=self.kwargs['pk'])