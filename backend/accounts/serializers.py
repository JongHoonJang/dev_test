from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'user_id',
            'password',
            'name',
            "department",
        )
    def create(self,validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None :
        #provide django, password will be hashing!
            instance.set_password(password)
            instance.save()
            return instance