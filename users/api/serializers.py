from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    """serializando un objeto usuario"""
    class Meta:
        model = User
        fields = ('email', 'password', 'user_name')
        extra_kwargs = {'password':{'write_only': True, 'min_length': 5}}