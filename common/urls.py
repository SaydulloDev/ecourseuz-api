from django.urls import path

from common.views import ApplicationFormView, AboutUsListApiViews, CategoryListApiViews, ContactUsListApiView, ContactFormListApiView, BlogList, BlogDetail

urlpatterns = [
    path('blogs/', BlogList.as_view(), name='blog-list'),
    path('blogs/<int:pk>/', BlogDetail.as_view(), name='blog-detail'),
    path('application-form/', ApplicationFormView.as_view(), name='application-form'),
    path('category/', CategoryListApiViews.as_view(), name='category-list'),
    path('about-us/',AboutUsListApiViews.as_view(), name='about-us')
    path('contact/', ContactUsListApiView.as_view(), name='contact-us'),
    path('contact-form/', ContactFormListApiView.as_view(), name='contact-form')
]
