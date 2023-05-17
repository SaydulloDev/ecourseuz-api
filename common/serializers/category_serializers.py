from rest_framework import serializers

from common.models import Category


class CategoryListSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)

    class Meta:
        model = Category
        fields = '__all__'