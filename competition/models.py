from django.db import models
from django.contrib.auth.models import User

class TypingTest(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    duration = models.IntegerField(default=60)  # seconds
    active = models.BooleanField(default=True)
    start_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(TypingTest, on_delete=models.CASCADE)

    wpm = models.IntegerField()
    accuracy = models.FloatField()
    time_taken = models.FloatField()

    tab_switches = models.IntegerField(default=0)
    paste_attempts = models.IntegerField(default=0)
    backspace_count = models.IntegerField(default=0)

    keystroke_data = models.JSONField(null=True, blank=True)
    avg_key_interval = models.FloatField(default=0)

    suspicious = models.BooleanField(default=False)
    disqualified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.test.title}"
    
    class Meta:
        unique_together = ("user", "test")

