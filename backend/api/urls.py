from django.urls import path
from django.conf.urls import include
from .views import BoardView

boards = [
    path('list/', view=BoardView.as_view()),
]

# board_messages = [
#     path('list/', view=BoardMessageView.as_view()),
# ] 

urlpatterns = [
    path('boards/', include(boards)),
    path('board_messages/', include(board_messages)),
]

# {'message': 'board message'}