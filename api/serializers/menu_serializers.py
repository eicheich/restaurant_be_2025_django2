from rest_framework import serializers
from ..models import MenuCategory, MenuItem


class MenuCategorySerializer(serializers.ModelSerializer):
    """
    Serializer for MenuCategory model
    """
    class Meta:
        model = MenuCategory
        fields = ['id', 'name', 'description', 'is_active', 'created_at', 'updated_at']


class MenuItemSerializer(serializers.ModelSerializer):
    """
    Serializer for MenuItem model
    """
    category_name = serializers.ReadOnlyField(source='category.name')
    
    class Meta:
        model = MenuItem
        fields = ['id', 'category_id', 'category_name', 'name', 'description', 
                 'price', 'image', 'is_available', 'created_at', 'updated_at']
    
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


class MenuItemDetailSerializer(MenuItemSerializer):
    """
    Detailed serializer for MenuItem that includes category details
    """
    category = MenuCategorySerializer(read_only=True)
    
    class Meta:
        model = MenuItem
        fields = ['id', 'category', 'name', 'description', 'price', 'image', 
                 'is_available', 'created_at', 'updated_at']