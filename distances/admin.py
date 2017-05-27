from django.contrib import admin
from .models import House



class HouseAdmin(admin.ModelAdmin):
    list_display = [f.name for f in House._meta.fields if f.name != "image" and f.name != "id" and f.name != "link"] + ['show_link']
    def show_link(self, obj):
        return '<a href="%s">%s</a>' % (obj.link, obj.link)
    show_link.allow_tags = True

admin.site.register(House, HouseAdmin)
