from django.db import models
from django import forms

# Create your models here.
class WebTemplates(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="maker")
    title = models.CharField(max_length=50, verbose_name="title")
    description = models.TextField()
    page_number = models.IntegerField(verbose_name="Number of Pages(Max. 10)", default=1)
    created_date = models.DateField(auto_now_add=True, verbose_name="Created Date")
    cover_photo = models.FileField(verbose_name="Your Cover Photo", blank=True, null=True)
    template_image1 = models.FileField(verbose_name="Image 1", blank=True, null=True)
    template_image2 = models.FileField(verbose_name="Image 2", blank=True, null=True)
    template_image3 = models.FileField(verbose_name="Image 3", blank=True, null=True)
    template_image4 = models.FileField(verbose_name="Image 4", blank=True, null=True)
    template_image5 = models.FileField(verbose_name="Image 5", blank=True, null=True)
    template_image6 = models.FileField(verbose_name="Image 6", blank=True, null=True)
    template_image7 = models.FileField(verbose_name="Image 7", blank=True, null=True)
    template_image8 = models.FileField(verbose_name="Image 8", blank=True, null=True)
    template_image9 = models.FileField(verbose_name="Image 9", blank=True, null=True)
    template_image10 = models.FileField(verbose_name="Image 10", blank=True, null=True)
    template_file = models.FileField(verbose_name="Template Source Codes(ZIP)", blank=True, null=True)

class OneTemplateFiles(models.Model):
    title = models.CharField(max_length=50, verbose_name="title", default="title")
    cover_photo = models.FileField(verbose_name="Your Cover Photo", upload_to="coverimages")
    template_image1 = models.FileField(verbose_name="Image 1")
    template_file = models.FileField(verbose_name="Template Source Codes(ZIP)", upload_to="sourcefiles")

class TwoTemplateFiles(models.Model):
    title = models.CharField(max_length=50, verbose_name="title", default="title")
    cover_photo = models.FileField(verbose_name="Your Cover Photo", upload_to="coverimages")
    template_image1 = models.FileField(verbose_name="Image 1", upload_to="firstimages")
    template_image2 = models.FileField(verbose_name="Image 2", upload_to="secondimages")
    template_file = models.FileField(verbose_name="Template Source Codes(ZIP)", upload_to="sourcefiles")

class ThreeTemplateFiles(models.Model):
    title = models.CharField(max_length=50, verbose_name="title", default="title")
    cover_photo = models.FileField(verbose_name="Your Cover Photo")
    template_image1 = models.FileField(verbose_name="Image 1")
    template_image2 = models.FileField(verbose_name="Image 2")
    template_image3 = models.FileField(verbose_name="Image 3")
    template_file = models.FileField(verbose_name="Template Source Codes(ZIP)")

class FourTemplateFiles(models.Model):
    title = models.CharField(max_length=50, verbose_name="title", default="title")
    cover_photo = models.FileField(verbose_name="Your Cover Photo", upload_to="coverimages")
    template_image1 = models.FileField(verbose_name="Image 1", upload_to="firstimages")
    template_image2 = models.FileField(verbose_name="Image 2", upload_to="secondimages")
    template_image3 = models.FileField(verbose_name="Image 3", upload_to="thirdimages")
    template_image4 = models.FileField(verbose_name="Image 4", upload_to="fourthimages")
    template_file = models.FileField(verbose_name="Template Source Codes(ZIP)", upload_to="sourcefiles")

class FiveTemplateFiles(models.Model):
    title = models.CharField(max_length=50, verbose_name="title", default="title")
    cover_photo = models.FileField(verbose_name="Your Cover Photo")
    template_image1 = models.FileField(verbose_name="Image 1")
    template_image2 = models.FileField(verbose_name="Image 2")
    template_image3 = models.FileField(verbose_name="Image 3")
    template_image4 = models.FileField(verbose_name="Image 4")
    template_image5 = models.FileField(verbose_name="Image 5")
    template_file = models.FileField(verbose_name="Template Source Codes(ZIP)")

