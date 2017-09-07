from django.shortcuts import render
from rest_framework import viewsets
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status

from jsframework.models import Todo
from serializers import TodoSerializer


# Todos routes automatically generated
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def list(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            queryset = Todo.objects.filter(user__pk=request.user.pk)
            print 'I am here'
        else:
            queryset = Todo.objects.filter(session=request.COOKIES['sessionid'])
            print 'I am there'
        queryset = self.filter_queryset(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data
        if request.user.is_authenticated():
            data['user_id'] = request.user.pk
        else:
            data['session'] = request.COOKIES.get('sessionid', None)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

def index(request):
    return render(request, 'jsframework/base.html')
