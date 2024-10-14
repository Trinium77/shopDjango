from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ('user', 'ordered_at', 'status')
    search_fields = ('user__username',)

admin.site.register(Order, OrderAdmin)
