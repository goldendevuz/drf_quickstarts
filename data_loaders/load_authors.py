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

from api.models import Author

# List of authors to be added
with open('data_loaders/authors.json') as f:
    authors_data = json.load(f)

# Create authors
for author_data in authors_data:
    author, created = Author.objects.get_or_create(**author_data)
    if created:
        print(f'Created author: {author}')
    else:
        print(f'Author already exists: {author}')