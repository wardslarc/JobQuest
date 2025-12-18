#!/usr/bin/env python
"""
Standalone script to create a test user in Django
Run with: python create_test_user.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'resume.settings')
django.setup()

from django.contrib.auth.models import User

# Create test user if it doesn't exist
username = 'testuser'
email = 'test@example.com'
password = 'testpass123'

if User.objects.filter(username=username).exists():
    print(f"✓ User '{username}' already exists")
else:
    user = User.objects.create_user(username=username, email=email, password=password)
    print(f"✓ Created test user:")
    print(f"  Username: {username}")
    print(f"  Email: {email}")
    print(f"  Password: {password}")
