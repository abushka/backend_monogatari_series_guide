from .models import CustomUser
from dj_rest_auth.serializers import UserDetailsSerializer

class CustomUserSerializer(UserDetailsSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'github_account', 'image', 'date_joined', 'language', 'is_active', 'last_login', 'is_staff', 'is_superuser',)
