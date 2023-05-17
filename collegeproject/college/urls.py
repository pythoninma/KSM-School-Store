
from django.urls import path
from . import views
app_name='college'

urlpatterns = [

    path('',views.allStreamDept,name="allStreamDept"),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('form', views.form, name='form'),
    path('confirm', views.confirm, name='confirm'),
    path('<slug:c_slug>/',views.allStreamDept,name='streams_by_department'),
    path('<slug:c_slug>/<slug:stream_slug>/', views.streamDetail, name='streamDeptdetail')
]