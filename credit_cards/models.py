from django.db import models

# Create your models here.

class Bank(models.Model):
    name = models.CharField(max_length=100)

class Card(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    card_network = models.CharField(max_length=50)
    card_type = models.CharField(max_length=50)
    annual_fee = models.DecimalField(max_digits=10, decimal_places=2)
    joining_fee = models.DecimalField(max_digits=10, decimal_places=2)
    min_salary_requirement = models.DecimalField(max_digits=12, decimal_places=2)

class RewardsProgram(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    cashback_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    reward_points = models.IntegerField(null=True, blank=True)
    loyalty_programs = models.CharField(max_length=200, null=True, blank=True)
    welcome_offer = models.CharField(max_length=200, null=True, blank=True)
    other_benefits = models.TextField(null=True, blank=True)

class SpendingCategory(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=100)
    cashback_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    capping_limit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    exclusion_categories = models.CharField(max_length=200, null=True, blank=True)

class FeesAndCharges(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    apr_purchases = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    apr_cash_advances = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    apr_balance_transfers = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    late_payment_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    foreign_transaction_fee = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    min_payment = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

class AdditionalInformation(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    bank_website = models.URLField(null=True, blank=True)
    card_comparison_features = models.TextField(null=True, blank=True)
    bank_contact_details = models.TextField(null=True, blank=True)




class Customer(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    rewards_program = models.ForeignKey(RewardsProgram, on_delete=models.CASCADE)
    spending_category = models.ForeignKey(SpendingCategory, on_delete=models.CASCADE)
    fees_and_charges = models.ForeignKey(FeesAndCharges, on_delete=models.CASCADE)
    additional_information = models.ForeignKey(AdditionalInformation, on_delete=models.CASCADE)

    # Add other fields specific to the Customer model if needed
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.customer_name





