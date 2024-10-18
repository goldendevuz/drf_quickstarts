from django.contrib import admin

from api.models import Author, Book, Chapter


class BaseAdmin(admin.ModelAdmin):
    list_per_page = 10

    class Meta:
        abstract = True

class AuthorAdmin(BaseAdmin):
    list_display = [f.name for f in Author._meta.fields]
    list_display.remove('bio')
    list_display.append('short_bio')

    def short_bio(self, obj):
        return obj.bio[:30] + '...' if len(obj.bio) > 30 else obj.book

class BookAdmin(BaseAdmin):
    list_display = [f.name for f in Book._meta.fields]
    # list_display = ['id', 'title', 'author', 'rate', 'pages_count']
    save_as = True




class ChapterAdmin(BaseAdmin):
    list_display = [f.name for f in Chapter._meta.fields]
    save_as = True


admin.site.register(Author, AuthorAdmin)


admin.site.register(Book, BookAdmin)


admin.site.register(Chapter, ChapterAdmin)