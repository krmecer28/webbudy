# Generated by Django 4.2.5 on 2023-10-18 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webtemplates', '0002_alter_eighttemplatefiles_template_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webtemplates',
            name='created_date',
            field=models.DateField(auto_now_add=True, verbose_name='Created Date'),
        ),
    ]
