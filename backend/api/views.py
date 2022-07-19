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

        for v in f_args.values():
            print(type(v))

        # 2. Здеся вызываем хранимку add_board через call_stored_procedure - она ничего не вернет вам поэтому если выполнилась
        # то и бог с ней а если вернет то это в ответ пихаем
        """
        CREATE OR REPLACE PROCEDURE boards.add_board(
            IN p_board_name character varying,
            IN p_description character varying,
            IN p_id_bussstop_yandex integer,
            IN p_id_tramstop_yandex integer,
            IN p_zabbix_node_name character varying,
            IN p_id_busstop_pikas integer,
            IN p_id_tramstop_pikas integer,
            IN p_datetime_update_pikas timestamp without time zone,
            IN p_boards_data character varying)
        LANGUAGE 'plpgsql'
        """
        result = call_stored_procedure('boards.add_board', 'default', *f_args.values())
        print(result)
        return Response({'message': 'board with id {} created'.format(f_args.get('board_id'))}, status=status.HTTP_201_CREATED)

        # Добавить дополнительный board в массив BOARDS

    def put(self, request):
        # 1. Параметры из запроса в f_args засунуть напоминаю что это словарь ключ:значение
        pass
        # 2. Здеся вызываем хранимку update_board через call_stored_procedure - она ничего не вернет вам поэтому если выполнилась
        # то и бог с ней а если вернет то это в ответ пихаем
        """
        CREATE OR REPLACE PROCEDURE boards.update_board(
        	IN p_board_id integer,
        	IN p_board_name character varying,
        	IN p_description character varying,
        	IN p_id_bussstop_yandex integer,
        	IN p_id_tramstop_yandex integer,
        	IN p_zabbix_node_name character varying,
        	IN p_id_busstop_pikas integer,
        	IN p_id_tramstop_pikas integer,
        	IN p_datetime_update_pikas timestamp without time zone,
        	IN p_boards_data character varying)
        LANGUAGE 'plpgsql'
        """
        pass
        return Response({'message': 'board with id does not exist'}, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request):
        # Пока не делоем
        return Response({'message': 'board with id does not exist'}, status=status.HTTP_204_NO_CONTENT)
        


