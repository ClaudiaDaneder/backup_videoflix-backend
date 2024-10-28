from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import include, path
from content.views import CategoriesView, VideoViewSet
from customers.views import ActivateAccountView, EmailCheck, LoginView, LogoutView, RegisterView, UsernameCheck, run_migrate


router = DefaultRouter()
router.register(r'content', VideoViewSet, basename='video')

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('django-rq/', include('django_rq.urls')),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('register/', RegisterView.as_view()),
    path('categories/', CategoriesView.as_view()),
    path('', include(router.urls)),
    path('password_reset/', include('django_rest_passwordreset.urls')),
    path('activate/', ActivateAccountView.as_view()),
    path('check_username/', UsernameCheck.as_view()),
    path('check_email/', EmailCheck.as_view()),
    path('run-migrate/', run_migrate),
] 


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
