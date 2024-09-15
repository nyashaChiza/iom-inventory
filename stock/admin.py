from django.contrib import admin
from .models import Category, Department, Stock, Request, Transaction

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')
    search_fields = ('name',)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')
    search_fields = ('name',)

class StockAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'department', 'quantity', 'created', 'updated')
    list_filter = ('category', 'department')
    search_fields = ('name',)
    ordering = ('-created',)

class RequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'source', 'destination', 'approved', 'created', 'updated')
    list_filter = ('approved', 'source', 'destination')
    search_fields = ('user__username', 'stock__name')
    ordering = ('-created',)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('stock', 'transaction_type', 'quantity', 'created', 'updated')
    list_filter = ('transaction_type',)
    search_fields = ('stock__name',)
    ordering = ('-created',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Request, RequestAdmin)
admin.site.register(Transaction, TransactionAdmin)
