from rest_framework import serializers

from .models import Element,Category,Type
from comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    
    count = serializers.SerializerMethodField() #devuelve el numero de comentarios de cada elemento y lo coge del mentodo get_count

    class Meta:
        model= Comment
        fields = '__all__'
    
    def get_count(self, obj):
        return Comment.objects.filter(element_id= obj.element_id).count()



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields = '__all__'



class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Type
        fields = '__all__'

class ElementSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    type = TypeSerializer(read_only=True)
    comment_count = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True,read_only=True)
    class Meta:
        model= Element
        fields = '__all__'

    def get_comment_count(self,obj):
        return Comment.objects.filter(element_id=obj.id).count()