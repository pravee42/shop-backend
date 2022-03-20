from django.urls import path
from . import views

urlpatterns = [
    path("product/<str:pk>/", views.ProductView.as_view()),
    path("product/detail/<str:tk>/<str:pk>/",
         views.ProductDetailView.as_view()),
    path("bill/<str:pk>/", views.BillView.as_view()),
    path("bill/detail/<str:tk>/<str:pk>/",
         views.BillDetailView.as_view()),
    path("billtotal/<str:pk>/", views.TotalBillView.as_view()),
    path("billtotal/detail/<str:tk>/<str:pk>/",
         views.TotalBillDetailView.as_view()),
    path("service/<str:pk>/", views.ServiceView.as_view()),
    path("service/detail/<str:tk>/<str:pk>/",
         views.ServiceDetailView.as_view()),
    path("servicetotal/<str:pk>/", views.TotalServiceView.as_view()),
    path("servicetotal/detail/<str:tk>/<str:pk>/",
         views.TotalServiceDetailView.as_view()),
    path("cih/<str:pk>/", views.CashinHandView.as_view()),
    path("cih/detail/<str:tk>/<str:pk>/",
         views.CashinHandDetailView.as_view()),
]
