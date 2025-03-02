from django.contrib import admin
from django.urls import path
from main.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', hello_world),
    path('today/', today_view),
    path('talabalar/', talabalar_view),
    path('talabalar/<int:talaba_id>/', talaba_details_view),
    path('mualliflar/', mualliflar_view),
    path('', home_view),
    path('mualliflar/<int:muallif_id>/', muallif_details_view),
    path('kitoblar/', kitoblar_view),
    path('recordlar/', recordlar_view),
    path('top3-kitoblar/', top3_kitoblar_view)





]
