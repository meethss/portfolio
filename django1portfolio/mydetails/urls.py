from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home, name="home"),
    path('education/',views.Education, name="education"),
    path('certificate/',views.Certificate, name="certificate"),
    path('project/',views.Project, name="project"),
    path('experience/',views.Experience, name="experience"),
]
