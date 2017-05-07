from django.db import models

# Create your models here.

class Access_Log(models.Model):
    log_data = models.CharField(max_length=100)
    access_ip = models.CharField(max_length=100, blank=False)
    access_url = models.CharField(max_length=150, blank=False)
    access_status = models.IntegerField()
    blank_field1 = models.CharField(max_length=30)

    def __str__(self):
        return "access ip{0}--access_url{1}".format(self.access_ip,self.access_url)

class Error_Log(models.Model):
    error_level = models.CharField(max_length=30)
    error_ip = models.CharField(max_length=100)
    error_content = models.TextField()
    blank_error = models.CharField(max_length=30)

    def __str__(self):
        return "Error log ip:{0}--error_level{1}".format(self.error_ip, self.error_level)

