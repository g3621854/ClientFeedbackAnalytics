from rest_framework import serializers
from .models import KeyWordReviews
class KeyWordReviewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = KeyWordReviews
        fields = ["place_name", "date", "keywords", "keywordCount"]