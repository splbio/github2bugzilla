from django.db import models

# Create your models here.
from datetime import datetime

from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator, URLValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

class PullRecord(Model):
    state = models.IntegerField(
            verbose_name=_("What state the pull record is in."),
            default=0,
            null=False,
            )
    bugid = models.IntegerField(
            verbose_name=_("Bugzilla ID"),
            null=False,
            )
    submitted = models.DateTimeField(
            verbose_name=_("When Bugzilla ID was submitted"),
            )
    headhash = models.CharField(
            verbose_name=_("Head of last sha submitted to bugzilla"),
            max_length=40)
