from django.shortcuts import render, redirect, get_object_or_404
from .models import Supplier
from django import forms

# Form tailored to the Supplier model and HTML form fields
class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = [
            'code', 'name', 'email', 'mobile_phone', 'address1', 'contact_name',
            'address2', 'tin', 'address3', 'gst_exempt', 'post_code', 'bank',
            'phone_no', 'bsb', 'email2', 'bank_account', 'product', 'bank_account_name'
        ]
        widgets = {
            'code': forms.TextInput(attrs={'placeholder': 'Enter code', 'required': True}),
            'name': forms.TextInput(attrs={'placeholder': 'Enter Supplier Name', 'required': True}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email'}),
            'mobile_phone': forms.TextInput(attrs={'placeholder': 'Enter mobile phone'}),
            'address1': forms.TextInput(attrs={'placeholder': 'Enter address 1'}),
            'contact_name': forms.TextInput(attrs={'placeholder': 'Enter contact name'}),
            'address2': forms.TextInput(attrs={'placeholder': 'Enter address 2'}),
            'tin': forms.TextInput(attrs={'placeholder': 'Enter TIN'}),
            'address3': forms.TextInput(attrs={'placeholder': 'Enter address 3'}),
            'gst_exempt': forms.TextInput(attrs={'placeholder': 'Enter GST exempt'}),
            'post_code': forms.TextInput(attrs={'placeholder': 'Enter post code'}),
            'bank': forms.TextInput(attrs={'placeholder': 'Enter bank'}),
            'phone_no': forms.TextInput(attrs={'placeholder': 'Enter phone no'}),
            'bsb': forms.TextInput(attrs={'placeholder': 'Enter BSB'}),
            'email2': forms.EmailInput(attrs={'placeholder': 'Enter email'}),
            'bank_account': forms.TextInput(attrs={'placeholder': 'Enter bank account'}),
            'product': forms.TextInput(attrs={'placeholder': 'Enter product'}),
            'bank_account_name': forms.TextInput(attrs={'placeholder': 'Enter bank account name'}),
        }

# Create a new supplier
def supplier_create(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')
    else:
        form = SupplierForm()
    return render(request, 'PO_Data/supplier_List_Form.html', {'form': form})

# List all suppliers
def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'PO_Data/supplier_list.html', {'suppliers': suppliers})

# Edit an existing supplier
def supplier_edit(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'PO_Data/supplier_List_Form.html', {'form': form, 'edit': True})

# Delete a supplier
def supplier_delete(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        supplier.delete()
        return redirect('supplier_list')
    return render(request, 'PO_Data/supplier_confirm_delete.html', {'supplier': supplier})