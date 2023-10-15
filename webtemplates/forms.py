from django import forms
from .models import WebTemplates, OneTemplateFiles, TwoTemplateFiles, ThreeTemplateFiles, FourTemplateFiles, FiveTemplateFiles, SixTemplateFiles, SevenTemplateFiles, EightTemplateFiles, NineTemplateFiles, TenTemplateFiles

class TemplateForm(forms.ModelForm):
    class Meta:
        model = WebTemplates
        fields = ["title", "description", "page_number"]

class TenTemplateImageFileForm(forms.ModelForm):
    class Meta:
        model = TenTemplateFiles
        fields = ["cover_photo", "template_image1", "template_image2", "template_image3", "template_image4", "template_image5", "template_image6", "template_image7", "template_image8", "template_image9", "template_image10", "template_file"]

class NineTemplateImageFileForm(forms.ModelForm):
    class Meta:
        model = NineTemplateFiles
        fields = ["cover_photo", "template_image1", "template_image2", "template_image3", "template_image4", "template_image5", "template_image6", "template_image7", "template_image8", "template_image9", "template_file"]

class EightTemplateImageFileForm(forms.ModelForm):
    class Meta:
        model = EightTemplateFiles
        fields = ["cover_photo", "template_image1", "template_image2", "template_image3", "template_image4", "template_image5", "template_image6", "template_image7", "template_image8", "template_file"]

class SevenTemplateImageFileForm(forms.ModelForm):
    class Meta:
        model = EightTemplateFiles
        fields = ["cover_photo", "template_image1", "template_image2", "template_image3", "template_image4", "template_image5", "template_image6", "template_image7", "template_file"]

class SixTemplateImageFileForm(forms.ModelForm):
    class Meta:
        model = SixTemplateFiles
        fields = ["cover_photo", "template_image1", "template_image2", "template_image3", "template_image4", "template_image5", "template_image6", "template_file"]

class FiveTemplateImageFileForm(forms.ModelForm):
    class Meta:
        model = FiveTemplateFiles
        fields = ["cover_photo", "template_image1", "template_image2", "template_image3", "template_image4", "template_image5", "template_file"]

class FourTemplateImageFileForm(forms.ModelForm):
    class Meta:
        model = FiveTemplateFiles
        fields = ["cover_photo", "template_image1", "template_image2", "template_image3", "template_image4", "template_file"]

class ThreeTemplateImageFileForm(forms.ModelForm):
    class Meta:
        model = ThreeTemplateFiles
        fields = ["cover_photo", "template_image1", "template_image2", "template_image3", "template_file"]

class TwoTemplateImageFileForm(forms.ModelForm):
    class Meta:
        model = TwoTemplateFiles
        fields = ["cover_photo", "template_image1", "template_image2", "template_file"]

class OneTemplateImageFileForm(forms.ModelForm):
    class Meta:
        model = OneTemplateFiles
        fields = ["cover_photo", "template_image1", "template_file"]