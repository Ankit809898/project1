# Generated by Django 5.0.1 on 2024-01-20 08:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bank",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Card",
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
                ("name", models.CharField(max_length=100)),
                ("card_network", models.CharField(max_length=50)),
                ("card_type", models.CharField(max_length=50)),
                ("annual_fee", models.DecimalField(decimal_places=2, max_digits=10)),
                ("joining_fee", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "min_salary_requirement",
                    models.DecimalField(decimal_places=2, max_digits=12),
                ),
                (
                    "bank",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="credit_cards.bank",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AdditionalInformation",
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
                ("bank_website", models.URLField(blank=True, null=True)),
                ("card_comparison_features", models.TextField(blank=True, null=True)),
                ("bank_contact_details", models.TextField(blank=True, null=True)),
                (
                    "card",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="credit_cards.card",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FeesAndCharges",
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
                (
                    "apr_purchases",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "apr_cash_advances",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "apr_balance_transfers",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "late_payment_fee",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "foreign_transaction_fee",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "min_payment",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "card",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="credit_cards.card",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RewardsProgram",
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
                (
                    "cashback_rate",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                ("reward_points", models.IntegerField(blank=True, null=True)),
                (
                    "loyalty_programs",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "welcome_offer",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("other_benefits", models.TextField(blank=True, null=True)),
                (
                    "card",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="credit_cards.card",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SpendingCategory",
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
                ("category_name", models.CharField(max_length=100)),
                (
                    "cashback_rate",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "capping_limit",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "exclusion_categories",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "card",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="credit_cards.card",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Customer",
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
                ("customer_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                (
                    "additional_information",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="credit_cards.additionalinformation",
                    ),
                ),
                (
                    "bank",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="credit_cards.bank",
                    ),
                ),
                (
                    "card",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="credit_cards.card",
                    ),
                ),
                (
                    "fees_and_charges",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="credit_cards.feesandcharges",
                    ),
                ),
                (
                    "rewards_program",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="credit_cards.rewardsprogram",
                    ),
                ),
                (
                    "spending_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="credit_cards.spendingcategory",
                    ),
                ),
            ],
        ),
    ]
