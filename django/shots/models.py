from django.db import models


class Shot(models.Model):
    shot_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def get_complexity(self):
        return 0.0


class Task(models.Model):
    shot = models.ForeignKey(Shot, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=200)


class Scene(models.Model):
    linked_task = models.ForeignKey(Task, on_delete=models.CASCADE)
    number_of_polygons = models.IntegerField(max_length=100)
