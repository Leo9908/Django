# Generated by Django 3.2.6 on 2023-01-24 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_website_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='status',
            field=models.CharField(choices=[('N', 'Not Reviewed'), ('R', 'Reviewed'), ('E', 'Error'), ('A', 'Accepted')], max_length=1),
        ),
    ]
