from django.db import models
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100, blank=True, null=True)  
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)  

    def __str__(self):
        return f"{self.name} ({self.speciality})" if self.speciality else self.name

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)  
    illness = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.illness}"



class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.patient.name} with {self.doctor.name} on {self.date} at {self.time}"
