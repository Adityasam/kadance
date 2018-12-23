from django.urls import path
from . import views

app_name="main"

urlpatterns = [
    path('', views.home, name="home"),
    path('centers/',views.centers,name="centers"),
    path('admin_page/',views.admin_page,name="admin_page"),
    path('add_data/<center_id>',views.add_data,name="add_data"),
    path('update_data/<cid>', views.update_data,name="update_data"),
    path('del_data/<cid>',views.del_data,name="del_data"),
    path('admin_login',views.admin_login,name="admin_login"),
    path('logout/',views.logouts,name="logout"),
    path('add_center_data/<center_id>',views.add_center_data,name="add_center_data"),
    path('update_center/<did>',views.update_center,name="update_center"),
    path('detail/<center_id>',views.detail,name="detail"),
    path('center_detail/<center_id>',views.center_detail,name='center_detail'),
    path('mark/<mid>',views.mark,name='mark'),
    path('transfer/<tid>',views.transfer,name='transfer'),
    path('damaged/<tid>',views.damaged,name="damaged"),
    path('tobe/',views.tobe,name="tobe"),
    path('mark_received/<tid>',views.mark_received,name="mark_received"),
    path('transfer_tab/',views.transfer_tab,name="transfer_tab"),
    path('transfer_from_center/<tid>/<cid>',views.transfer_from_center,name="transfer_from_center"),
    path('orignal_home/',views.orignal_home,name='orignal_home'),
]
