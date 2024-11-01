from django.db import models
from users.models import UserProfile


class Course(models.Model):
    # 原有字段
    name = models.CharField(max_length=100)
    description = models.TextField()
    students = models.ManyToManyField(UserProfile, related_name='courses')

    # 新增上课时间字段
    DAY_CHOICES = [
        (1, "周一"),
        (2, "周二"),
        (3, "周三"),
        (4, "周四"),
        (5, "周五"),
        (6, "周六"),
        (7, "周日"),
    ]

    PERIOD_CHOICES = [
        (1, "第一节课 (8:00 - 10:00)"),
        (2, "第二节课 (10:00 - 12:00)"),
        (3, "第三节课 (14:00 - 16:00)"),
        (4, "第四节课 (16:00 - 18:00)"),
    ]

    day_of_week = models.IntegerField(
        choices=DAY_CHOICES, verbose_name="上课日", default=1)
    class_period = models.IntegerField(
        choices=PERIOD_CHOICES, verbose_name="上课节次", default=1)

    def __str__(self):
        return f"{self.name} - {self.get_day_of_week_display()} {self.get_class_period_display()}"
