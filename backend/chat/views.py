from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.
from django.contrib.auth import get_user_model
from chat.serializers import UserGetSerializer
from  rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

@api_view(['GET'])
def get_user_list(request):
    try:
        user_obj = User.objects.exclude(id=request.user.id)
        serializer = UserGetSerializer(user_obj, many=True)
        return Response(serializer.data)
    except Exception as e:
        print("Error in getting users list", str(e))
        return Response({"error" : "Error in getting users list"}, staus=400)
    

        