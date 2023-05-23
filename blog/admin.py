from django.contrib import admin
from blog.models import Post,Category

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_dispaly='-empty-'
    #fields = ('title',)
    list_display = ['title','author','counted_views','status', 'created_date', 'published_date']
    list_filter = ['status','author']
    ordering=['-created_date']
    search_fields=['title','content'] 

admin.site.register(Category)
admin.site.register(Post,PostAdmin)
 