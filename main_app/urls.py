from tkinter.font import names

from django.urls import path

from main_app import views, admin_views, donor_views, receiver_views
from main_app.donor_views import donor
from main_app.receiver_views import receiver_base

urlpatterns = [
    path('test',views.test,name='test'),
    path('dore', views.DonorR, name='DoRe'),
    path('Receive', views.Receive, name='Receive'),
    path('', views.index, name='index'),
    path('dash_index',views.index_dashboard,name='dash_index'),
    path('login', views.Login_view, name='login'),

#admin
    path('admin_base', admin_views.admin_base, name='admin_base'),

    path("read", admin_views.read, name='read'),
    path("delete/<int:id>/", admin_views.remove, name='delete'),
    path('update/<int:id>/', admin_views.update, name='update'),

    path("read1", admin_views.read1, name='read1'),
    path("delete1/<int:id>/", admin_views.remove1, name='delete1'),
    path('update1/<int:id>/', admin_views.update1, name='update1'),

    path('table',admin_views.table_request,name='table'),

    path('dndr',admin_views.donation_request,name='dndr'),
    path('accept/<int:id>/',admin_views.accept,name='accept'),
    path('reject/<int:id>/', admin_views.reject, name='reject'),
    path('view',admin_views.accept_view,name='view'),
    path('adfdv',admin_views.adfdv,name='adfdv'),
    path('Replay/<int:id>/',admin_views.replay_feedback,name="Replay"),
    path('logou', admin_views.logou, name='logou'),

    #donor
    path('donor_base',donor_views.donor,name='donor_base'),
    path('donorre',donor_views.donor_request,name='donorre'),
    path('donate/<int:id>/', donor_views.donate, name='donate'),
    path('donation',donor_views.donation,name='donation'),
    path('profile', donor_views.profile, name='profile'),
    path('donor_update/<int:id>/', donor_views.donor_update, name='donor_update'),
    path('logou',donor_views.logou,name='logou'),

    #receiver
    path('receiver_base',receiver_views.receiver_base,name='receiver_base'),
    path('request',receiver_views.Request,name='request'),
    path('req',receiver_views.re_request,name='req'),
    path("delete_request/<int:id>/", receiver_views.delete_request,name='delete_request'),
    path('feedback',receiver_views.feedback,name='feedback'),
    path('feedview',receiver_views.fdbv,name='feedview'),
    path('mypro', receiver_views.mypro, name='mypro'),
    path('receiver_update/<int:id>/', receiver_views.receiver_update, name='receiver_update'),
    path('logou',receiver_views.logou,name='logou'),
    path('donor_view',receiver_views.donor_view,name='donor_view')

]
