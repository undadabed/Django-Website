from django import forms

from .models import Product, OrderItem

class ProductForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Title"}))
    price = forms.DecimalField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "5.95",
            }
        )
    )
    description = forms.CharField(
        required=False, 
        widget=forms.TextInput(
            attrs={
                "placeholder": "Description",
            }
        )
    )
    summary = forms.CharField(
        required=False, 
        widget=forms.Textarea(
            attrs={
                "placeholder": "Summary",
                "class": "new-class-name two",
                "id": "my-id-for-textarea", 
                "rows": 20,
                'cols': 120,
            }
        )
    )
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'summary',
            'display_image',
        ]

class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = [
            'quantity'
        ]