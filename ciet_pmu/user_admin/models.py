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
    













# class Annualbudget(models.Model):
#     year = models.IntegerField()
#     budget = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'AnnualBudget'


# class Budgetsummary(models.Model):
#     year = models.IntegerField()
#     month = models.IntegerField()
#     total_expenditure = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'BudgetSummary'


# class Program(models.Model):
#     type = models.TextField(blank=True, null=True)
#     title = models.TextField()
#     coordinator = models.ForeignKey('User', models.DO_NOTHING)
#     annual_budget = models.ForeignKey(Annualbudget, models.DO_NOTHING)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'Program'


# class Subentry(models.Model):
#     task = models.ForeignKey('Task', models.DO_NOTHING)
#     title = models.TextField()
#     description = models.TextField(blank=True, null=True)
#     date = models.DateField()
#     budget = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'SubEntry'


# class Task(models.Model):
#     program = models.ForeignKey(Program, models.DO_NOTHING)
#     task_type = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'Task'
