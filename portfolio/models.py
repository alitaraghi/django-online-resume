from django.db import models


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ("programming", "Programming"),
        ("web", "Web"),
        ("frameworks_tools", "Frameworks & Tools"),
        ("other", "Other"),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    order = models.PositiveIntegerField(default=0)
    description = models.CharField(
        max_length=255,
        blank=True,
        help_text="Short English description for this skill",
    )

    class Meta:
        ordering = ["category", "order", "name"]

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "title"]

    def __str__(self):
        return self.title
