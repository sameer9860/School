import base64
from datetime import date, timedelta

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from academics.models import Curriculum
from core.models import PrincipalMessage, SchoolInfo, Slider
from events.models import Event
from gallery.models import GalleryItem
from notices.models import Notice


# 1x1 transparent PNG
_PNG_1X1 = base64.b64decode(
    b"iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMB/6X9l9cAAAAASUVORK5CYII="
)


def _img_file(name: str) -> ContentFile:
    f = ContentFile(_PNG_1X1)
    f.name = name
    return f


def _text_file(name: str, text: str) -> ContentFile:
    f = ContentFile(text.encode("utf-8"))
    f.name = name
    return f


class Command(BaseCommand):
    help = "Seed demo data for admin (slider, principal, notices, events, gallery, curriculum)."

    def add_arguments(self, parser):
        parser.add_argument(
            "--with-superuser",
            action="store_true",
            help="Create demo superuser if no users exist (admin/admin123).",
        )

    def handle(self, *args, **options):
        # Ensure MEDIA_ROOT exists
        settings.MEDIA_ROOT.mkdir(parents=True, exist_ok=True)

        User = get_user_model()
        if options["with_superuser"] and not User.objects.exists():
            extra_fields = {}
            field_names = {f.name for f in User._meta.fields}
            if "role" in field_names:
                extra_fields["role"] = "admin"
            User.objects.create_superuser(
                username="admin",
                email="admin@example.com",
                password="admin123",
                **extra_fields,
            )

        admin_user = User.objects.first() if User.objects.exists() else None

        school, _ = SchoolInfo.objects.get_or_create(
            name="ABC School",
            defaults={
                "address": "Jawalakhel, Lalitpur, Nepal",
                "phone": "01-5421050, 01-5421150",
                "email": "info@abcschool.edu.np",
                "about": (
                    "Welcome to ABC School. We are committed to quality education, "
                    "discipline, and holistic development of students."
                ),
            },
        )

        PrincipalMessage.objects.get_or_create(
            name="Principal",
            defaults={
                "message": (
                    "Namaste!\n\nWelcome to ABC School. Our focus is on competence, "
                    "conscience, commitment, and compassion."
                ),
                "photo": _img_file("principal/demo-principal.png"),
            },
        )

        if not Slider.objects.exists():
            Slider.objects.create(
                title="Welcome to ABC School",
                description="Quality Education in Nepal",
                image=_img_file("slider/slide-1.png"),
            )
            Slider.objects.create(
                title="Admissions Open",
                description="Enroll now for the new academic session",
                image=_img_file("slider/slide-2.png"),
            )
            Slider.objects.create(
                title="Sports & Activities",
                description="Balanced learning with extra-curricular excellence",
                image=_img_file("slider/slide-3.png"),
            )

        if not Notice.objects.exists():
            for i in range(1, 8):
                Notice.objects.create(
                    title=f"Notice {i}: School update",
                    description="This is a demo notice. Replace it from admin with real content.",
                    created_by=admin_user,
                )

        if not Event.objects.exists():
            today = date.today()
            for i, title in enumerate(["Sports Week", "Annual Function", "Science Exhibition"], start=1):
                Event.objects.create(
                    title=title,
                    description="This is a demo event. Update details in admin.",
                    event_date=today + timedelta(days=i * 7),
                    image=_img_file(f"events/event-{i}.png"),
                )

        if not GalleryItem.objects.exists():
            GalleryItem.objects.create(
                title="School Campus (Demo Photo)",
                category="photo",
                image=_img_file("gallery/demo-photo-1.png"),
            )
            GalleryItem.objects.create(
                title="Annual Function Highlights (Demo Video)",
                category="video",
                video_url="https://www.youtube.com/embed/dQw4w9WgXcQ",
            )
            GalleryItem.objects.create(
                title="Science Exhibition (Demo Video)",
                category="video",
                video_url="https://www.youtube.com/embed/tgbNymZ7vqY",
            )

        if not Curriculum.objects.exists():
            Curriculum.objects.create(
                class_name="Grade 1-3",
                description="Demo curriculum outline for Grade 1-3.",
                file=_text_file("curriculum/grade-1-3.txt", "Demo curriculum file."),
            )
            Curriculum.objects.create(
                class_name="Grade 4-5",
                description="Demo curriculum outline for Grade 4-5.",
                file=_text_file("curriculum/grade-4-5.txt", "Demo curriculum file."),
            )
            Curriculum.objects.create(
                class_name="Grade 6-8",
                description="Demo curriculum outline for Grade 6-8.",
                file=_text_file("curriculum/grade-6-8.txt", "Demo curriculum file."),
            )

        self.stdout.write(self.style.SUCCESS("Demo data seeded."))

