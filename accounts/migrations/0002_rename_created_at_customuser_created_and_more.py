# Generated by Django 5.1.1 on 2024-09-18 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='created_at',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='updated_at',
            new_name='updated',
        ),
    ]
