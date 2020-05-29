from django.core.management.commands.migrate import Command as MigrationCommand
from django.db import connection

from libs.utils import get_tenants_map


class Command(MigrationCommand):
    def handle(self, *args, **options):
        # to use database connection use, connection.cursor() to get a cursor object
        with connection.cursor() as cursor: 
            schemas = get_tenants_map().values()
            for schema in schemas:
                cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {schema}") # create a new shema 
                cursor.execute(f"SET search_path to {schema}") # set connection to use the given schema
                super().handle(*args, **options)




