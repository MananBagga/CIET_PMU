# from django.db import models

# # Create your models here.


# from django.contrib.auth.models import User

# class Program(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user
#     type = models.CharField(max_length=100)
#     title = models.CharField(max_length=100)
#     program_budget = models.DecimalField(max_digits=10, decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title

# class KPIDetails(models.Model):
#     program = models.ForeignKey(Program, on_delete=models.CASCADE)
#     kpi_name = models.CharField(max_length=100)
#     kpi_date = models.DateField()
#     kpi_budget = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return self.kpi_name

# class WorkshopDetails(models.Model):
#     program = models.ForeignKey(Program, on_delete=models.CASCADE)
#     workshop_name = models.CharField(max_length=100)  # Corrected from CharFile to CharField
#     workshop_date = models.DateField()
#     workshop_budget = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return self.workshop_name

# class MeetingDetails(models.Model):
#     program = models.ForeignKey(Program, on_delete=models.CASCADE)
#     meeting_name = models.CharField(max_length=100)
#     meeting_date = models.DateField()
#     meeting_budget = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return self.meeting_name

# class ManpowerDetails(models.Model):
#     program = models.ForeignKey(Program, on_delete=models.CASCADE)
#     manpower_details = models.CharField(max_length=100)
#     manpower_date = models.DateField()
#     manpower_budget = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return self.manpower_details