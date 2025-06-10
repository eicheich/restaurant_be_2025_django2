#!/usr/bin/env python
"""
Simple database connection test for cPanel
Run this to check if your database settings are correct
"""
import os
import sys
import django

# Set production settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_be_2025_django.settings_production')

# Setup Django
django.setup()

from django.db import connection
from django.conf import settings

def test_database_connection():
    print("=== Database Connection Test ===")
    print(f"Database Engine: {settings.DATABASES['default']['ENGINE']}")
    print(f"Database Name: {settings.DATABASES['default']['NAME']}")
    print(f"Database User: {settings.DATABASES['default']['USER']}")
    print(f"Database Host: {settings.DATABASES['default']['HOST']}")
    print("")

    try:
        # Test connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            print("✅ Database connection successful!")
            print(f"Test query result: {result}")

        # Check if tables exist
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        print(f"📊 Existing tables: {len(tables)}")
        for table in tables:
            print(f"  - {table[0]}")

    except Exception as e:
        print("❌ Database connection failed!")
        print(f"Error: {e}")
        print("")
        print("Please check:")
        print("1. Database name, user, password are correct")
        print("2. Database user has privileges on the database")
        print("3. MySQL service is running")
        return False

    return True

if __name__ == "__main__":
    success = test_database_connection()
    if success:
        print("\n🎉 Database is ready! You can now run migrations.")
    else:
        print("\n❌ Fix database issues before running migrations.")
