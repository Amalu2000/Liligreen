# Generated by Django 5.1.4 on 2025-03-20 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
