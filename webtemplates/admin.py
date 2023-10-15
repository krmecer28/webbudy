from django.contrib import admin
from .models import WebTemplates, OneTemplateFiles, TwoTemplateFiles, ThreeTemplateFiles, FourTemplateFiles, FiveTemplateFiles, SixTemplateFiles, SevenTemplateFiles, EightTemplateFiles, NineTemplateFiles, TenTemplateFiles

# Register your models here.
@admin.register(WebTemplates)
class WebTemplateAdmin(admin.ModelAdmin):

    list_display = ["title","author", "created_date"]
    search_fields = ["title"]
    list_filter = ["created_date"]
    class Meta:
        model = WebTemplates

@admin.register(OneTemplateFiles)
class OneTemplateFileAdmin(admin.ModelAdmin):
    list_display = ["title"]

    class meta:
        model = OneTemplateFiles

@admin.register(TwoTemplateFiles)
class TwoTemplateFileAdmin(admin.ModelAdmin):
    list_display = ["title"]

    class meta:
        model = TwoTemplateFiles

@admin.register(ThreeTemplateFiles)
class ThreeTemplateFileAdmin(admin.ModelAdmin):
    list_display = ["title"]

    class meta:
        model = ThreeTemplateFiles

@admin.register(FourTemplateFiles)
class FourTemplateFileAdmin(admin.ModelAdmin):
    list_display = ["title"]

    class meta:
        model = FourTemplateFiles

@admin.register(FiveTemplateFiles)
class FiveTemplateFileAdmin(admin.ModelAdmin):
    list_display = ["title"]

    class meta:
        model = FiveTemplateFiles

@admin.register(SixTemplateFiles)
class SixTemplateFileAdmin(admin.ModelAdmin):
    list_display = ["title"]

    class meta:
        model = SixTemplateFiles

@admin.register(SevenTemplateFiles)
class SevenTemplateFileAdmin(admin.ModelAdmin):
    list_display = ["title"]

    class meta:
        model = SevenTemplateFiles

@admin.register(EightTemplateFiles)
class EightTemplateFileAdmin(admin.ModelAdmin):
    list_display = ["title"]

    class meta:
        model = EightTemplateFiles

@admin.register(NineTemplateFiles)
class NineTemplateFileAdmin(admin.ModelAdmin):
    list_display = ["title"]

    class meta:
        model = NineTemplateFiles

@admin.register(TenTemplateFiles)
class TenTemplateFileAdmin(admin.ModelAdmin):
    list_display = ["title"]

    class meta:
        model = TenTemplateFiles