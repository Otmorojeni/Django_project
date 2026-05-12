from django.urls import path
from . import views


urlpatterns = [
    path('themes/', views.theme_list, name='theme-list'),
    path('themes/<int:pk>/', views.theme_detail, name='theme-detail'),
    path('kits/', views.KitListCreateView.as_view(), name='kit-list'),
    path('kits/<int:pk>/', views.KitDetailView.as_view(), name='kit-detail'),
    path('brands/', views.BrandListCreateView.as_view(), name='brand-list'),
    path('brands/<int:pk>/', views.BrandDetailView.as_view(), name='brand-detail'),
    path('reviews/', views.ReviewList.as_view(), name='review-list'),
    path('reviews/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),
    path('kits/<int:kit_id>/reviews/', views.ReviewList.as_view(), name='kit_review')
]