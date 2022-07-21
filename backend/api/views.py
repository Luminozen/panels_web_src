from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
import rest_framework.status as status

from .json_DB import BOARDS
from .utils import call_stored_function, call_stored_procedure

from datetime import datetime
import time

class BoardView(APIView):

    def get(self, request):
        f_args = {
            'board_id': request.GET.get('board_id')
        }
        
        boards = call_stored_function('boards.get_board', 'default', True if f_args.get('board_id') else False, *f_args.values())
        return Response(boards, status=status.HTTP_200_OK)

    def post(self, request):
        # 1. Вот это в f_args засунуть напоминаю что это словарь ключ:значение
        f_args = {
            'name': str(request.data.get('board_name')) ,
            'description': str(request.data.get('board_description')),
            'id_busstop_yandex': int(request.data.get('id_busstop_yandex')),
            'id_tramstop_yandex': int(request.data.get('id_tramstop_yandex')),
            'zabbix_node_name': str(request.data.get('zabbix_node_name')),
            'id_busstop_pikas': int(request.data.get('id_busstop_pikas')),
            'id_tramstop_pikas': int(request.data.get('id_tramstop_pikas')),
            'datatime_update_pikas': datetime.now(),
            'boards_data': str(request.data.get('boards_data')),
        }

        result = call_stored_procedure('boards.add_board', 'default', *f_args.values())
        print(result)
        return Response(result, status=status.HTTP_201_CREATED)

        # Добавить дополнительный board в массив BOARDS

    def put(self, request):
        # 1. Параметры из запроса в f_args засунуть напоминаю что это словарь ключ:значение
        f_args = {
            'board_id': int(request.data.get('board_id')) ,
            'board_name': str(request.data.get('board_name')) ,
            'description': str(request.data.get('board_description')),
            'id_busstop_yandex': int(request.data.get('id_busstop_yandex')),
            'id_tramstop_yandex': int(request.data.get('id_tramstop_yandex')),
            'zabbix_node_name': str(request.data.get('zabbix_node_name')),
            'id_busstop_pikas': int(request.data.get('id_busstop_pikas')),
            'id_tramstop_pikas': int(request.data.get('id_tramstop_pikas')),
            'datatime_update_pikas': datetime.now(),
            'boards_data': str(request.data.get('boards_data')),
        }
        result = call_stored_procedure('boards.update_board', 'default', *f_args.values())
        return Response(result, status=status.HTTP_200_OK)

    def delete(self, request):
        f_args = {
            'board_id': int(request.data.get('board_id')),
        }
        result = call_stored_procedure('boards.remove_board', 'default', *f_args.values())
        return Response(result, status=status.HTTP_200_OK)
        


