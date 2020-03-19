from rest_framework import serializers
from recipe_app import models
from django.contrib.auth.models import User



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields =( 
            'name',
        )

class TechniqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Technique
        fields =(
            'technique_name',
        )

class KeyWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.KeyWord
        fields =(
            'keywords',
        )

class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ingredients
        fields =(
            'ingredients', 'id'
        )

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comments
        fields =(
            'comments',
        )


class RecipeSerializer(serializers.ModelSerializer):
    ingredient_info = IngredientsSerializer(many=True, read_only=True, source='ingredients')

    keyword_info = KeyWordSerializer(many=True, read_only=True, source='keywords')

    category_info = CategorySerializer(many=True, read_only=True, source='category')

    technique_info = TechniqueSerializer(many=True,read_only=True, source='technique')

    comments_info = CommentsSerializer(many=True, read_only=True, source='comments')

    class Meta:
        model = models.Recipe
        fields =(
            'id',
            'recipe_name',
            'category',
            'category_info',
            'technique',
            'technique_info',
            'keywords',
            'keyword_info',
            'prep_time',
            'ingredients',
            'ingredient_info',
            'picture',
            'body',
            'favorites',
            'comments',
            'comments_info',
            # 'favorites_info',
        )
        # depth = 1
class UserSerializer(serializers.ModelSerializer):
    favorites_info = RecipeSerializer(many=True,read_only=True, source='favorites')
    comments_info = RecipeSerializer(many=True,read_only=True, source='comments')
    class Meta:
        model = models.User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'favorites','favorites_info','comments','comments_info')