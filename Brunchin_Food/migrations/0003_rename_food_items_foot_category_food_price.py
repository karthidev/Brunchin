# Generated by Django 4.2.11 on 2024-05-12 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Brunchin_Food', '0002_foot_category_user_login'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foot_category',
            old_name='food_items',
            new_name='food_price',
        ),
    ]