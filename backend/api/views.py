from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
import rest_framework.status as status

from .json_DB import BOARDS


class BoardView(APIView):

    def get(self, request):
        board_id = request.GET.get('board_id')
        if board_id:
            for board in BOARDS:
                if board.get('id') == board_id:
                    return Response(board, status=status.HTTP_200_OK)
            return Response({'message': 'board with current id does not exist'}, status=status.HTTP_204_NO_CONTENT)
        return Response(BOARDS, status=status.HTTP_200_OK)

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

        return Response({'message': 'board with id {} created'.format(board_data.get('board_id'))}, status=status.HTTP_201_CREATED)

        # Добавить дополнительный board в массив BOARDS

    def put(self, request):
        board_id = request.data.get('board_id')
        name = board_id = request.data.get('name')
        if board_id:
            # При обходе по циклу в board попадает ссылка на очередной объект из BOARDS
            for board in BOARDS:
                if board.get('id') == board_id:
                    board['name'] = name
                    return Response({'message': 'board with id updated'.format(board_id)}, status=status.HTTP_200_OK)
            return Response({'message': 'board with id does not exist'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message': 'board with id does not exist'}, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request):
        print(request.data)
        board_id = request.data.get('board_id')
        if board_id:
            for index in range(len(BOARDS)):
                if BOARDS[index].get(board_id) == board_id:
                    del BOARDS[index]
                    return Response({'message': f'board with id: {board_id} deleted'}, status=status.HTTP_200_OK)
            return Response({'message': 'board with id does not exist'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message': 'board with id does not exist'}, status=status.HTTP_204_NO_CONTENT)
        
