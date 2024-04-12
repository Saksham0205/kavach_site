from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)


    def create(Self, validated_data):
        user = get_user_model().objects.create_user(
            email = validated_data['email'],
            password = validated_data['password'],
            first_name = validated_data.get('first_name', ""),
            last_name = validated_data.get('last_name', "")
        )
        return user
    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    id = serializers.CharField(max_length=15,read_only=True)
    password = serializers.CharField(max_length=255, write_only=True)
    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)

        if email is None:
            raise serializers.ValidationError({"errors": "Please provide an email address."})
        
        if password is None:
            raise serializers.ValidationError({"errors":"Please provide a password."})
        user = authenticate(username=email, password = password)

        if user is None:
            raise serializers.ValidationError(
                "Invalid Email or Password"
            )
        if not user.is_active:
            raise serializers.ValidationError(
                "User is Incactive"
            )
        return{
            "email": user.email,
            "id" : user.id
        }
