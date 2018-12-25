from django.contrib import admin

# Register your models here.

from catalog.models import Author, Genre, Book, BookInstance, Language

class BooksInline(admin.TabularInline):
    model = Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['last_name', 'first_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]
admin.site.register(Author, AuthorAdmin)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','display_genre')
    inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
                'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
                'fields': ('status', 'due_back')
        }),
    )

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass



