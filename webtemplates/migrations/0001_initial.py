# Generated by Django 4.2.5 on 2023-10-08 09:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EightTemplateFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title', max_length=50, verbose_name='title')),
                ('cover_photo', models.FileField(upload_to='coverimages', verbose_name='Your Cover Photo')),
                ('template_image1', models.FileField(upload_to='firstimages', verbose_name='Image 1')),
                ('template_image2', models.FileField(upload_to='secondimages', verbose_name='Image 2')),
                ('template_image3', models.FileField(upload_to='thirdimages', verbose_name='Image 3')),
                ('template_image4', models.FileField(upload_to='fourthimages', verbose_name='Image 4')),
                ('template_image5', models.FileField(upload_to='fiftimages', verbose_name='Image 5')),
                ('template_image6', models.FileField(upload_to='sixthimages', verbose_name='Image 6')),
                ('template_image7', models.FileField(upload_to='seventhimages', verbose_name='Image 7')),
                ('template_image8', models.FileField(upload_to='eightimages', verbose_name='Image 8')),
                ('template_file', models.FileField(upload_to='sourcefiles', verbose_name='Template Source Codes(ZIP)')),
            ],
        ),
        migrations.CreateModel(
            name='FiveTemplateFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title', max_length=50, verbose_name='title')),
                ('cover_photo', models.FileField(upload_to='coverimages', verbose_name='Your Cover Photo')),
                ('template_image1', models.FileField(upload_to='firstimages', verbose_name='Image 1')),
                ('template_image2', models.FileField(upload_to='secondimages', verbose_name='Image 2')),
                ('template_image3', models.FileField(upload_to='thirdimages', verbose_name='Image 3')),
                ('template_image4', models.FileField(upload_to='fourthimages', verbose_name='Image 4')),
                ('template_image5', models.FileField(upload_to='fiftimages', verbose_name='Image 5')),
                ('template_file', models.FileField(upload_to='sourcefiles', verbose_name='Template Source Codes(ZIP)')),
            ],
        ),
        migrations.CreateModel(
            name='FourTemplateFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title', max_length=50, verbose_name='title')),
                ('cover_photo', models.FileField(upload_to='coverimages', verbose_name='Your Cover Photo')),
                ('template_image1', models.FileField(upload_to='firstimages', verbose_name='Image 1')),
                ('template_image2', models.FileField(upload_to='secondimages', verbose_name='Image 2')),
                ('template_image3', models.FileField(upload_to='thirdimages', verbose_name='Image 3')),
                ('template_image4', models.FileField(upload_to='fourthimages', verbose_name='Image 4')),
                ('template_file', models.FileField(upload_to='sourcefiles', verbose_name='Template Source Codes(ZIP)')),
            ],
        ),
        migrations.CreateModel(
            name='NineTemplateFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title', max_length=50, verbose_name='title')),
                ('cover_photo', models.FileField(upload_to='coverimages', verbose_name='Your Cover Photo')),
                ('template_image1', models.FileField(upload_to='firstimages', verbose_name='Image 1')),
                ('template_image2', models.FileField(upload_to='secondimages', verbose_name='Image 2')),
                ('template_image3', models.FileField(upload_to='thirdimages', verbose_name='Image 3')),
                ('template_image4', models.FileField(upload_to='fourthimages', verbose_name='Image 4')),
                ('template_image5', models.FileField(upload_to='fiftimages', verbose_name='Image 5')),
                ('template_image6', models.FileField(upload_to='sixthimages', verbose_name='Image 6')),
                ('template_image7', models.FileField(upload_to='seventhimages', verbose_name='Image 7')),
                ('template_image8', models.FileField(upload_to='eightimages', verbose_name='Image 8')),
                ('template_image9', models.FileField(upload_to='nineimages', verbose_name='Image 9')),
                ('template_file', models.FileField(upload_to='sourcefiles', verbose_name='Template Source Codes(ZIP)')),
            ],
        ),
        migrations.CreateModel(
            name='OneTemplateFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title', max_length=50, verbose_name='title')),
                ('cover_photo', models.FileField(upload_to='coverimages', verbose_name='Your Cover Photo')),
                ('template_image1', models.FileField(upload_to='firstimages', verbose_name='Image 1')),
                ('template_file', models.FileField(upload_to='sourcefiles', verbose_name='Template Source Codes(ZIP)')),
            ],
        ),
        migrations.CreateModel(
            name='SevenTemplateFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title', max_length=50, verbose_name='title')),
                ('cover_photo', models.FileField(upload_to='coverimages', verbose_name='Your Cover Photo')),
                ('template_image1', models.FileField(upload_to='firstimages', verbose_name='Image 1')),
                ('template_image2', models.FileField(upload_to='secondimages', verbose_name='Image 2')),
                ('template_image3', models.FileField(upload_to='thirdimages', verbose_name='Image 3')),
                ('template_image4', models.FileField(upload_to='fourthimages', verbose_name='Image 4')),
                ('template_image5', models.FileField(upload_to='fiftimages', verbose_name='Image 5')),
                ('template_image6', models.FileField(upload_to='sixthimages', verbose_name='Image 6')),
                ('template_image7', models.FileField(upload_to='seventhimages', verbose_name='Image 7')),
                ('template_file', models.FileField(upload_to='sourcefiles', verbose_name='Template Source Codes(ZIP)')),
            ],
        ),
        migrations.CreateModel(
            name='SixTemplateFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title', max_length=50, verbose_name='title')),
                ('cover_photo', models.FileField(upload_to='coverimages', verbose_name='Your Cover Photo')),
                ('template_image1', models.FileField(upload_to='firstimages', verbose_name='Image 1')),
                ('template_image2', models.FileField(upload_to='secondimages', verbose_name='Image 2')),
                ('template_image3', models.FileField(upload_to='thirdimages', verbose_name='Image 3')),
                ('template_image4', models.FileField(upload_to='fourthimages', verbose_name='Image 4')),
                ('template_image5', models.FileField(upload_to='fiftimages', verbose_name='Image 5')),
                ('template_image6', models.FileField(upload_to='sixthimages', verbose_name='Image 6')),
                ('template_file', models.FileField(upload_to='sourcefiles', verbose_name='Template Source Codes(ZIP)')),
            ],
        ),
        migrations.CreateModel(
            name='TenTemplateFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title', max_length=50, verbose_name='title')),
                ('cover_photo', models.FileField(upload_to='coverimages', verbose_name='Your Cover Photo')),
                ('template_image1', models.FileField(upload_to='firstimages', verbose_name='Image 1')),
                ('template_image2', models.FileField(upload_to='secondimages', verbose_name='Image 2')),
                ('template_image3', models.FileField(upload_to='thirdimages', verbose_name='Image 3')),
                ('template_image4', models.FileField(upload_to='fourthimages', verbose_name='Image 4')),
                ('template_image5', models.FileField(upload_to='fiftimages', verbose_name='Image 5')),
                ('template_image6', models.FileField(upload_to='sixthimages', verbose_name='Image 6')),
                ('template_image7', models.FileField(upload_to='seventhimages', verbose_name='Image 7')),
                ('template_image8', models.FileField(upload_to='eightimages', verbose_name='Image 8')),
                ('template_image9', models.FileField(upload_to='nineimages', verbose_name='Image 9')),
                ('template_image10', models.FileField(upload_to='tenimages', verbose_name='Image 10')),
                ('template_file', models.FileField(upload_to='sourcefiles', verbose_name='Template Source Codes(ZIP)')),
            ],
        ),
        migrations.CreateModel(
            name='ThreeTemplateFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title', max_length=50, verbose_name='title')),
                ('cover_photo', models.FileField(upload_to='coverimages', verbose_name='Your Cover Photo')),
                ('template_image1', models.FileField(upload_to='firstimages', verbose_name='Image 1')),
                ('template_image2', models.FileField(upload_to='secondimages', verbose_name='Image 2')),
                ('template_image3', models.FileField(upload_to='thirdimages', verbose_name='Image 3')),
                ('template_file', models.FileField(upload_to='sourcefiles', verbose_name='Template Source Codes(ZIP)')),
            ],
        ),
        migrations.CreateModel(
            name='TwoTemplateFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title', max_length=50, verbose_name='title')),
                ('cover_photo', models.FileField(upload_to='coverimages', verbose_name='Your Cover Photo')),
                ('template_image1', models.FileField(upload_to='firstimages', verbose_name='Image 1')),
                ('template_image2', models.FileField(upload_to='secondimages', verbose_name='Image 2')),
                ('template_file', models.FileField(upload_to='sourcefiles', verbose_name='Template Source Codes(ZIP)')),
            ],
        ),
        migrations.CreateModel(
            name='WebTemplates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('description', models.TextField()),
                ('page_number', models.IntegerField(default=1, verbose_name='Number of Pages(Max. 10)')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('cover_photo', models.FileField(blank=True, null=True, upload_to='coverimages', verbose_name='Your Cover Photo')),
                ('template_image1', models.FileField(blank=True, null=True, upload_to='firstimages', verbose_name='Image 1')),
                ('template_image2', models.FileField(blank=True, null=True, upload_to='secondimages', verbose_name='Image 2')),
                ('template_image3', models.FileField(blank=True, null=True, upload_to='thirdimages', verbose_name='Image 3')),
                ('template_image4', models.FileField(blank=True, null=True, upload_to='fourthimages', verbose_name='Image 4')),
                ('template_image5', models.FileField(blank=True, null=True, upload_to='fiftimages', verbose_name='Image 5')),
                ('template_image6', models.FileField(blank=True, null=True, upload_to='sixthimages', verbose_name='Image 6')),
                ('template_image7', models.FileField(blank=True, null=True, upload_to='seventhimages', verbose_name='Image 7')),
                ('template_image8', models.FileField(blank=True, null=True, upload_to='eightimages', verbose_name='Image 8')),
                ('template_image9', models.FileField(blank=True, null=True, upload_to='nineimages', verbose_name='Image 9')),
                ('template_image10', models.FileField(blank=True, null=True, upload_to='tenimages', verbose_name='Image 10')),
                ('template_file', models.FileField(blank=True, null=True, upload_to='sourcefiles', verbose_name='Template Source Codes(ZIP)')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='maker')),
            ],
        ),
    ]
