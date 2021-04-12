# Generated by Django 3.1.7 on 2021-04-12 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client_side', '0001_initial'),
        ('admin_side', '0003_tenants_tenant_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deals',
            name='deal_is_in_progress',
        ),
        migrations.AddField(
            model_name='deals',
            name='status',
            field=models.CharField(choices=[('под', 'подписан'), ('раб', 'в работе'), ('вып', 'выполнен')], default='под', max_length=100),
        ),
        migrations.AlterField(
            model_name='deals',
            name='additional_services',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='client_side.additional_services'),
        ),
        migrations.AlterField(
            model_name='deals',
            name='discount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_side.discount_cards'),
        ),
    ]