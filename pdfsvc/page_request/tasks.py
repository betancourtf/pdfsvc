import io

from weasyprint import HTML
from django.core.files import File

from .models import PageRequest
from pdfsvc.celery import app


@app.task(time_limit=120)
def pdf(page_id):
    page = PageRequest.objects.get(pk=page_id)
    if page.status != page.Status.PENDING:
        return
    page.status = PageRequest.Status.GENERATING
    page.save()
    try:
        html = HTML(url=page.url)
    except Exception as e:
        page.status = PageRequest.Status.ERROR
        page.error_msg = str(e)
        page.save()
        return
    try:
        pdf_in_memory = io.BytesIO()
        html.write_pdf(target=pdf_in_memory)
    except Exception as e:
        page.status = PageRequest.Status.ERROR
        page.error_msg = str(e)
        page.save()
        return
    page.pdf_file = File(pdf_in_memory, f"{page.pk}.pdf")
    page.status = PageRequest.Status.READY
    page.save()
