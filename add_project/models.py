from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100, null=False)
    image = models.ImageField(upload_to='project_images/', null=False, )
    github = models.URLField(null=False)
    deploy = models.URLField(null=False)
    devchallenges = models.URLField(null=False)
    
def delete(self, using=None, keep_parents=False):
    if self.image and self.image.storage.exists(self.image.name):
        self.image.storage.delete(self.image.name)
    
    return super().delete(using=using, keep_parents=keep_parents)