from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from .json_DB import BOARDS


class BoardView(APIView):

    def get(self, request):
        board_id = request.GET.get('board_id')
        if board_id:
            for board in BOARDS:
                if board.get('id') == board_id:
                    return Response(board)
            return Response({'message': 'board with current id does not exist'})
        return Response(BOARDS)

    def post(self, request):
        board_data = dict(
            board_id=request.data.get('board_id'),
            name=request.data.get('name'),
            description=request.data.get('description'),
            id_busstop_yandex=request.data.get('id_busstop_yandex'),
            id_tramstop_yandex=request.data.get('id_tramstop_yandex'),
            zabbix_node_name=request.data.get('zabbix_node_name'),
            id_busstop_pikas=request.data.get('id_busstop_pikas'),
            id_tramstop_pikas=request.data.get('id_tramstop_pikas'),
            boards_data=request.data.get('boards_data'),
            datatime_update_pikas=request.data.get('datatime_update_pikas'))

        BOARDS.append(board_data)

        return Response({'message': 'board with id {} created'.format(board_data.get('board_id'))})

        # Добавить дополнительный board в массив BOARDS

    def put(self, request):
        board_id = request.data.get('board_id')
        name = board_id = request.data.get('name')
        if board_id:
            for board in BOARDS:
                if board.get('id') == board_id:
                    board['name'] = name
                    return Response({'message': 'board with id updated'.format(board_id)})
            return Response({'message': 'board with id does not exist'})
        return Response({'message': 'board with id does not exist'})

    def delete(self, request):
        print(request.data)
        board_id = request.data.get('board_id')
        
