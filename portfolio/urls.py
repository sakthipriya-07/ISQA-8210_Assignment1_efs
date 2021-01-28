from django.conf.urls import url
from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeDoneView

app_name = 'portfolio'
urlpatterns = [
    path('', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    path('customer_list', views.customer_list, name='customer_list'),
    path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('stock_list', views.stock_list, name='stock_list'),
    path('stock/create/', views.stock_new, name='stock_new'),
    path('stock/<int:pk>/edit/', views.stock_edit, name='stock_edit'),
    path('stock/<int:pk>/delete/', views.stock_delete, name='stock_delete'),
    path('investment/create/', views.investment_new, name='investment_new'),
    path('investment_list', views.investment_list, name='investment_list'),
    path('investment/<int:pk>/edit/', views.investment_edit, name='investment_edit'),
    path('investment/<int:pk>/delete/', views.investment_delete, name='investment_delete'),
    path('signup/', views.register, name='register'),
    path('login/password-reset/',
         auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'),
         name='password_reset'),
    path('reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='registration/password_success.html'),
         name='password_success'),
    path('reset/OA/set-password/', auth_views.PasswordResetView.as_view(template_name='registration/reset_confirm.html'), name='reset_confirm'),
    path('login/change-password/',
         auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html'),
         name='change_password'),
    path('password_change/done/',
         views.PasswordChangeDoneView.as_view(template_name='registration/password_success.html'),
         name='password_success'),
    path('mutual_list', views.mutual_list, name='mutual_list'),
    path('mutual/<int:pk>/edit/', views.mutual_edit, name='mutual_edit'),
    path('mutual/<int:pk>/delete/', views.mutual_delete, name='mutual_delete'),
    path('mutual/create/', views.mutual_new, name='mutual_new'),
    path('category/portfolio/', views.customer_portfolio, name='customer_portfolio'),
 ]
