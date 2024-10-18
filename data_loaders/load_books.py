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

from api.models import Book

# List of books to be added
with open('data_loaders/books.json') as f:
    books_data = json.load(f)

# Create books
for book_data in books_data:
    book, created = Book.objects.get_or_create(**book_data)
    if created:
        print(f'Created book: {book}')
    else:
        print(f'Book already exists: {book}')