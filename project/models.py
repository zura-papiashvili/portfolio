# project/models.py
from django.db import models
from django.utils.translation import gettext_lazy as _


class Project(models.Model):
    STATUS_CHOICES = [
        ("planning", "Planning"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
        ("on_hold", "On Hold"),
    ]

    # Basic Fields
    name = models.CharField(max_length=255, verbose_name="Project Name")
    description = models.TextField(
        help_text="Detailed description of the project.", verbose_name="Description"
    )
    customer_name = models.CharField(
        max_length=255, help_text="Name of the customer.", verbose_name="Customer Name"
    )
    customer_email = models.EmailField(
        help_text="Customer's email address.", verbose_name="Customer Email"
    )
    customer_phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text="Customer's phone number.",
        verbose_name="Customer Phone",
    )

    # Date Fields
    start_date = models.DateField(
        help_text="The date the project started.", verbose_name="Start Date"
    )
    end_date = models.DateField(
        null=True,
        blank=True,
        help_text="The estimated or actual completion date of the project.",
        verbose_name="End Date",
    )

    # Project Status
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="planning",
        help_text="Current status of the project.",
        verbose_name="Status",
    )

    # Budget Fields
    budget = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Total budget allocated for the project.",
        verbose_name="Budget",
    )
    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Total cost incurred so far (optional).",
        verbose_name="Cost",
    )

    # Images or Media (Optional)
    image = models.ImageField(
        upload_to="project_images/",
        blank=True,
        null=True,
        help_text="Image related to the project.",
        verbose_name="Image",
    )
    project_video = models.URLField(
        max_length=200,
        blank=True,
        null=True,
        help_text="Link to a video of the project (optional).",
        verbose_name="Project Video",
    )

    # Additional Information
    notes = models.TextField(
        blank=True,
        null=True,
        help_text="Additional notes about the project.",
        verbose_name="Notes",
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-start_date"]  # Order by start date (most recent first)
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")


class Service(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    price_range = models.CharField(max_length=255, verbose_name="Price Range")
    description = models.TextField(verbose_name="Description")
    features = models.TextField(
        help_text="Separate features with a new line.", verbose_name="Features"
    )
    ideal_for = models.TextField(
        help_text="Separate target groups with a new line.", verbose_name="Ideal For"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    def get_features(self):
        return self.features.split("\n")

    def get_ideal_for(self):
        return self.ideal_for.split("\n")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")
