from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from rest_framework import viewsets

from libs.utils import tenant_from_request
from .serializers import PollSerializer
from libs.utils import set_tenant_schema_for_request


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    def get_queryset(self):
        set_tenant_schema_for_request(self.request)
        tenant = tenant_from_request(self.request)
        return super().get_queryset().filter(tenant=tenant)

    def destroy(self, request, *args, **kwargs):
        set_tenant_schema_for_request(self.request)
        poll = Poll.objects.get(pk=self.kwargs["pk"])
        if not request.user == poll.created_by:
            raise PermissionDenied("You cannot delete this poll")
        return super().destroy(request, *args, **kwargs)
