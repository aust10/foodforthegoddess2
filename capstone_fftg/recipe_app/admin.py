from django.contrib import admin

from .models import Recipe, Category, Technique, KeyWord, Ingredients


admin.site.register(Recipe)
admin.site.register(Category)
admin.site.register(Technique)
admin.site.register(KeyWord)
admin.site.register(Ingredients)



# class RecipeAdmin(admin.ModelAdmin):
#     list_display = ('recipe_name','category','technique','key_words','prep_time','body')

# class CategoryAdmin(admin.ModelAdmin):
#     list_display= ('name')

# the above can be used to cutomize the admin pannel 

# admin.site.register(Favorite)
# admin.site.register(Picture)