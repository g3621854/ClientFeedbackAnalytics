from rest_framework import serializers
from .models import KeyWordReviews
class KeyWordReviewsSerializers(serializers.Serializer):
    place_name = serializers.CharField
    date = serializers.DateField()
    keywords = serializers.CharField()
    keywordCount = serializers.IntegerField()
    category_choices = (
        (True, '好評'),
        (False, '負評')
    )
    # category = serializers.DictField()
    class Meta:
        model = KeyWordReviews
        fields = '__all__'