from django.db import models

class Projects(models.Model):
    project_name = models.CharField(max_length=80)
    project_location = models.CharField(max_length=80)
    client_name = models.CharField(max_length=80)
    
    work_status_choices = (
        ('Completed', 'Completed'),
        ('Ongoing', 'Ongoing')
    )
    project_status = models.CharField(choices=work_status_choices, default='Ongoing', max_length=20)
    
    work_des = models.TextField(blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    
    project_img = models.ImageField(upload_to='media/', height_field=None, width_field=None, max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.project_status == 'Ongoing':
            self.end_date = None  # Set end_date to None if the project is ongoing
        super().save(*args, **kwargs)

    def __str__(self):
        return self.project_name
