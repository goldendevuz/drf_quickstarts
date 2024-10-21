# Register your models here.
from django.contrib import admin
from sendables.core.models import ReceivedSendable, RecipientSendableAssociation

admin.site.register([ReceivedSendable, RecipientSendableAssociation])
