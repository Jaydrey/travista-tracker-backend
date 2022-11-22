from django.db import models
from django.utils import timezone
import uuid
# Create your models here.

class Business(models.Model):
    class Meta:
        ordering = ["business_name"]
    bsn_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    business_name = models.CharField(max_length=250, help_text="business_name")
    business_email = models.EmailField(max_length=250, help_text="business_email")
    google_business = models.CharField(max_length=100, blank=True, null=True)
    user_id = models.UUIDField()
    # user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    shop_address = models.CharField(max_length=500,blank=True)
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self) -> str:
        return self.business_name
