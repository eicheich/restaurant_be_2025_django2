from rest_framework import serializers
from ..models import Article


class ArticleSerializer(serializers.ModelSerializer):
    """
    Serializer for Article model
    """
    class Meta:
        model = Article
        fields = ['id', 'title', 'slug', 'content', 'image',
                 'is_published', 'created_at', 'updated_at']
        read_only_fields = ['slug']  # Slug is automatically generated

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Default image URL jika image = null
        default_image_url = "https://safetypreneur.co.id/halaman/kontak-tengah"

        if representation['image'] and instance.image:
            request = self.context.get('request')
            if request:
                representation['image'] = request.build_absolute_uri(instance.image.url)
        else:
            representation['image'] = default_image_url

        return representation
