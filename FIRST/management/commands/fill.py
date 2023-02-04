from catalog.models import Category
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        categories = []

        while True:
            print('enter stop to stop')
            name = input('name = ').lower().strip()
            description = input('description = ').lower().strip()

            if any(x in ('', 'stop', 'стоп') for x in [name, description]):
                break

            categories.append(Category(name, description))


        Category.objects.bulk_create(categories)


