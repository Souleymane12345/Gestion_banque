from django.urls import path , include
from . import views

app_name = 'banks'
urlpatterns = [
    path('', views.home , name='home'),
    path('acceuil/', views.acceuil , name='acceuil'),
    path('first_choice/', views.first_choice , name='first_choice'),
    path('creation_bank/', views.creation_bank , name='creation_bank'),
    path('connexion_bank/', views.connexion_bank , name='connexion_bank'),
    path('bank_menu/', views.bank_menu , name='bank_menu'),
    path('agent_menu/', views.agent_menu , name='agent_menu'),
    path('gestion_client/', views.gestion_client , name='gestion_client'),
    path('table_bank/', views.table_bank , name='table_bank'),
    path('connexion_agent/', views.connexion_agent , name='connexion_agent'),
    path('inscription_agents/', views.inscription_agents , name='inscription_agents'),
    path('inscription_users/', views.inscription_users , name='inscription_users'),
    path('connexion_users/', views.connexion_users , name='connexion_users'),
    path('suppression_users/', views.suppression_users , name='suppression_users'),
    
    path('/depot', views.depot , name='depot'),
    path('/retrait', views.retrait , name='retrait'),
    path('/transfert', views.transfert , name='transfert'),
    path('menu_users/', views.menu_users , name='menu_users'),
    
    
]
