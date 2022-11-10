import os
import json

from mainapp.models import CollectionModel
from django.core.management.base import BaseCommand

JSON_PATH = 'mainapp/jsons'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), mode='r', encoding='UTF-8') as infile:

        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        collections = load_from_json('collections')

        CollectionModel.objects.all().delete()
        for collection in collections:
            new_collection = CollectionModel(**collection)
            new_collection.save()
