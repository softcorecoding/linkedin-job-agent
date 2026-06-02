import argparse
import json
import re
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, SimpleDocTemplate


OUT_DIR = Path("tailor_cv")


def cv_filename(data):
    name_slug = slugify(data["candidate"]["name"]).lower()
    return f"{name_slug}_cv.pdf"


def slugify(value):
    value = re.sub(r"[^A-Za-z0-9]+", "_", value).strip("_")
    return re.sub(r"_+", "_", value)


def rich_text(value):
    if isinstance(value, dict):
        if "label" in value and "text" in value:
            return f"<b>{escape(value['label'])}:</b> {escape(value['text'])}"
        raise ValueError(f"Unsupported rich text object: {value}")
    return escape(str(value))


def para_text(value):
    if isinstance(value, list):
        return "<br/>".join(rich_text(item) for item in value)
    return rich_text(value)


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="CandidateName",
            parent=styles["Normal"],
            fontName="Helvetica-Bold",
            fontSize=16,
            leading=18,
            alignment=TA_CENTER,
            spaceAfter=2,
        )
    )
    styles.add(
        ParagraphStyle(
            name="ContactLine",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=8.7,
            leading=10,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#333333"),
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SectionHeading",
            parent=styles["Normal"],
            fontName="Helvetica-Bold",
            fontSize=10.5,
            leading=12,
            textColor=colors.HexColor("#1F4E79"),
            spaceBefore=8,
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="EntryHeading",
            parent=styles["Normal"],
            fontName="Helvetica-Bold",
            fontSize=9.7,
            leading=11,
            spaceBefore=3,
            spaceAfter=1,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SubtleLine",
            parent=styles["Normal"],
            fontName="Helvetica-Oblique",
            fontSize=8.8,
            leading=10,
            textColor=colors.HexColor("#444444"),
            spaceAfter=3,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CVBody",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=8.5,
            leading=10.5,
            alignment=TA_LEFT,
            spaceAfter=3,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CVBullet",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=8,
            leading=10.3,
            bulletFontName="Helvetica",
            bulletFontSize=6.5,
            bulletIndent=0,
            leftIndent=10,
            firstLineIndent=0,
            spaceAfter=2,
        )
    )
    return styles


def add_bullets(story, items, styles):
    for item in items:
        story.append(Paragraph(para_text(item), styles["CVBullet"], bulletText="•"))


def add_header(story, styles, candidate, subtitle):
    story.append(Paragraph(escape(candidate["name"]), styles["CandidateName"]))
    story.append(Paragraph(escape(subtitle), styles["ContactLine"]))
    story.append(Paragraph(escape(candidate["contact"]), styles["ContactLine"]))


def add_cv_section(story, styles, section):
    story.append(Paragraph(escape(section["title"]), styles["SectionHeading"]))
    for text in section.get("paragraphs", []):
        story.append(Paragraph(para_text(text), styles["CVBody"]))
    for entry in section.get("entries", []):
        story.append(Paragraph(escape(entry["heading"]), styles["EntryHeading"]))
        if entry.get("meta"):
            story.append(Paragraph(escape(entry["meta"]), styles["SubtleLine"]))
        for text in entry.get("paragraphs", []):
            story.append(Paragraph(para_text(text), styles["CVBody"]))
        for subsection in entry.get("subsections", []):
            if subsection.get("heading"):
                story.append(Paragraph(escape(subsection["heading"]), styles["EntryHeading"]))
            if subsection.get("paragraphs"):
                for text in subsection["paragraphs"]:
                    story.append(Paragraph(para_text(text), styles["CVBody"]))
            if subsection.get("bullets"):
                add_bullets(story, subsection["bullets"], styles)
        if entry.get("bullets"):
            add_bullets(story, entry["bullets"], styles)


def application_slug(data):
    if data.get("output_base"):
        return slugify(data["output_base"])
    return slugify(f"{data['company']}_{data['role']}")


def output_dir(data):
    return OUT_DIR / application_slug(data)


def stage_json_in_output(input_path, data):
    destination = output_dir(data) / f"{application_slug(data)}.json"
    source = input_path.resolve()
    if source != destination.resolve():
        input_path.replace(destination)
    return destination


def build_cv(data, styles):
    path = output_dir(data) / cv_filename(data)
    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        rightMargin=1.35 * cm,
        leftMargin=1.35 * cm,
        topMargin=1.2 * cm,
        bottomMargin=1.15 * cm,
    )
    story = []
    add_header(story, styles, data["candidate"], data["cv"]["subtitle"])
    for section in data["cv"]["sections"]:
        add_cv_section(story, styles, section)
    doc.build(story)
    return path


def main():
    parser = argparse.ArgumentParser(description="Generate a tailored CV PDF from JSON content.")
    parser.add_argument("input", help="Path to a tailoring JSON file.")
    args = parser.parse_args()

    input_path = Path(args.input)
    data = json.loads(input_path.read_text(encoding="utf-8"))
    output_dir(data).mkdir(parents=True, exist_ok=True)
    json_path = stage_json_in_output(input_path, data)
    styles = build_styles()
    cv_path = build_cv(data, styles)
    print(json_path)
    print(cv_path)


if __name__ == "__main__":
    main()
