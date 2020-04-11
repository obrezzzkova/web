from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from blog.views import uploadImage

urlpatterns = [
    path('',views.main, name='main'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    # path('post/<int:pk>/upload', uploadImage, name='uploadImage'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
