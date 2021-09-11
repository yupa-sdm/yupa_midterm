from django.db import models

class Patient(models.Model):
    """Model definition for Patient."""

    # TODO: Define fields here
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    age = models.CharField(max_length=5)

    class Meta:
        """Meta definition for Patient."""

        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'

    def __str__(self):
        """Unicode representation of Patient."""
        return self.first_name + " " + self.last_name

        
class Hospital(models.Model):
    """Model definition for Hospital."""

    # TODO: Define fields here
    hospital_name = models.CharField(max_length=255)

    class Meta:
        """Meta definition for Hospital."""

        verbose_name = 'Hospital'
        verbose_name_plural = 'Hospitals'

    def __str__(self):
        """Unicode representation of Hospital."""
        return self.hospital_name

class Physician (models.Model):
    """Model definition for Physician."""
    # TODO: Define fields here
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    expertise = models.CharField(max_length=255)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    hospital = models.ManyToManyField(Hospital, default=None, blank=True, null=True)

    class Meta:
        """Meta definition for Physician."""

        verbose_name = 'Physician'
        verbose_name_plural = 'Physicians'

    def __str__(self):
        """Unicode representation of Physician."""
        return self.first_name + " " + self.last_name



