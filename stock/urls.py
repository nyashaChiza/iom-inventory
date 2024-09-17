from django.urls import path
from stock.views import StockListView, StockCreateView, StockDetailView, StockUpdateView, StockDeleteView

urlpatterns = [
    path('', StockListView.as_view(), name='stock_index'),
    path('create/', StockCreateView.as_view(), name='stock_create'),
    path('<int:pk>/', StockDetailView.as_view(), name='stock_detail'),
    path('<int:pk>/update/', StockUpdateView.as_view(), name='stock_update'),
    path('<int:pk>/delete/', StockDeleteView.as_view(), name='stock_delete'),
]