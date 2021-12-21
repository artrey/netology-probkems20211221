from django.contrib import admin
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from demo.models import Product, Order, OrderPosition


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    search_fields = ['name']


class PositionsInlineFormset(BaseInlineFormSet):
    def clean(self):
        if len(self.forms) == 0:
            raise ValidationError('Не указаны товары!')

        if len(self.forms) != len({form.cleaned_data['product'].id for form in self.forms}):
            raise ValidationError('Товары дублируются!')

        return super().clean()


class PositionInline(admin.TabularInline):
    model = OrderPosition
    formset = PositionsInlineFormset
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'client']
    list_filter = ['client']
    inlines = [PositionInline]
