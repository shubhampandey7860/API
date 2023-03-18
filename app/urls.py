from django .urls import path
from .views import *
urlpatterns = [
    path('course-list/',CourseList),
    path('course-detail/<str:pk>',CourseDetail,name='detail'),
    path('course-create/',CourseCreate,name='CourseCreate'),
    path('course-update/<str:pk>',CourseUpdate,name='course-update'),
    path('course-delete/<str:pk>',CourseDelete,name='course-delete'),
    
    path('',apiOverview,name='apiOverview'),
]
