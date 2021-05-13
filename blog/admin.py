from django.contrib import admin
from blog.models import Publication


class PublicationAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'
    list_display = ('nome', 'cwid', 'publication_date')
    list_filter = ('nome', 'cwid')
    search_fields = ('nome', 'cwid')


admin.site.register(Publication, PublicationAdmin)

