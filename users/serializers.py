from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
   
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'password', 'token', 'role')

    # def create(self, validated_data):
    #     return User.objects.create_user(**validated_data)


# class LoginSerializer(serializers.Serializer):

# #     # def login(request):
# #     #     email = request.POST['email']
# #     #     password = request.POST['password']
# #     #     user = authenticate(email=email, password=password)
# #     #     if user is not None and user.is_active:
# #     #         login(request, user)
# #     #         return HttpResponseRedirect("/users/profile/")


#     email = serializers.CharField(max_length=255)
#     username = serializers.CharField(max_length=255, read_only=True)
#     password = serializers.CharField(max_length=128, write_only=True)
#     token = serializers.CharField(max_length=255, read_only=True)

#     def validate(self, data):
#         email = data.get('email', None)
#         password = data.get('password', None)
        
#         if email is None:
#             raise serializers.ValidationError(
#                 'An email address is required to log in.'
#             )

#         if password is None:
#             raise serializers.ValidationError(
#                 'A password is required to log in.'
#             )

#         user = authenticate(username=email, password=password)
#         # user = User.objects.get(email=email, password=password)

#         if user is None:
#             raise serializers.ValidationError(
#                 'A user with this email and password was not found.'
#             )

#         if not user.is_active:
#             raise serializers.ValidationError(
#                 'This user has been deactivated.'
#             )

#         return {
#             'email': user.email,
#             'username': user.username,
#             'token': user.token
#         }