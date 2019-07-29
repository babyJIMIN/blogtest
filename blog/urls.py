from django.contrib import admin
from django.urls import path, include
import blogapp.views
import accounts.views
import portfolio.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name = 'home'),
    path('blog/', include('blogapp.urls')),
    path('accounts/', include('accounts.urls')),
    path('portfolio/', portfolio.views.portfolio, name = 'portfolio'),
]
