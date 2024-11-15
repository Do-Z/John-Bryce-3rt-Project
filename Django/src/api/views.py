from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Like, TotalLikesSerializer, User, RoleModel, UserSerializer, Vacation, VacationsStatsSerializer, TotalUsersSerializer, LikesSplitSerializer
from validate_email_address import validate_email
from .cyber import Cyber
from django.utils import timezone

@api_view(['POST'])
def log_in(request):
    try:
        if request.method == 'POST':
            email = request.data.get('email')
            password = request.data.get('password')

            if not email:
                return Response({'error':'missing email'}, status=status.HTTP_400_BAD_REQUEST)
            if not password:
                return Response({'error':'missing password'}, status=status.HTTP_400_BAD_REQUEST)
            if not validate_email(email):
                return Response({'error':'invalid email'}, status=status.HTTP_400_BAD_REQUEST)
            user = User.objects.get(email = email)
            if user is None:
                return Response({'error':'incorrect email or password'}, status=status.HTTP_401_UNAUTHORIZED)
            hashed_password = Cyber.hash(password)
            if hashed_password != user.password:
                return Response({'error':'incorrect email or password'}, status=status.HTTP_401_UNAUTHORIZED)
            if user.role_id != RoleModel.Admin.value:
                return Response({'error':'you are not authorized'}, status=status.HTTP_403_FORBIDDEN)
            request.session["is_logged_in"] = True
            serializer = UserSerializer(user)
            return Response(serializer.data)
    except User.DoesNotExist:
        return Response ({'error':'user does not exist'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as err:
        return Response ({'error':str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def log_out(request):
    try:
        if ("is_logged_in" in request.session) == False:
            return Response({"error":"you are not logged in"}, status=status.HTTP_401_UNAUTHORIZED)
        request.session.flush()
        return Response({"message":"logged out successfully"}, status=status.HTTP_200_OK)
    except Exception as err:
        return Response ({'error':str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['GET'])
def get_vacations_stats(request):
    try:
        if("is_logged_in" in request.session) == False:
            return Response({"error":"you are not logged in"}, status=status.HTTP_401_UNAUTHORIZED)
        past_vacations = Vacation.objects.filter(end_date__lt=timezone.now()).count()
        on_going_vacations = Vacation.objects.filter(start_date__lte=timezone.now(), end_date__gte=timezone.now()).count()
        future_vacations = Vacation.objects.filter(start_date__gt=timezone.now()).count()        

        vacations_stats = {
            "past_vacations": past_vacations,
            "on_going_vacations": on_going_vacations,
            "future_vacations": future_vacations
        }
        serializer = VacationsStatsSerializer(vacations_stats)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    except Exception as err:
        return Response ({'error':str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_total_users(request):
    try:
        if("is_logged_in" in request.session) == False:
            return Response({"error":"you are not logged in"}, status=status.HTTP_401_UNAUTHORIZED)
        total_users = User.objects.count()
        serializer = TotalUsersSerializer({"total_users": total_users})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    except Exception as err:
        return Response ({'error':str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['GET'])
def get_total_likes(request):
    try:
        if("is_logged_in" in request.session) == False:
            return Response({"error":"you are not logged in"}, status=status.HTTP_401_UNAUTHORIZED)
        total_likes = Like.objects.count()
        serializer = TotalLikesSerializer({"total_likes": total_likes})
        return Response (serializer.data, status=status.HTTP_200_OK)
    
    except Exception as err:
        return Response ({'error':str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['GET'])
def get_likes_split(request):
    try:
        if("is_logged_in" in request.session) == False:
            return Response ({"error":"you are not logged in"}, status=status.HTTP_401_UNAUTHORIZED)
        vacations = Vacation.objects.values('vacation_id', 'country__country_name')
        likes_data = []
        for vacation in vacations:
            likes_count = Like.objects.filter(vacation_id = vacation["vacation_id"]).count()
            likes_data.append({
                "country":vacation["country__country_name"],
                "likes":likes_count
            })
        likes_split = {}
        for vacation in likes_data:
            country_name = vacation["country"]
            total_likes = vacation["likes"]
            if country_name in likes_split:
                likes_split[country_name] += total_likes
            else:
                likes_split[country_name] = total_likes
            
        likes_per_country = [{'destination':country, 'likes':likes}for country, likes in likes_split.items()]
        serializer = LikesSplitSerializer(likes_per_country, many=True)
        return Response (serializer.data, status=status.HTTP_200_OK)

    except Exception as err:
        return Response ({'error':str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
     