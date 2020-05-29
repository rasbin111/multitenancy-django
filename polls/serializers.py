from rest_framework.serializers import ModelSerialzier
from .models import Poll

class PollSerializer(ModelSerialzier):

	class Meta:
		model = Poll
		fields = "__all__"