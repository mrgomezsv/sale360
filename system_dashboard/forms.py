from django import forms
from django.forms import inlineformset_factory
from .models import SaleOrder, SaleOrderLine, Partner, Product

class SaleOrderForm(forms.ModelForm):
    class Meta:
        model = SaleOrder
        fields = ['partner_id', 'date_order', 'validity_date', 'note']
        widgets = {
            'date_order': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'validity_date': forms.DateInput(attrs={'type': 'date'}),
            'note': forms.Textarea(attrs={'rows': 4}),
        }

class SaleOrderLineForm(forms.ModelForm):
    class Meta:
        model = SaleOrderLine
        fields = ['product_id', 'name', 'product_uom_qty', 'price_unit', 'discount', 'tax_rate']
        widgets = {
            'name': forms.Textarea(attrs={'rows': 2}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product_id'].queryset = Product.objects.filter(active=True)

# Formset para las líneas de pedido
SaleOrderLineFormSet = inlineformset_factory(
    SaleOrder,
    SaleOrderLine,
    form=SaleOrderLineForm,
    extra=1,  # Número de formularios vacíos
    can_delete=True,  # Permite eliminar líneas
    min_num=1,  # Mínimo número de líneas
    validate_min=True,  # Valida el mínimo
)
