from django.urls import path
from myapp.views import hello

urlpatterns = [
    # myapp/
    path('', hello, name='hello'),
    # myapp/<str:name>
    path('<str:name>', hello, name='hello_name'),
]
