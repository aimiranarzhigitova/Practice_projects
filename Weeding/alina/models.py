from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    content = models.TextField()

    def save(self, *args, **kwargs):
        super(Contact, self).save(*args, **kwargs)
        return 'Contact.save'

