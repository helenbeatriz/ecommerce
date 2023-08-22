# Generated by Django 3.2.19 on 2023-08-16 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("products", "0002_alter_category_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order_number", models.CharField(editable=False, max_length=32)),
                ("full_name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("phone_number", models.CharField(max_length=20)),
                ("street_address", models.CharField(max_length=80)),
                ("town_or_city", models.CharField(max_length=40)),
                ("county", models.CharField(blank=True, max_length=80, null=True)),
                ("postcode", models.CharField(blank=True, max_length=20, null=True)),
                ("country", models.CharField(max_length=40)),
                (
                    "delivery_cost",
                    models.DecimalField(decimal_places=2, default=0, max_digits=6),
                ),
                (
                    "order_total",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                (
                    "grand_total",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="OrderLineItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField(default=0)),
                (
                    "lineitem_total",
                    models.DecimalField(decimal_places=2, editable=False, max_digits=6),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lineitems",
                        to="checkout.order",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
            ],
        ),
    ]
