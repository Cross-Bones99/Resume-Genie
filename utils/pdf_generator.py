from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.platypus import Spacer
from reportlab.lib.styles import getSampleStyleSheet

import io


def create_cover_letter_pdf(cover_letter):

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    elements = []

    paragraph = Paragraph(
        cover_letter.replace("\n", "<br/>"),
        styles["Normal"]
    )

    elements.append(paragraph)

    elements.append(Spacer(1, 12))

    doc.build(elements)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf
