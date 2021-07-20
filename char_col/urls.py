from django.urls import path

from . import views

urlpatterns = [
    path('', views.characters_index, name='index'),
    path('characters/<int:character_id>/', views.character_detail, name='detail'),
    path('characters/create/', views.CharacterCreate.as_view(), name='create'),
    path('characters/<int:pk>/update/', views.CharacterUpdate.as_view(), name='update'),
    path('characters/<int:pk>/delete/', views.CharacterDelete.as_view(), name='delete'),
    path('characters/<int:character_id>/add_campaign', views.add_campaign, name='add_campaign'),
    path('abilities/', views.AbilityList.as_view(), name='ability_index'),
    path('abilities/create/', views.AbilityCreate.as_view(), name='ability_create'),
    path('abilities/<int:pk>/', views.AbilityDetail.as_view(), name='ability_detail'),
    path('abilities/<int:pk>/update/', views.AbilityUpdate.as_view(), name='ability_update'),
    path('abilities/<int:pk>/delete/', views.AbilityDelete.as_view(), name='ability_delete'),
    path('characters/<int:character_id>/add_ability/<int:ability_id>/', views.add_ability, name='add_ability'),
    path('characters/<int:character_id>/remove_ability/<int:ability_id>/', views.remove_ability, name='remove_ability'),
]