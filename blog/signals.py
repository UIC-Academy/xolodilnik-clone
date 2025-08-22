from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.text import slugify

from blog.models import BlogPost
from blog.choices import BlogPostStatus


@receiver(pre_save, sender=BlogPost)
def blog_post_post_save_handler(sender, instance, **kwargs):
    if instance.title:
        instance.slug = slugify(instance.title)
    if instance.status == BlogPostStatus.PUBLISHED and not instance.published_at:
        instance.published_at = instance.created_at
    elif instance.status == BlogPostStatus.DRAFT:
        instance.published_at = None