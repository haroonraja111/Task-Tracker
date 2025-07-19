from django.db import models

# Create your models here.

class Task(models.Model):
    STATUS_CHOICES = [
        ('TODO' , 'To Do'),
        ('IN_PROGRESS', 'In progress'),
        ('DONE' , 'Done')
    ]
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='TODO')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"
    
    class Meta:
        # MSSQL specific optimization
        indexes = [
            models.Index(fields=['status'], name='status_idx'),
        ]