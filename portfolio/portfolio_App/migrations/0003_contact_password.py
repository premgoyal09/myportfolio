# Generated by Django 5.0.6 on 2024-08-06 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_App', '0002_remove_contact_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='password',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
