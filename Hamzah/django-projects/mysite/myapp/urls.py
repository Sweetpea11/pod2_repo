from django.urls import path
from myapp.views import hello
from myapp.views import goodbye

urlpatterns = [
    #myapp/
    path('', hello, name='hello'),
    # myapp/<str:name>
    path('<str:name>', hello, name='hello_name'),
]   
urlpatterns = [
    path('goodbye/', goodbye, name='see you later,'),
    path('goodbye/<str:name>', goodbye, name='see_you_later_name'),
]
