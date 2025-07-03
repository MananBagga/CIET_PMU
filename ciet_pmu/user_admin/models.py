from django.db import models
from django.utils import timezone

# Create your models here.
class programs(models.Model):
    PROGRAM_TYPES = [
        ('PAC', 'PAC'),
        ('PAB', 'PAB'),
        ('OTHERS', 'OTHERS'),
    ]

    PROGRAM_SUBTYPES = [
        ('pl', 'Planning'),
        ('rs', 'Research'),
        ('dl', 'Developement'),
        ('or', 'Outreach')
    ]

    program_title = models.CharField(max_length=100)
    date_added = models.DateTimeField(default=timezone.now)
    program_subtypes = models.CharField(max_length=2, choices=PROGRAM_SUBTYPES, default='pl')
    program_types = models.CharField(max_length=6, choices=PROGRAM_TYPES, default='OTHERS')
    # assign_coordinator = models.ForeignKey(coordinator, on_delete=models.CASCADE, related_name='assign_coordinator')
    
