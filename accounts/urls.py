from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('dashboard/', TemplateView.as_view(template_name='accounts/dashboard.html'), name='dashboard'),
    path('order-summary/', TemplateView.as_view(template_name='accounts/order-summary.html'), name='order-summary'),
    path('settings/', TemplateView.as_view(template_name='accounts/settings.html'), name='settings'),
    path('order/<int:id>/', TemplateView.as_view(template_name='accounts/order-details.html')),
    path('wishlist/', TemplateView.as_view(template_name='accounts/wishlist.html'), name='wishlist'),
    path('cart/', TemplateView.as_view(template_name='accounts/cart.html'), name='cart'),
    path('checkout/', TemplateView.as_view(template_name='accounts/checkout.html'), name='checkout')

]