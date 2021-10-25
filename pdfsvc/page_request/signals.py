import logging

from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import pdf
from .models import PageRequest

logger = logging.getLogger(__name__)


@receiver(post_save, sender=PageRequest)
def call_pdf(sender, instance, created, **kwargs):
    logger.info("New Page Created: %s", instance.url)
    if created:
        logger.info("Creating pdf for instance %s", instance.pk)
        pdf(instance)