class SixTemplateFiles(models.Model):
    title = models.CharField(max_length=50, verbose_name="title", default="title")
    cover_photo = models.FileField(verbose_name="Your Cover Photo")
    template_image1 = models.FileField(verbose_name="Image 1")
    template_image2 = models.FileField(verbose_name="Image 2")
    template_image3 = models.FileField(verbose_name="Image 3")
    template_image4 = models.FileField(verbose_name="Image 4")
    template_image5 = models.FileField(verbose_name="Image 5")
    template_image6 = models.FileField(verbose_name="Image 6")
    template_file = models.FileField(verbose_name="Template Source Codes(ZIP)")

class SevenTemplateFiles(models.Model):
    title = models.CharField(max_length=50, verbose_name="title", default="title")
    cover_photo = models.FileField(verbose_name="Your Cover Photo")
    template_image1 = models.FileField(verbose_name="Image 1")
    template_image2 = models.FileField(verbose_name="Image 2")
    template_image3 = models.FileField(verbose_name="Image 3", upload_to="thirdimages")
    template_image4 = models.FileField(verbose_name="Image 4", upload_to="fourthimages")
    template_image5 = models.FileField(verbose_name="Image 5", upload_to="fiftimages")
    template_image6 = models.FileField(verbose_name="Image 6", upload_to="sixthimages")
    template_image7 = models.FileField(verbose_name="Image 7", upload_to="seventhimages")
    template_file = models.FileField(verbose_name="Template Source Codes(ZIP)", upload_to="sourcefiles")

class EightTemplateFiles(models.Model):
    title = models.CharField(max_length=50, verbose_name="title", default="title")
    cover_photo = models.FileField(verbose_name="Your Cover Photo", upload_to="coverimages")
    template_image1 = models.FileField(verbose_name="Image 1")
    template_image2 = models.FileField(verbose_name="Image 2")
    template_image3 = models.FileField(verbose_name="Image 3")
    template_image4 = models.FileField(verbose_name="Image 4")
    template_image5 = models.FileField(verbose_name="Image 5")
    template_image6 = models.FileField(verbose_name="Image 6")
    template_image7 = models.FileField(verbose_name="Image 7")
    template_image8 = models.FileField(verbose_name="Image 8")
    template_file = models.FileField(verbose_name="Template Source Codes(ZIP)")

class NineTemplateFiles(models.Model):
    title = models.CharField(max_length=50, verbose_name="title", default="title")
    cover_photo = models.FileField(verbose_name="Your Cover Photo")
    template_image1 = models.FileField(verbose_name="Image 1")
    template_image2 = models.FileField(verbose_name="Image 2")
    template_image3 = models.FileField(verbose_name="Image 3")
    template_image4 = models.FileField(verbose_name="Image 4")
    template_image5 = models.FileField(verbose_name="Image 5")
    template_image6 = models.FileField(verbose_name="Image 6")
    template_image7 = models.FileField(verbose_name="Image 7")
    template_image8 = models.FileField(verbose_name="Image 8")
    template_image9 = models.FileField(verbose_name="Image 9")
    template_file = models.FileField(verbose_name="Template Source Codes(ZIP)")

class TenTemplateFiles(models.Model):
    title = models.CharField(max_length=50, verbose_name="title", default="title")
    cover_photo = models.FileField(verbose_name="Your Cover Photo")
    template_image1 = models.FileField(verbose_name="Image 1")
    template_image2 = models.FileField(verbose_name="Image 2")
    template_image3 = models.FileField(verbose_name="Image 3")
    template_image4 = models.FileField(verbose_name="Image 4")
    template_image5 = models.FileField(verbose_name="Image 5")
    template_image6 = models.FileField(verbose_name="Image 6")
    template_image7 = models.FileField(verbose_name="Image 7")
    template_image8 = models.FileField(verbose_name="Image 8")
    template_image9 = models.FileField(verbose_name="Image 9")
    template_image10 = models.FileField(verbose_name="Image 10")
    template_file = models.FileField(verbose_name="Template Source Codes(ZIP)")