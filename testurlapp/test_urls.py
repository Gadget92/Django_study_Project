from django.conf.urls import url
from testurlapp import views

urlpatterns = [
    # url('', views.home, name='home'),
    url('user/<int>', views.home2, name='home'),
    url('user/<int:month>/<int:year>', views.home2, name='home'),

]

