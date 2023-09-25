from rest_framework import serializers
from todo.models.category import CategoryEntity

class CategorySerializer(serializers.ModelSerializer):
    tasks = serializers.SlugRelatedField(
        many = True,
        read_only = True,
        slug_field = 'name'
    )

    class Meta:
        model = CategoryEntity
        fields = ['id', 'name', 'description','tasks']