from django.db import models
from django.contrib.auth.models import User

from tenants.models import TenantAwareModel


class Poll(TenantAwareModel):
    question = models.CharField(max_length=100, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


class Choice(TenantAwareModel):
    poll = models.ForeignKey(
        Poll, related_name='choices', on_delete=models.CASCADE, null=True)
    choice_text = models.CharField(max_length=100)

    def __str__(self):
        return self.choice_text


class Vote(TenantAwareModel):
    choice = models.ForeignKey(
        Choice, related_name='votes', on_delete=models.CASCADE, null=True)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, null=True)
    voted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        unique_together = ('poll', 'voted_by')
