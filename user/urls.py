from django.urls import path
from . views import Registration_Form, Log_in_Form
from django.contrib.auth.views import LogoutView

app_name = 'user'

urlpatterns = [
    path('', Log_in_Form.as_view(), name='login'),
    path('register/', Registration_Form.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='user:login'), name='logout'),
]
