from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Comment
from .serializers import CommentSerializer
# Create your views here.



class CommentList(APIView):
    """
    This CommentList class is used to allow a front-end users to easily identify and manipulate a list of comments in
    my current MySQL database.
    """
    def get_All(self, request):
        """
        Get all the comments in the current list of comments.
        :param request: Comes from the client.
        :return: The list of songs.
        """
        comment = Comment.objects.all()
        # Converts all objects into JSON
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Creates a comment object with input from client.
        :param request: Comes from client.
        :return: Will return a comment object to push into the database.
        """
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(APIView):
    """
    This CommentDetail class is used to allow a front-end users to easily identify and manipulate specific
     comments in a list of comments contained in my current MySQL database.
    """

    def get_Comment(self, pk):
        """
        Allows you to search for a comment contained in the current MySQL database containing all the comment objects.
        :param pk: Given by the client.
        :return: The specific details of a comment in a comment object.
        """
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        comment = self.get_Comment(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Allows you to update a specific object inside of the current list of comment objects thats contained in the
        MySQL database.
        :param request:Taken in from the client.
        :param pk: The specific comment that the client wants to manipulate. (It's location.)
        :return: The updated comment object.
        """
        comment = self.get_Comment(pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update_likes(self, request, pk):
        """
        Can be used to isolate any specific attribute inside of comment. In this case, it's being
        used to isolate the number of likes inside of the current comment model being viewed.
        :param request: Taken in from the client.
        :param pk: The specific comment that the client wants to manipulate. (It's location.)
        :return: The updated comment object.
        """
        comment = self.get_Comment(pk)
        comment.like += 1
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update_dislikes(self, request, pk):
        """
        Can be used to isolate any specific attribute inside of comment. In this case, it's being
        used to isolate the number of likes inside of the current comment model being viewed.
        :param request: Taken in from the client.
        :param pk: The specific comment that the client wants to manipulate. (It's location.)
        :return: The updated comment object.
        """
        comment = self.get_Comment(pk)
        comment.dislike += 1
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Deletes the comment that is searched by the client wanting to delete it.
        :param request: Taken in from the client.
        :param pk: The specific comment that the client wants to manipulate (It's location)
        :return: A response to the client stating that there is no content.
        """
        comment = self.get_Comment(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)