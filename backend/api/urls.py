from django.urls import path
from django.conf.urls import include
from .views import BoardView

boards = [
    path('', view=BoardView.as_view()),
]


urlpatterns = [
    path('boards/', include(boards)),
]
