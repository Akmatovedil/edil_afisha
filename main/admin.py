from django.contrib import admin
from main.models import Film, Review
# Register your models here.
class FilmAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'producer', 'rating', 'duration']
    search_fields = 'name'.split()
admin.site.register(Film, FilmAdmin)
admin.site.register(Review)
