from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from .utils import compress_and_optimize_image
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Product Name"))


# Create your models here.


def validate_image_size(image):
    """Validates image size to ensure it doesn't exceed a specific limit."""
    filesize = image.file.size
    limit_mb = 10  # Max size in MB
    if filesize > limit_mb * 1024 * 1024:
        raise ValidationError(f"Max size of image is {limit_mb} MB")


class Tag(models.Model):
    caption = models.CharField(max_length=20, verbose_name=_("Tag"))

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class Author(models.Model):
    first_name = models.CharField(max_length=100, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=100, verbose_name=_("Last Name"))
    email_address = models.EmailField(verbose_name=_("Email Address"))
    image = models.ImageField(
        upload_to="authors",
        null=True,
        verbose_name=_("Image"),
        validators=[validate_image_size],
    )
    bio = models.TextField(
        validators=[MinLengthValidator(10)], null=True, verbose_name=_("Biography")
    )

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

    def save(self, *args, **kwargs):
        if self.image:
            # Compress and optimize image before saving
            self.image = compress_and_optimize_image(self.image)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Team Member")
        verbose_name_plural = _("Team Members")


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name=_("Title"))
    excerpt = models.CharField(max_length=200, null=True, verbose_name=_("Excerpt"))
    date = models.DateField(auto_now=True, verbose_name=_("Date"))
    access_type = models.CharField(
        max_length=20,
        choices=[("public", _("Public")), ("private", _("Private"))],
        default="public",
        verbose_name=_("Access Type"),
    )
    slug = models.SlugField(unique=True, db_index=True, verbose_name=_("Slug"))
    youtube_url = models.URLField(null=True, verbose_name=_("YouTube URL"))
    content = models.TextField(
        validators=[MinLengthValidator(10)], verbose_name=_("Content")
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        null=True,
        related_name="posts",
        verbose_name=_("Author"),
    )
    tags = models.ManyToManyField(Tag, related_name="posts", verbose_name=_("Tags"))

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title


class Comment(models.Model):
    user_name = models.CharField(max_length=100, verbose_name=_("User Name"))
    user_email = models.EmailField(verbose_name=_("Email Address"))
    text = models.TextField(max_length=400, verbose_name=_("Comment"))
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments", verbose_name=_("Post")
    )

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")


# Frequently Asked Questions


class FAQ(models.Model):
    question = models.CharField(max_length=100, verbose_name=_("Question"))
    answer = models.TextField(max_length=400, verbose_name=_("Answer"))
    main = models.BooleanField(default=False, verbose_name=_("Main FAQ"))

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = _("FAQ")
        verbose_name_plural = _("FAQs")


# Content for pages
# Carousel model
class Carousel(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Title"))
    description = models.TextField(
        max_length=400, verbose_name=_("Description"), blank=True, null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Carousel")
        verbose_name_plural = _("Carousels")


# CarouselImage model
class CarouselImage(models.Model):
    carousel = models.ForeignKey(
        Carousel,
        related_name="images",
        on_delete=models.CASCADE,
        verbose_name=_("Carousel"),
    )
    image = models.ImageField(
        upload_to="carousel/images",
        verbose_name=_("Image"),
        validators=[validate_image_size],
    )
    caption = models.CharField(
        max_length=200, verbose_name=_("Caption"), blank=True, null=True
    )

    url = models.URLField(max_length=200, verbose_name=_("URL"), blank=True, null=True)

    def __str__(self):
        return f"Image of {self.carousel.title}"

    class Meta:
        verbose_name = _("Carousel Image")
        verbose_name_plural = _("Carousel Images")


class RestrictedPage(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Title"))
    content = models.TextField(verbose_name=_("Content"))
    access_code = models.CharField(
        max_length=20, verbose_name=_("Access Code"), unique=True
    )  # The code for accessing the page

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Restricted Page")
        verbose_name_plural = _("Restricted Pages")


class ZoomEvent(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Title"))
    type = models.CharField(
        max_length=20,
        choices=[("webinar", _("Webinar")), ("workshop", _("Workshop"))],
        verbose_name=_("Type"),
    )
    access_type = models.CharField(
        max_length=20,
        choices=[("public", _("Public")), ("private", _("Private"))],
        default="public",
        verbose_name=_("Access Type"),
    )
    description = models.TextField(verbose_name=_("Description"))
    event_time = models.DateTimeField(verbose_name=_("Event Time"))
    zoom_link = models.URLField(verbose_name=_("Zoom Link"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Zoom Event")
        verbose_name_plural = _("Zoom Events")


class WebProduct(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Product Name"))
    description = models.TextField(verbose_name=_("Description"))
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Price")
    )
    image = models.ImageField(
        upload_to="web_products/images",
        verbose_name=_("Image"),
        validators=[validate_image_size],
    )
    available = models.BooleanField(default=True, verbose_name=_("Available"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Web Product")
        verbose_name_plural = _("Web Products")
