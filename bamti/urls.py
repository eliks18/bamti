"""bamti URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from users import views as usr_views
from customers import views as cstmr_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(usr_views.welcome), name='welcome'),
    path('register/', usr_views.register),
    path('accounts/login/', usr_views.login),
    path('logout/', login_required(usr_views.logout)),

    path('customers/create', login_required(cstmr_views.create), name='customer.create'),
    path('customers/validate_customer_type', login_required(cstmr_views.validate_customer_type), name='customers.validate_customer_type'),

    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
