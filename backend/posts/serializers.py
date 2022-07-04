from rest_framwork import serializers

from .models import Post

class PostSerializer(serializers.ModelSerializer):

	class Meta:
		model = Post 
		fields = ("__all__")