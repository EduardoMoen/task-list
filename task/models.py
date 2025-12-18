from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    date = models.DateField()
    deadline = models.DateTimeField(null=True, blank=True)
    concluded = models.BooleanField(default=False)
    tags = models.ManyToManyField(
        Tag,
        related_name='tasks'
    )

    def __str__(self):
        return self.content
