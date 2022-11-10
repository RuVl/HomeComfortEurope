from django.contrib import admin
from .models import UserProfileModel, ProductType, ProductItem, CollectionModel, NewsModel, CompanyModel
admin.site.register(UserProfileModel)
admin.site.register(ProductType)
admin.site.register(ProductItem)
admin.site.register(CollectionModel)
admin.site.register(NewsModel)
admin.site.register(CompanyModel)
# Register your models here.
