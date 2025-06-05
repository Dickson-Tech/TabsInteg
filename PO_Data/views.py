from django.shortcuts import render, get_object_or_404, redirect
from .models import Supplier
from .forms import SupplierForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages

# Create your views here.
def supplier_list_view(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            suppliers = Supplier.objects.filter(name__icontains=form.cleaned_data['name'])
        else:
            suppliers = Supplier.objects.all()
    else:
        form = SupplierForm()
        suppliers = Supplier.objects.all()
    return render(request, 'supplier_List_form.html', {'form': form, 'suppliers': suppliers})

# Create a new supplier
def supplier_create(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            name = form.cleaned_data['name']
            if Supplier.objects.filter(code=code).exists() or Supplier.objects.filter(name=name).exists():
                form.add_error(None, "Supplier with this code or name already exists.")
            else:
                form.save()
                messages.success(request, "Supplier created successfully!")
                return redirect('supplier_list')
    else:
        form = SupplierForm()
    return render(request, 'PO_Data/supplier_List_Form.html', {'form': form})

# List all suppliers
def supplier_list(request):
    query = request.GET.get('search', '')
    suppliers = Supplier.objects.all().order_by('name')
    if query:
        suppliers = suppliers.filter(name__icontains=query)
    paginator = Paginator(suppliers, 15)  # Show 15 suppliers per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'PO_Data/supplier_list.html', {
        'page_obj': page_obj,
        'search': query,
    })

# Edit an existing supplier
def supplier_edit(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            messages.success(request, "Supplier updated successfully!")
            return redirect('supplier_list')
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'PO_Data/supplier_List_Form.html', {'form': form, 'edit': True, 'supplier': supplier})

# Delete a supplier
def supplier_delete(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        supplier.delete()
        return redirect('supplier_list')
    return render(request, 'PO_Data/supplier_confirm_delete.html', {'supplier': supplier})