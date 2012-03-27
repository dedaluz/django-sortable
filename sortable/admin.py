from django.contrib import admin

class SortableAdmin(admin.ModelAdmin):

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.18/jquery-ui.min.js',
            'js/django-admin-sortable.js',)