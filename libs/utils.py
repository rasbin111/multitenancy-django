""" Extracting tenant from request """

from tenants.models import Tenant
from django.db import connection


def hostname_from_request(request):
    print(request.get_host())
    return (request.get_host().split(':')[0].lower())


def tenant_from_request(request):
    hostname = hostname_from_request(request)
    print(hostname)
    subdomain_prefix = hostname.split('.')[0]
    return (Tenant.objects.filter(subdomain_prefix=subdomain_prefix).first())


def set_tenant_schema_for_request(request):
    schema = tenant_from_request(request)
    print(schema)
    with connection.cursor() as cursor:
        if schema is not None:
            cursor.execute(f"SET search_path to {schema.name}")


def get_tenants_map():
    """ when we get request to thor.polls.local, we need to read from schema thor and 
                                    when we get request to potter.polls.local, we need to read from schema potter """
    return{
        'thor.polls.local': 'thor',
        'potter.polls.local': 'potter'
    }
