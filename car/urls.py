from django.urls import path
from . import views

app_name = 'car'
urlpatterns = [
    path('t', views.treatment, name="t"),
    path('treatments', views.treatments, name="treatments"),
    path('charts', views.charts, name="charts")
]
