from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem

@receiver([post_save, post_delete], sender=OrderLineItem)
def update_order_total(sender, instance, **kwargs):
    """
    Update order total on lineitem update/create/delete
    """
    instance.order.update_total()
