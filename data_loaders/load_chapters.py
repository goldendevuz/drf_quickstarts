import json
import os
import sys
import django

# Set the root folder as the working directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from api.models import Chapter

# List of chapters to be added
with open('data_loaders/chapters.json') as f:
    chapters_data = json.load(f)

# Create chapters
for chapter_data in chapters_data:
    chapter, created = Chapter.objects.get_or_create(**chapter_data)
    if created:
        print(f'Created chapter: {chapter}')
    else:
        print(f'Chapter already exists: {chapter}')