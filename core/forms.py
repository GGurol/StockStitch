from django import forms
from .models import Customer, InventoryItem, Order, Requirement, Payment, Supplier, Purchase
from django.contrib.auth.forms import UserCreationForm
from .models import CustomerUser
from django.contrib.auth.models import User

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'contact', 'address']

class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['item_name', 'item_type', 'fabric_type', 'cost_per_meter', 'total_meters', 'taxes', 'size', 'color', 'is_printed', 'stock_quantity', 'supplier', 'image']

class OrderForm(forms.ModelForm):
    product_type = forms.ChoiceField(
        choices=[('', 'Select Product Type')] + list(InventoryItem.ITEM_TYPE_CHOICES),
        required=True,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    status = forms.CharField(widget=forms.Select(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Shipped', 'Shipped')], attrs={'class': 'form-select'}))
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    inventory_item = forms.ModelChoiceField(queryset=InventoryItem.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    measurements = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter measurements as JSON'}), required=False)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].empty_label = 'Select Customer'
        self.fields['inventory_item'].empty_label = 'Select Inventory Item'
        # Fix: If measurements is None/null, set initial to empty string
        if 'measurements' in self.fields:
            value = self.initial.get('measurements') or getattr(self.instance, 'measurements', None)
            if not value or value == 'null' or value == '""':
                self.initial['measurements'] = ''
    class Meta:
        model = Order
        fields = ['customer', 'inventory_item', 'product_type', 'measurements', 'status', 'notes', 'delivery_date', 'image']

class RequirementForm(forms.ModelForm):
    steps_done = forms.CharField(
        widget=forms.Textarea(attrs={'rows':2}),
        required=False,
        help_text='Enter each completed step on a new line. This is a checklist of what has already been done for this requirement.'
    )
    steps_not_done = forms.CharField(
        widget=forms.Textarea(attrs={'rows':2}),
        required=False,
        help_text='Enter each remaining step on a new line. This is a checklist of what still needs to be done for this requirement.'
    )
    order = forms.ModelChoiceField(queryset=Order.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.steps_done:
            self.initial['steps_done'] = '\n'.join(self.instance.steps_done)
        if self.instance and self.instance.steps_not_done:
            self.initial['steps_not_done'] = '\n'.join(self.instance.steps_not_done)
        self.fields['order'].empty_label = 'Select Order'
    class Meta:
        model = Requirement
        fields = ['order', 'description', 'is_fulfilled', 'steps_done', 'steps_not_done', 'attachment', 'notes']
    def clean_steps_done(self):
        data = self.cleaned_data['steps_done']
        return [s.strip() for s in data.splitlines() if s.strip()]
    def clean_steps_not_done(self):
        data = self.cleaned_data['steps_not_done']
        return [s.strip() for s in data.splitlines() if s.strip()]

class PaymentForm(forms.ModelForm):
    order = forms.ModelChoiceField(queryset=Order.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['order'].empty_label = 'Select Order'
    class Meta:
        model = Payment
        fields = ['order', 'amount', 'status', 'payment_date', 'notes']

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'contact', 'address', 'email', 'phone']

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['supplier', 'item', 'quantity', 'price', 'notes']

class CustomerUserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email'] 