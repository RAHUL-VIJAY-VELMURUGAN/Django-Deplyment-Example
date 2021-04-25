from django.urls import path
from basic_app import views

# Template tagging --> should do the below
app_name = 'basic_app'

urlpatterns = [
    path('',views.basic_app_home_page,name = "basic_app_home_page"),
    path('relative/',views.relative,name = 'relative'),
    path('other/',views.other, name ='other'),
]
