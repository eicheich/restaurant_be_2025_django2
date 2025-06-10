#!/usr/bin/env python
"""
Database connection debugging script for cPanel deployment
Run this script to test database connectivity and diagnose issues
"""
import os
import sys
import django
from django.conf import settings

# Add the project root to the Python path
sys.path.append('/home/cpanelusername/restaurant_be_2025_django')

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_be_2025_django.settings_production')

# Setup Django
django.setup()

from django.db import connection
from django.core.management import execute_from_command_line

def test_database_connection():
    """Test basic database connectivity"""
    print("="*50)
    print("TESTING DATABASE CONNECTION")
    print("="*50)

    try:
        # Test basic connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            print("✅ Database connection successful!")
            print(f"   Test query result: {result}")

        # Get database info
        db_settings = settings.DATABASES['default']
        print(f"\n📋 Database Configuration:")
        print(f"   Engine: {db_settings['ENGINE']}")
        print(f"   Name: {db_settings['NAME']}")
        print(f"   User: {db_settings['USER']}")
        print(f"   Host: {db_settings['HOST']}")
        print(f"   Port: {db_settings['PORT']}")

        # Check if tables exist
        print(f"\n🔍 Checking existing tables:")
        with connection.cursor() as cursor:
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            if tables:
                print(f"   Found {len(tables)} tables:")
                for table in tables:
                    print(f"   - {table[0]}")
            else:
                print("   No tables found in database")

        # Check migration status
        print(f"\n📊 Migration Status:")
        try:
            from django.db.migrations.executor import MigrationExecutor
            executor = MigrationExecutor(connection)
            plan = executor.migration_plan(executor.loader.graph.leaf_nodes())

            if plan:
                print(f"   Pending migrations: {len(plan)}")
                for migration in plan:
                    print(f"   - {migration[0].app_label}.{migration[0].name}")
            else:
                print("   ✅ All migrations are up to date")

            # Check if django_migrations table exists
            with connection.cursor() as cursor:
                cursor.execute("SHOW TABLES LIKE 'django_migrations'")
                migrations_table = cursor.fetchone()
                if migrations_table:
                    cursor.execute("SELECT COUNT(*) FROM django_migrations")
                    count = cursor.fetchone()[0]
                    print(f"   Django migrations table exists with {count} records")
                else:
                    print("   ⚠️ Django migrations table does not exist")

        except Exception as e:
            print(f"   Error checking migrations: {e}")

    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        print(f"\n🔧 Troubleshooting tips:")
        print(f"   1. Check if MySQL database exists")
        print(f"   2. Verify database credentials in settings_production.py")
        print(f"   3. Ensure database user has proper permissions")
        print(f"   4. Check if MySQL service is running")
        return False

    return True

def check_app_models():
    """Check if our app models are properly configured"""
    print("\n" + "="*50)
    print("CHECKING APP MODELS")
    print("="*50)

    try:
        from api.models import MenuCategory, MenuItem, Article

        print("✅ Models imported successfully:")
        print("   - MenuCategory")
        print("   - MenuItem")
        print("   - Article")

        # Check model counts
        try:
            categories_count = MenuCategory.objects.count()
            items_count = MenuItem.objects.count()
            articles_count = Article.objects.count()

            print(f"\n📊 Current data counts:")
            print(f"   MenuCategory: {categories_count}")
            print(f"   MenuItem: {items_count}")
            print(f"   Article: {articles_count}")

        except Exception as e:
            print(f"   ⚠️ Could not query models (tables may not exist): {e}")

    except ImportError as e:
        print(f"❌ Could not import models: {e}")
        return False

    return True

def main():
    """Main debugging function"""
    print("🔧 Django Restaurant BE - Database Debug Tool")
    print("=" * 60)

    # Test database connection
    db_ok = test_database_connection()

    if db_ok:
        # Check models
        check_app_models()

        print("\n" + "="*50)
        print("RECOMMENDATIONS")
        print("="*50)

        print("If migrations show 'No migrations to apply':")
        print("1. Run: python manage.py showmigrations")
        print("2. If tables don't exist, run: python manage.py migrate --fake-initial")
        print("3. If that fails, drop tables and run: python manage.py migrate")
        print("4. Then populate data with: python manage.py shell < populate_data.py")

    else:
        print("\n" + "="*50)
        print("NEXT STEPS")
        print("="*50)
        print("1. Update settings_production.py with correct database credentials")
        print("2. Create MySQL database in cPanel")
        print("3. Create database user and grant permissions")
        print("4. Run this script again to verify connection")

if __name__ == "__main__":
    main()
