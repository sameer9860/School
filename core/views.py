from django.shortcuts import render

from academics.models import Class, Subject
from academics.models import Curriculum
from admissions.models import Admission
from notices.models import Notice
from gallery.models import GalleryItem
from events.models import Event

from core.models import ContactMessage, PrincipalMessage, SchoolInfo, Slider


def home(request):
    sliders = Slider.objects.all()
    principal = PrincipalMessage.objects.first()
    notices = Notice.objects.order_by("-created_at")[:6]
    events = Event.objects.order_by("-event_date")[:3]
    news = Notice.objects.order_by("-created_at")[6:9]
    videos = GalleryItem.objects.filter(category="video").order_by("-uploaded_at")[:3]
    return render(
        request,
        "core/home.html",
        {
            "sliders": sliders,
            "principal": principal,
            "notices": notices,
            "events": events,
            "news": news,
            "videos": videos,
        },
    )


def about(request):
    school = SchoolInfo.objects.first()
    return render(request, "core/about.html", {"school": school})


def academics(request):
    classes = Class.objects.order_by("name", "section")
    subjects = Subject.objects.select_related("class_name").order_by("class_name__name", "name")
    return render(
        request,
        "core/academics.html",
        {
            "classes": classes,
            "subjects": subjects,
        },
    )


def admissions(request):
    if request.method == "POST":
        payload = {
            "student_name": request.POST.get("student_name", "").strip(),
            "date_of_birth": request.POST.get("date_of_birth"),
            "class_applying": request.POST.get("class_applying", "").strip(),
            "parent_name": request.POST.get("parent_name", "").strip(),
            "phone": request.POST.get("phone", "").strip(),
            "address": request.POST.get("address", "").strip(),
        }
        document = request.FILES.get("document")

        errors = {}
        for k, v in payload.items():
            if not v:
                errors[k] = "This field is required."
        if not document:
            errors["document"] = "Please upload a document."

        if not errors:
            Admission.objects.create(**payload, document=document)
            return render(request, "core/admissions_success.html")

        return render(request, "core/admissions.html", {"errors": errors, "data": payload})

    return render(request, "core/admissions.html", {"errors": {}, "data": {}})


def notices(request):
    notices_qs = Notice.objects.order_by("-created_at")
    return render(request, "core/notices.html", {"notices": notices_qs})


def contact(request):
    if request.method == "POST":
        payload = {
            "name": request.POST.get("name", "").strip(),
            "email": request.POST.get("email", "").strip(),
            "message": request.POST.get("message", "").strip(),
        }
        errors = {k: "This field is required." for k, v in payload.items() if not v}

        if not errors:
            ContactMessage.objects.create(**payload)
            return render(request, "core/contact_success.html")

        return render(request, "core/contact.html", {"errors": errors, "data": payload})

    return render(request, "core/contact.html", {"errors": {}, "data": {}})


def gallery(request):
    items = GalleryItem.objects.order_by("-uploaded_at")
    return render(request, "core/gallery.html", {"items": items})


def curriculum(request):
    data = Curriculum.objects.order_by("class_name")
    return render(request, "core/curriculum.html", {"data": data})
