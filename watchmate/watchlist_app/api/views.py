from rest_framework import status
from rest_framework.response import Response

from .serializers import moviesserializers

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from ..models import movies

"""  CLASS BASED VIEWS  """


class Movie_List(APIView):
    def get(self):
        movie = movies.objects.all()
        seria = moviesserializers(movie, many=True)
        return Response(seria.data)

    def post(self,request):
        serializer=moviesserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class movie_details(APIView):
    def get(self,request):
        try:
            mvie = movies.objects.get(pk=pk)
        except movies.DoesNotExist:
            return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = moviesserializers(mvie)
        return Response(serializer.data)

    def put(self,request):
        serializer = moviesserializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)

    def delete(self,request):
        moive1 = movies.objects.get(pk=pk)
        moive1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



"""  FUNCTION BASED VIEWS  """
# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movie = movies.objects.all()
#         serilizer = moviesserializers(movie, many=True)
#         return Response(serilizer.data)
#
#     if request.method == 'POST':
#         serializer = moviesserializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):
#     if request.method == 'GET':
#         try:
#             mvie = movies.objects.get(pk=pk)
#         except movies.DoesNotExist:
#             return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = moviesserializers(mvie)
#         return Response(serializer.data)
#
#     if request.method == 'PUT':
#         serializer = moviesserializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'DELETE':
#         moive1 = movies.objects.get(pk=pk)
#         moive1.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
