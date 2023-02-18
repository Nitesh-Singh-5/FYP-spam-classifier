from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('', views.Add_To_Feedback.as_view(), name='add_to_feedback'),
    path('recent_messages/', views.RecentMessages, name='recent_messages'),
    path('generate_message/', views.GenerateMessages, name='generate_message'),
]