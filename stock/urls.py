from django.urls import path
from stock.views import StockListView, StockCreateView, StockDetailView, StockUpdateView, StockDeleteView

from stock.views import (
    RequestListView,
    RequestCreateView,
    RequestDetailView,
    RequestUpdateView,
    RequestDeleteView,
)

from stock.views import (
    TransactionListView,
    TransactionCreateView,
    TransactionDetailView,
    TransactionUpdateView,
    TransactionDeleteView,
)
from stock.views import ApprovalUpdateView, ApprovalListView

urlpatterns = [
    path('stocks/<int:stock_id>/transactions/', TransactionListView.as_view(), name='transaction_list'),
    path('transactions/create/<int:request_id>/', TransactionCreateView.as_view(), name='transaction_create'),
    path('transactions/<int:pk>/', TransactionDetailView.as_view(), name='transaction_detail'),
    path('transactions/<int:pk>/update/', TransactionUpdateView.as_view(), name='transaction_update'),
    path('transactions/<int:pk>/delete/', TransactionDeleteView.as_view(), name='transaction_delete'),
    path('', StockListView.as_view(), name='stock_index'),
    path('create/', StockCreateView.as_view(), name='stock_create'),
    path('<int:pk>/', StockDetailView.as_view(), name='stock_details'),
    path('<int:pk>/update/', StockUpdateView.as_view(), name='stock_update'),
    path('<int:pk>/delete/', StockDeleteView.as_view(), name='stock_delete'),
    path('requests/', RequestListView.as_view(), name='request_index'),
    path('requests/create/', RequestCreateView.as_view(), name='request_create'),
    path('requests/<int:pk>/', RequestDetailView.as_view(), name='request_details'),
    path('requests/<int:pk>/update/', RequestUpdateView.as_view(), name='request_update'),
    path('requests/<int:pk>/delete/', RequestDeleteView.as_view(), name='request_delete'),
    path('requests/<int:request_id>/approvals/', ApprovalListView.as_view(), name='approval_list'),
    path('approvals/<int:pk>/update/', ApprovalUpdateView.as_view(), name='approval_update'),
]