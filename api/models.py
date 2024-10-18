from django.core.validators import MinValueValidator
from django.db import models
from django_extensions.db.models import TimeStampedModel


class Author(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)
    bio = models.TextField(max_length=1000, unique=True)

    def __str__(self):
        return self.name


class Book(TimeStampedModel):
    title = models.CharField(max_length=100, unique=True)
    publication_date = models.DateTimeField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    chapters_count = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title


class Chapter(TimeStampedModel):
    title = models.CharField(max_length=100, unique=True)
    chapter_number = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Chapter number of the book."
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='chapters')

    def save(self, **kwargs):
        if self.chapter_number is None:
            raise ValueError("Chapter number cannot be None.")
        if self.book.chapters_count and self.chapter_number > self.book.chapters_count:
            raise ValueError(f"Chapter number cannot exceed {self.book.chapters_count} chapters.")
        super(Chapter, self).save(**kwargs)

    def __str__(self):
        return self.title
