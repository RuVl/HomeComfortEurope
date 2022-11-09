import os
import json

from django.core.management.base import BaseCommand

from mainapp.models import ProductItem, ProductType, CollectionModel

JSON_PATH = 'mainapp/jsons'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), mode='r', encoding='UTF-8') as infile:

        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        product_object = load_from_json('products')

        for product_type in product_object.keys():
            get_collection = CollectionModel.objects.get(name='All Collection')
            new_product_type = ProductType(name=product_type, collection=get_collection)
            new_product_type.save()
            for product_item in product_object[product_type].items():
                product_item = product_item[1]
                product_name_delete_whitespace = product_item['Range Name'].split()
                product_name = "_".join(product_name_delete_whitespace)
                image_path = 'ProductImages/'+product_name
                product_item['image'] = image_path
                product_new_item = ProductItem(
                    name=product_item['Range Name'],
                    image=product_item['image'],
                    product_code=product_item['Product Code'],
                    material=product_item['Material'],
                    size=product_item['Size'],
                    availability=product_item['Availability'],
                    weight=product_item['Weight'],
                    type=new_product_type
                )
                product_new_item.save()

        # products = load_from_json('products')
        #
        # Product.objects.all().delete()
        # for product in products:
        #     category_name = product['category']
        #     _category = ProductCategory.objects.get(name=category_name)
        #     product['category'] = _category
        #     new_category = Product(**product)
        #     new_category.save()