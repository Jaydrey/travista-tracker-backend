from rest_framework import  serializers
from .models import Business

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = (
            "bsn_id",
            "business_name",
            "business_email",
            "google_business",
            "user_id",
            "shop_address",
            "created_at",
        )

class BusinessRegistrationSerializer(serializers.Serializer):
    business_name = serializers.CharField(max_length=100)
    business_email = serializers.CharField(max_length=100)
    google_business = serializers.CharField(allow_blank=True, max_length=100)
    shop_address = serializers.CharField(max_length=100, allow_blank=True)
    user_id = serializers.IntegerField()