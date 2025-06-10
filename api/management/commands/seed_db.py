import os
import django
from django.core.management.base import BaseCommand
from api.models import MenuCategory, MenuItem, Article
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Seeds the database with initial data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding database...')

        # Create menu categories
        self.stdout.write('Creating menu categories...')
        categories = [
            {
                'name': 'Appetizers',
                'description': 'Start your meal with our delicious appetizers'
            },
            {
                'name': 'Main Course',
                'description': 'Savory and satisfying main dishes'
            },
            {
                'name': 'Desserts',
                'description': 'Sweet treats to end your meal'
            },
            {
                'name': 'Beverages',
                'description': 'Refreshing drinks and beverages'
            }
        ]

        created_categories = []
        for category_data in categories:
            category, created = MenuCategory.objects.get_or_create(
                name=category_data['name'],
                defaults={'description': category_data['description']}
            )
            created_categories.append(category)
            status = 'Created' if created else 'Already exists'
            self.stdout.write(f"  {status}: {category.name}")

        # Create menu items
        self.stdout.write('Creating menu items...')
        menu_items = [
            # Appetizers
            {
                'category': created_categories[0],
                'name': 'Spring Rolls',
                'description': 'Fresh vegetables wrapped in rice paper',
                'price': 7.99,
                'is_available': True
            },
            {
                'category': created_categories[0],
                'name': 'Garlic Bread',
                'description': 'Toasted bread with garlic butter',
                'price': 5.99,
                'is_available': True
            },
            # Main Course
            {
                'category': created_categories[1],
                'name': 'Grilled Salmon',
                'description': 'Fresh salmon with lemon butter sauce',
                'price': 18.99,
                'is_available': True
            },
            {
                'category': created_categories[1],
                'name': 'Beef Tenderloin',
                'description': 'Premium beef cooked to perfection',
                'price': 24.99,
                'is_available': True
            },
            # Desserts
            {
                'category': created_categories[2],
                'name': 'Chocolate Cake',
                'description': 'Rich chocolate cake with ganache',
                'price': 8.99,
                'is_available': True
            },
            {
                'category': created_categories[2],
                'name': 'Tiramisu',
                'description': 'Classic Italian dessert',
                'price': 9.99,
                'is_available': True
            },
            # Beverages
            {
                'category': created_categories[3],
                'name': 'Fresh Orange Juice',
                'description': 'Freshly squeezed orange juice',
                'price': 4.99,
                'is_available': True
            },
            {
                'category': created_categories[3],
                'name': 'Espresso',
                'description': 'Strong Italian coffee',
                'price': 3.99,
                'is_available': True
            }
        ]

        for item_data in menu_items:
            item, created = MenuItem.objects.get_or_create(
                name=item_data['name'],
                category=item_data['category'],
                defaults={
                    'description': item_data['description'],
                    'price': item_data['price'],
                    'is_available': item_data['is_available']
                }
            )
            status = 'Created' if created else 'Already exists'
            self.stdout.write(f"  {status}: {item.name} (${item.price})")

        # Create articles
        self.stdout.write('Creating articles...')
        articles = [
            {
                'title': 'New Summer Menu Unveiled',
                'content': 'We are excited to introduce our new summer menu featuring fresh, seasonal ingredients...',
                'is_published': True
            },
            {
                'title': 'Chef Spotlight: Meet Our Head Chef',
                'content': 'Get to know the culinary genius behind our award-winning dishes...',
                'is_published': True
            },
            {
                'title': 'Upcoming Wine Tasting Event',
                'content': 'Join us for an exclusive wine tasting event featuring local vineyards...',
                'is_published': True
            }
        ]

        for article_data in articles:
            slug = slugify(article_data['title'])
            article, created = Article.objects.get_or_create(
                slug=slug,
                defaults={
                    'title': article_data['title'],
                    'content': article_data['content'],
                    'is_published': article_data['is_published']
                }
            )
            status = 'Created' if created else 'Already exists'
            self.stdout.write(f"  {status}: {article.title}")

        self.stdout.write(self.style.SUCCESS('Database seeding completed successfully!'))
