from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('about', views.about, name = "about"),
    path('aim', views.aim, name = "aim"),
    path('admission', views.admission, name = "admission"),
    path('book_list', views.book_list, name = "book_list"),
    path('co_curriculum', views.co_curriculum, name = "co_curriculum"),
    path('curriculum', views.curriculum, name = "curriculum"),
    path('contact', views.contact, name = "contact"),
    path('exam', views.exam, name = "exam"),
    path('facilities', views.facilities, name = "facilities"),
    path('faculty', views.faculty, name = "faculty"),
    path('fee', views.fee, name = "fee"),
    path('gallery', views.gallery, name = "gallery"),
    path('holiday_list', views.holiday_list, name = "holiday_list"),
    path('infrastructure', views.infrastructure, name = "infrastructure"),
    path('message', views.message, name = "message"),
    path('notice', views.notice, name = "notice"),
    path('public_disclosure', views.public_disclosure, name = "public_disclosure"),
    path('rules', views.rules, name = "rules"),
    path('strength', views.strength, name = "strength"),
    path('syllabus', views.syllabus, name = "syllabus"),

]
