from django.db.models import Model, CharField, IntegerField, DateField, ForeignKey, RESTRICT
from enum import Enum
from rest_framework import serializers

class Country(Model):
    country_id = IntegerField(primary_key=True)
    country_name = CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'countries'


class Role(Model):
    role_id = IntegerField(primary_key=True)
    name = CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'roles'


class User(Model):
    user_id = IntegerField(primary_key=True)
    first_name = CharField(max_length=45)
    last_name = CharField(max_length=45)
    email = CharField(max_length=45)
    password = CharField(max_length=256)
    role = ForeignKey(Role, on_delete=RESTRICT)

    class Meta:
        managed = False
        db_table = 'users'


class Vacation(Model):
    vacation_id = IntegerField(primary_key=True)
    country = ForeignKey(Country, on_delete=RESTRICT, db_column='country_id')
    description = CharField(max_length=400)
    start_date = DateField()
    end_date = DateField()
    price = IntegerField()
    image = CharField(max_length=400)

    class Meta:
        managed = False
        db_table = 'vacations'


class Like(Model):
    user_id = ForeignKey(User, on_delete=RESTRICT, db_column='user_id')
    vacation_id = ForeignKey(Vacation, on_delete=RESTRICT, db_column='vacation_id')

    class Meta:
        managed = False
        db_table = 'likes'


class RoleModel(Enum):
    Admin = 1
    User = 2


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class VacationsStats(Model):
    past_vacations = IntegerField(max_length=5)
    on_going_vacations = IntegerField(max_length=5)
    future_vacations = IntegerField(max_length=5)

    class Meta:
        managed = False

class VacationsStatsSerializer(serializers.ModelSerializer):

    class Meta:
        model = VacationsStats
        fields = '__all__'


class TotalUsers(Model):
    total_users = IntegerField(max_length=3)

    class Meta:
        managed = False

class TotalUsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = TotalUsers
        fields = '__all__'


class TotalLikes(Model):
    total_likes = IntegerField(max_length=5)

    class Meta:
        managed = False

class TotalLikesSerializer(serializers.ModelSerializer):

    class Meta:
        model = TotalLikes
        fields = '__all__'


class LikesSplit(Model):
    destination = CharField(max_length=20)
    likes = IntegerField(max_length=3)

    class Meta:
        managed = False

class LikesSplitSerializer(serializers.ModelSerializer):

    class Meta:
        model = LikesSplit
        fields = '__all__'

