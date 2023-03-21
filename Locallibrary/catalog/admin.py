from django.contrib import admin

# # Register your models here.
from .models import Author, Genre, Book, BookInstance

# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(Genre)
# admin.site.register(BookInstance)
# class AuthorAdmin(admin.ModelAdmin):
#     pass
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    pass

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass