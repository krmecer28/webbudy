from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import TemplateForm, OneTemplateImageFileForm, TwoTemplateImageFileForm, ThreeTemplateImageFileForm, FourTemplateImageFileForm, FiveTemplateImageFileForm, SixTemplateImageFileForm, SevenTemplateImageFileForm, EightTemplateImageFileForm, NineTemplateImageFileForm, TenTemplateImageFileForm
from django.contrib import messages
from .models import WebTemplates
from random import shuffle

from django.contrib.auth.decorators import login_required

# Create your views here.
def templates(request):
    templates = WebTemplates.objects.all()
    
    return render(request, "templates.html", {"templates": templates})

def index(request):
    temps = list()
    counter = 0

    for template in WebTemplates.objects.all():
        temps.append(template)
        counter += 1

        if (counter > 4):
            break

    shuffle(temps)
    return render(request, 'index.html', {"temps": temps})

def about(request):
    return render(request, 'about.html')

@login_required(login_url="user:login")
def addTemplate(request):
    form = TemplateForm(request.POST or None)

    if form.is_valid():
        template = form.save(commit=False)
        template.author = request.user
        template.save()

        messages.success(request, "Template Created Successfully. Please upload your images to publish your template")
        return redirect("webtemplates:dashboard")
    
    return render(request, 'addtemplate.html', {"form": form})

@login_required(login_url="user:login")
def dashboard(request):
    templates = WebTemplates.objects.filter(author = request.user)

    context = {
        "templates": templates,
    }

    return render(request, 'dashboard.html', context)

@login_required(login_url="user:login")
def deleteTemplate(request, id):
    template = get_object_or_404(WebTemplates, id = id)
    template.delete()
    messages.success(request, "Template Deleted Successfully")

    return redirect("webtemplates:dashboard")

@login_required(login_url="user:login")
def uploadImages(request, id):
    template = WebTemplates.objects.filter(id = id).first()
    print(template.title)

    if template.page_number == 1:
        form = OneTemplateImageFileForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            templatefiles = form.save(commit=False)
            templatefiles.title = WebTemplates.objects.filter(id = id).first().title
            templatefiles.save()

            template.cover_photo = templatefiles.cover_photo
            template.template_image1 = templatefiles.template_image1
            template.template_file = templatefiles.template_file
            template.save()

            messages.success(request, "Successfully added your files")
            return redirect("webtemplates:dashboard")
        return render(request, "addfiles.html", {"form": form})
    
    elif template.page_number == 2:
        form = TwoTemplateImageFileForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            templatefiles = form.save(commit=False)
            templatefiles.template = template.title
            templatefiles.save()

            template.cover_photo = templatefiles.cover_photo
            template.template_image1 = templatefiles.template_image1
            template.template_image2 = templatefiles.template_image2
            template.template_file = templatefiles.template_file
            template.save()

            messages.success(request, "Successfully added your files")
            return redirect("webtemplates:dashboard")
        return render(request, "addfiles.html", {"form": form})
    
    elif template.page_number == 3:
        form = ThreeTemplateImageFileForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            templatefiles = form.save(commit=False)
            templatefiles.template = template.title
            templatefiles.save()

            template.cover_photo = templatefiles.cover_photo
            template.template_image1 = templatefiles.template_image1
            template.template_image2 = templatefiles.template_image2
            template.template_image3 = templatefiles.template_image3
            template.template_file = templatefiles.template_file
            template.save()

            messages.success(request, "Successfully added your files")
            return redirect("webtemplates:dashboard")
        return render(request, "addfiles.html", {"form": form})
    
    elif template.page_number == 4:
        form = FourTemplateImageFileForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            templatefiles = form.save(commit=False)
            templatefiles.template = template.title
            templatefiles.save()

            template.cover_photo = templatefiles.cover_photo
            template.template_image1 = templatefiles.template_image1
            template.template_image2 = templatefiles.template_image2
            template.template_image3 = templatefiles.template_image3
            template.template_image4 = templatefiles.template_image4
            template.template_file = templatefiles.template_file
            template.save()

            messages.success(request, "Successfully added your files")
            return redirect("webtemplates:dashboard")
        return render(request, "addfiles.html", {"form": form})
    
    elif template.page_number == 5:
        form = FiveTemplateImageFileForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            templatefiles = form.save(commit=False)
            templatefiles.template = template.title
            templatefiles.save()

            template.cover_photo = templatefiles.cover_photo
            template.template_image1 = templatefiles.template_image1
            template.template_image2 = templatefiles.template_image2
            template.template_image3 = templatefiles.template_image3
            template.template_image4 = templatefiles.template_image4
            template.template_image5 = templatefiles.template_image5
            template.template_file = templatefiles.template_file
            template.save()

            messages.success(request, "Successfully added your files")
            return redirect("webtemplates:dashboard")
        return render(request, "addfiles.html", {"form": form})
    
    elif template.page_number == 6:
        form = SixTemplateImageFileForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            templatefiles = form.save(commit=False)
            templatefiles.template = template.title
            templatefiles.save()

            template.cover_photo = templatefiles.cover_photo
            template.template_image1 = templatefiles.template_image1
            template.template_image2 = templatefiles.template_image2
            template.template_image3 = templatefiles.template_image3
            template.template_image4 = templatefiles.template_image4
            template.template_image5 = templatefiles.template_image5
            template.template_image6 = templatefiles.template_image6
            template.template_file = templatefiles.template_file
            template.save()

            messages.success(request, "Successfully added your files")
            return redirect("webtemplates:dashboard")
        return render(request, "addfiles.html", {"form": form})
    
    elif template.page_number == 7:
        form = SevenTemplateImageFileForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            templatefiles = form.save(commit=False)
            templatefiles.template = template.title
            templatefiles.save()

            template.cover_photo = templatefiles.cover_photo
            template.template_image1 = templatefiles.template_image1
            template.template_image2 = templatefiles.template_image2
            template.template_image3 = templatefiles.template_image3
            template.template_image4 = templatefiles.template_image4
            template.template_image5 = templatefiles.template_image5
            template.template_image6 = templatefiles.template_image6
            template.template_image7 = templatefiles.template_image7
            template.template_file = templatefiles.template_file
            template.save()

            messages.success(request, "Successfully added your files")
            return redirect("webtemplates:dashboard")
        return render(request, "addfiles.html", {"form": form})
    
    elif template.page_number == 8:
        form = EightTemplateImageFileForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            templatefiles = form.save(commit=False)
            templatefiles.template = template.title
            templatefiles.save()

            template.cover_photo = templatefiles.cover_photo
            template.template_image1 = templatefiles.template_image1
            template.template_image2 = templatefiles.template_image2
            template.template_image3 = templatefiles.template_image3
            template.template_image4 = templatefiles.template_image4
            template.template_image5 = templatefiles.template_image5
            template.template_image6 = templatefiles.template_image6
            template.template_image7 = templatefiles.template_image7
            template.template_image8 = templatefiles.template_image8
            template.template_file = templatefiles.template_file
            template.save()

            messages.success(request, "Successfully added your files")
            return redirect("webtemplates:dashboard")
        return render(request, "addfiles.html", {"form": form})
    
    elif template.page_number == 9:
        form = NineTemplateImageFileForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            templatefiles = form.save(commit=False)
            templatefiles.template = template.title
            templatefiles.save()

            template.cover_photo = templatefiles.cover_photo
            template.template_image1 = templatefiles.template_image1
            template.template_image2 = templatefiles.template_image2
            template.template_image3 = templatefiles.template_image3
            template.template_image4 = templatefiles.template_image4
            template.template_image5 = templatefiles.template_image5
            template.template_image6 = templatefiles.template_image6
            template.template_image7 = templatefiles.template_image7
            template.template_image8 = templatefiles.template_image8
            template.template_image9 = templatefiles.template_image9
            template.template_file = templatefiles.template_file
            template.save()

            messages.success(request, "Successfully added your files")
            return redirect("webtemplates:dashboard")
        return render(request, "addfiles.html", {"form": form})
    
    elif template.page_number == 10:
        form = TenTemplateImageFileForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            templatefiles = form.save(commit=False)
            templatefiles.template = template.title
            templatefiles.save()

            template.cover_photo = templatefiles.cover_photo
            template.template_image1 = templatefiles.template_image1
            template.template_image2 = templatefiles.template_image2
            template.template_image3 = templatefiles.template_image3
            template.template_image4 = templatefiles.template_image4
            template.template_image5 = templatefiles.template_image5
            template.template_image6 = templatefiles.template_image6
            template.template_image7 = templatefiles.template_image7
            template.template_image8 = templatefiles.template_image8
            template.template_image9 = templatefiles.template_image9
            template.template_image10 = templatefiles.template_image10
            template.template_file = templatefiles.template_file
            template.save()

            messages.success(request, "Successfully added your files")
            return redirect("webtemplates:dashboard")
        return render(request, "addfiles.html", {"form": form})
    

def detail(request, id):
    template = get_object_or_404(WebTemplates, id=id)
    return render(request, "detail.html", {"template": template})