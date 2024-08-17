# Generated by Django 4.2.4 on 2024-08-12 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sifex_system', '0066_awbhistory_remark_delete_awbremark'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_id', models.IntegerField()),
                ('awb', models.CharField(max_length=255)),
                ('customer', models.CharField(max_length=255)),
                ('pcs', models.IntegerField()),
                ('weight_kg', models.DecimalField(decimal_places=2, max_digits=10)),
                ('origin', models.CharField(max_length=255)),
                ('total_amount_tzs', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(max_length=50)),
                ('action', models.CharField(max_length=50)),
                ('performed_at', models.DateTimeField(auto_now_add=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('performed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
