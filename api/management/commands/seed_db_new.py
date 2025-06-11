import os
import django
from django.core.management.base import BaseCommand
from api.models import MenuCategory, MenuItem, Article
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Seeds the database with restaurant menu data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding database dengan menu restoran...')

        # Create menu categories based on real data
        self.stdout.write('Creating menu categories...')
        categories = [
            {
                'name': 'Menu Paket',
                'description': 'Paket menu lengkap dengan nasi dan minuman'
            },
            {
                'name': 'Minuman',
                'description': 'Minuman segar dan hangat'
            },
            {
                'name': 'Menu Makanan',
                'description': 'Menu makanan utama dan lauk pauk'
            },
            {
                'name': 'Cemilan',
                'description': 'Cemilan dan makanan ringan'
            }
        ]

        created_categories = {}
        for category_data in categories:
            category, created = MenuCategory.objects.get_or_create(
                name=category_data['name'],
                defaults={'description': category_data['description']}
            )
            created_categories[category_data['name']] = category
            status = 'Created' if created else 'Already exists'
            self.stdout.write(f"  {status}: {category.name}")

        # Create menu items based on real restaurant data
        self.stdout.write('Creating menu items...')
        menu_items = [
            # Menu Paket
            {
                'category': created_categories['Menu Paket'],
                'name': 'Paket Nila Bakar/Goreng + Nasi + Es Teh',
                'description': 'Paket lengkap nila bakar atau goreng dengan nasi dan es teh',
                'price': 29000
            },
            {
                'category': created_categories['Menu Paket'],
                'name': 'Paket Sate Kambing + Nasi + Es Teh',
                'description': 'Paket sate kambing dengan nasi dan es teh',
                'price': 20000
            },

            # Minuman
            {
                'category': created_categories['Minuman'],
                'name': 'Jeruk Panas/Es',
                'description': 'Minuman jeruk segar, tersedia panas atau es',
                'price': 5000
            },
            {
                'category': created_categories['Minuman'],
                'name': 'Teh Panas/Es',
                'description': 'Teh manis, tersedia panas atau es',
                'price': 4000
            },
            {
                'category': created_categories['Minuman'],
                'name': 'Kopi Susu',
                'description': 'Kopi dengan susu yang nikmat',
                'price': 5000
            },
            {
                'category': created_categories['Minuman'],
                'name': 'Es Cokelat',
                'description': 'Minuman cokelat dingin yang menyegarkan',
                'price': 7000
            },
            {
                'category': created_categories['Minuman'],
                'name': 'Es Jeruk Teko Kecil',
                'description': 'Es jeruk dalam teko kecil untuk berbagi',
                'price': 12000
            },
            {
                'category': created_categories['Minuman'],
                'name': 'Es Jeruk Teko Besar',
                'description': 'Es jeruk dalam teko besar untuk keluarga',
                'price': 22000
            },
            {
                'category': created_categories['Minuman'],
                'name': 'Es Teh Teko Kecil',
                'description': 'Es teh dalam teko kecil untuk berbagi',
                'price': 10000
            },
            {
                'category': created_categories['Minuman'],
                'name': 'Es Teh Teko Besar',
                'description': 'Es teh dalam teko besar untuk keluarga',
                'price': 18000
            },

            # Menu Makanan
            {
                'category': created_categories['Menu Makanan'],
                'name': '1 Kg Nila Bakar/Goreng',
                'description': 'Ikan nila segar 1 kg, bisa dibakar atau digoreng',
                'price': 65000
            },
            {
                'category': created_categories['Menu Makanan'],
                'name': '1 Kg Nila Bumbu Kari',
                'description': 'Ikan nila 1 kg dengan bumbu kari yang khas',
                'price': 70000
            },
            {
                'category': created_categories['Menu Makanan'],
                'name': 'Sup Nila Serani Khas Jepara',
                'description': 'Sup ikan nila dengan resep khas Jepara',
                'price': 27000
            },
            {
                'category': created_categories['Menu Makanan'],
                'name': 'Mie Mewah',
                'description': 'Mie special dengan topping istimewa',
                'price': 13000
            },
            {
                'category': created_categories['Menu Makanan'],
                'name': 'Ca Kangkung',
                'description': 'Tumis kangkung dengan bumbu yang sedap',
                'price': 8000
            },
            {
                'category': created_categories['Menu Makanan'],
                'name': 'Ca Tauge',
                'description': 'Tumis tauge segar dengan bumbu yang pas',
                'price': 8000
            },
            {
                'category': created_categories['Menu Makanan'],
                'name': 'Nasi Putih',
                'description': 'Nasi putih hangat',
                'price': 4000
            },

            # Cemilan
            {
                'category': created_categories['Cemilan'],
                'name': 'Mendoan',
                'description': 'Tempe mendoan khas dengan bumbu yang gurih',
                'price': 6000
            },
            {
                'category': created_categories['Cemilan'],
                'name': 'Tahu Isi',
                'description': 'Tahu dengan isian sayuran segar',
                'price': 6000
            },
            {
                'category': created_categories['Cemilan'],
                'name': 'Udang Rambutan',
                'description': 'Cemilan udang dengan bentuk unik seperti rambutan',
                'price': 10000
            },
            {
                'category': created_categories['Cemilan'],
                'name': 'Pangsit Ayam',
                'description': 'Pangsit isi ayam yang renyah',
                'price': 10000
            },
            {
                'category': created_categories['Cemilan'],
                'name': 'Cireng Ayam Suwir',
                'description': 'Cireng dengan isian ayam suwir',
                'price': 10000
            },
            {
                'category': created_categories['Cemilan'],
                'name': 'Citul',
                'description': 'Cemilan tradisional yang gurih',
                'price': 10000
            },
            {
                'category': created_categories['Cemilan'],
                'name': 'Timus Ubi Ungu',
                'description': 'Cemilan dari ubi ungu yang manis',
                'price': 10000
            },
            {
                'category': created_categories['Cemilan'],
                'name': 'Bola-Bola Pisang Coklat',
                'description': 'Bola pisang dengan topping coklat',
                'price': 10000
            },
            {
                'category': created_categories['Cemilan'],
                'name': 'Pancake Durian',
                'description': 'Pancake dengan rasa durian yang istimewa',
                'price': 10000
            },
            {
                'category': created_categories['Cemilan'],
                'name': 'Kentang Goreng',
                'description': 'Kentang goreng renyah dan lezat',
                'price': 10000
            }
        ]

        created_items = []
        for item_data in menu_items:
            item, created = MenuItem.objects.get_or_create(
                name=item_data['name'],
                defaults={
                    'category': item_data['category'],
                    'description': item_data['description'],
                    'price': item_data['price'],
                    'is_available': True
                }
            )
            created_items.append(item)
            status = 'Created' if created else 'Already exists'
            self.stdout.write(f"  {status}: {item.name} - Rp {item.price:,}")

        # Create sample articles
        self.stdout.write('Creating sample articles...')
        articles = [
            {
                'title': 'Selamat Datang di Restoran Kami',
                'content': '''
                Restoran kami menyajikan berbagai menu khas dengan cita rasa yang autentik.
                Mulai dari nila bakar yang segar, sup serani khas Jepara, hingga berbagai cemilan tradisional.

                Kami menggunakan bahan-bahan segar dan berkualitas untuk memberikan pengalaman kuliner terbaik bagi Anda.
                ''',
                'is_published': True
            },
            {
                'title': 'Menu Spesial: Nila Bakar Khas Jepara',
                'content': '''
                Nikmati kelezatan ikan nila segar yang dibakar dengan bumbu khas.
                Menu andalan kami yang selalu menjadi favorit pelanggan.

                Tersedia dalam paket lengkap dengan nasi dan es teh, atau bisa juga dipesan terpisah.
                ''',
                'is_published': True
            },
            {
                'title': 'Promo Spesial Bulan Ini',
                'content': '''
                Dapatkan diskon 10% untuk pembelian paket menu di atas Rp 50.000.

                Promo berlaku setiap hari mulai pukul 17:00 - 21:00.
                Buruan datang sebelum kehabisan!
                ''',
                'is_published': True
            }
        ]

        for article_data in articles:
            article, created = Article.objects.get_or_create(
                title=article_data['title'],
                defaults={
                    'content': article_data['content'],
                    'is_published': article_data['is_published']
                }
            )
            status = 'Created' if created else 'Already exists'
            self.stdout.write(f"  {status}: {article.title}")

        self.stdout.write(
            self.style.SUCCESS(
                f'''
Database seeding completed successfully!
- {len(categories)} categories created
- {len(menu_items)} menu items created
- {len(articles)} articles created

Summary:
✅ Menu Paket: 2 items
✅ Minuman: 8 items
✅ Menu Makanan: 7 items
✅ Cemilan: 10 items
✅ Articles: 3 items

Total: {len(menu_items)} menu items ready!
                '''
            )
        )
