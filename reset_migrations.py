#!/usr/bin/env python
"""
Migration reset script for Django Restaurant BE
Use this if migrations are not applying correctly
"""
import os
import sys
import django
from django.conf import settings

# Setup Django
sys.path.append('/home/cpanelusername/restaurant_be_2025_django')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_be_2025_django.settings_production')
django.setup()

from django.db import connection
from django.core.management import execute_from_command_line

def reset_migrations():
    """Reset migrations and recreate tables"""
    print("="*50)
    print("RESETTING MIGRATIONS")
    print("="*50)

    try:
        with connection.cursor() as cursor:
            # Drop all our app tables if they exist
            tables_to_drop = [
                'api_menucategory',
                'api_menuitem',
                'api_article'
            ]

            for table in tables_to_drop:
                try:
                    cursor.execute(f"DROP TABLE IF EXISTS {table}")
                    print(f"✅ Dropped table: {table}")
                except Exception as e:
                    print(f"⚠️ Could not drop {table}: {e}")

            # Also clean up migration records for our app
            try:
                cursor.execute("DELETE FROM django_migrations WHERE app = 'api'")
                print("✅ Cleaned up migration records for 'api' app")
            except Exception as e:
                print(f"⚠️ Could not clean migration records: {e}")

        print("\n" + "="*50)
        print("NOW RUN THESE COMMANDS:")
        print("="*50)
        print("1. python manage.py makemigrations api")
        print("2. python manage.py migrate")
        print("3. python manage.py shell < populate_data.py")

    except Exception as e:
        print(f"❌ Error during reset: {e}")

def show_migration_status():
    """Show current migration status"""
    print("="*50)
    print("MIGRATION STATUS")
    print("="*50)

    try:
        from django.db.migrations.executor import MigrationExecutor
        executor = MigrationExecutor(connection)

        # Show all migrations
        print("All migrations:")
        for app_name, migrations in executor.loader.graph.nodes.items():
            if app_name[0] == 'api':  # Only show our app
                print(f"  App: {app_name[0]}")
                print(f"    Migration: {app_name[1]}")

        # Show pending migrations
        plan = executor.migration_plan(executor.loader.graph.leaf_nodes())
        if plan:
            print(f"\nPending migrations: {len(plan)}")
            for migration in plan:
                print(f"  - {migration[0].app_label}.{migration[0].name}")
        else:
            print("\n✅ No pending migrations")

        # Show applied migrations
        with connection.cursor() as cursor:
            cursor.execute("SELECT app, name FROM django_migrations WHERE app = 'api'")
            applied = cursor.fetchall()
            if applied:
                print(f"\nApplied migrations for 'api' app:")
                for app, name in applied:
                    print(f"  - {app}.{name}")
            else:
                print(f"\n⚠️ No migrations applied for 'api' app")

    except Exception as e:
        print(f"Error checking migration status: {e}")

def main():
    """Main function"""
    print("🔧 Django Migration Reset Tool")
    print("=" * 50)

    print("Choose an option:")
    print("1. Show migration status")
    print("2. Reset migrations (WARNING: This will drop all app tables!)")
    print("3. Exit")

    try:
        choice = input("\nEnter choice (1-3): ").strip()

        if choice == '1':
            show_migration_status()
        elif choice == '2':
            confirm = input("⚠️ This will DROP all app tables! Continue? (yes/no): ").strip().lower()
            if confirm == 'yes':
                reset_migrations()
            else:
                print("Operation cancelled.")
        elif choice == '3':
            print("Exiting...")
        else:
            print("Invalid choice.")

    except KeyboardInterrupt:
        print("\nOperation cancelled.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
