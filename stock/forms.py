from django import forms
from .models import Stock, Request, Transaction, Approval

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['name', 'category', 'department', 'quantity']
        



class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['user', 'source', 'destination']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Get the user from kwargs
        super(RequestForm, self).__init__(*args, **kwargs)
        
        # Set the user field as hidden
        if user:
            self.fields['user'].initial = user
            self.fields['user'].widget = forms.HiddenInput()

        # Add Bootstrap classes to the fields
        self.fields['user'].widget.attrs.update({'readonly': True, 'class': 'form-control'})
        self.fields['source'].widget.attrs.update({'class': 'form-control'})
        self.fields['destination'].widget.attrs.update({'class': 'form-control'})


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['stock', 'quantity', 'transaction_type']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Call the parent __init__ method
        # Add Bootstrap classes to the form fields
        self.fields['stock'].widget.attrs.update({'class': 'form-control'})
        self.fields['quantity'].widget.attrs.update({'class': 'form-control'})
        self.fields['transaction_type'].widget.attrs.update({'class': 'form-control'})
        
class ApprovalForm(forms.ModelForm):
    class Meta:
        model = Approval
        fields = ['status']  # You can include other fields if needed

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].widget.attrs.update({'class': 'form-control'})  # Add Bootstrap class