from django.contrib import admin
from .models import UserProfileModel, CompanyModel, NewsModel, CollectionModel, ProductType, ProductItem

admin.site.register(UserProfileModel)
admin.site.register(CollectionModel)
admin.site.register(CompanyModel)
admin.site.register(NewsModel)
admin.site.register(ProductType)
admin.site.register(ProductItem)

# Register your models here.
