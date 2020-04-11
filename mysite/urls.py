from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib.auth import views
from blog.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/register/', register, name = 'register'),
    path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    path('', include('blog.urls')),
    # path('static/images', uploadImage, name='uploadImage'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
