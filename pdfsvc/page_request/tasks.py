import io
import time

from weasyprint import HTML
from django.core.files import File
from .models import PageRequest


def pdf(page):
    # post_save fires after the save but before the transaction is commited 
    time.sleep(1)
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
