from django.urls import path
from . import views

app_name = 'ccc'
urlpatterns = [
    path('', views.home, name="home"),
    path('about.html', views.about, name="about"),
    path('team.html', views.team, name="team"),
    path('portfolio.html', views.portfolio, name="portfolio"),
    path('recruitment.html', views.recruitment, name="recruitment"),
    path('services.html', views.services, name="services"),
    path('contact.html', views.contact, name="contact"),
    
]