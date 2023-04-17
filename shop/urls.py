from django.urls import path

from . import views

urlpatterns = [
    path("chart/filter-options/",views.get_filter_options, name="chart_filter_options"),
    path("chart/sales/<int:year>/",views.get_sales_chart, name="chart_sales"),
    path("chart/spend_per_customer/<int:year>/",views.spend_per_customer_chart , name="chart_spend_per_customer"),
    path("chart/payment_success/<int:year>/",views.payment_success_chart , name="chart_payment_success"),
    path("chart/payment_method/<int:year>/",views.payment_method_chart , name="chart_payment_method"),
]