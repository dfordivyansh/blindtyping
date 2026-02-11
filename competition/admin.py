from django.contrib import admin
from .models import TypingTest, Result

@admin.register(TypingTest)
class TypingTestAdmin(admin.ModelAdmin):
    list_display = ("title", "duration", "active")
    list_filter = ("active",)

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ("user", "test", "wpm", "accuracy", "avg_key_interval", "suspicious", "disqualified", "created_at")
    list_filter = ("suspicious", "disqualified", "created_at")
    search_fields = ("user__username",)
