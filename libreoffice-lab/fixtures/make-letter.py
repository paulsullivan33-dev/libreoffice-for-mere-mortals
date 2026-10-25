#!/usr/bin/env python3
"""Create the guide's letter fixture: harbour-letter.docx.

A short letter from an invented friends-of-the-lighthouse
group, with a heading, a list and a table -- enough real
structure to prove that a conversion kept it.
"""
from docx import Document
from docx.shared import Pt

doc = Document()

doc.add_heading("Friends of Harbour Light", level=1)
doc.add_paragraph("Harbour Road, Port Sable")
doc.add_paragraph("12 November 2026")

doc.add_paragraph("Dear Member,")

doc.add_paragraph(
    "The lighthouse museum closes for its winter refit on "
    "Sunday 30 November. This letter sets out the winter "
    "opening hours and the two volunteer days we are asking "
    "members to cover."
)

doc.add_paragraph(
    "From 1 December the museum and shop will open as follows:"
)

hours = doc.add_table(rows=1, cols=2)
hours.style = "Light Grid Accent 1"
hours.rows[0].cells[0].text = "Day"
hours.rows[0].cells[1].text = "Hours"
for day, hrs in [
    ("Wednesday", "10:00 - 15:00"),
    ("Saturday", "10:00 - 16:00"),
    ("Sunday", "11:00 - 15:00"),
]:
    row = hours.add_row().cells
    row[0].text = day
    row[1].text = hrs

doc.add_paragraph("")
p = doc.add_paragraph()
p.add_run("Volunteer days. ").bold = True
p.add_run(
    "We need two members for the lantern-room clean on "
    "Saturday 6 December and two more for the archive "
    "sorting on Saturday 13 December. No experience is "
    "needed; bring gloves and a flask."
)

bullets = [
    "Lantern-room clean - Saturday 6 December, 09:30",
    "Archive sorting - Saturday 13 December, 09:30",
    "Carol evening in the lamp room - Friday 19 December, 18:30",
]
for b in bullets:
    doc.add_paragraph(b, style="List Bullet")

p = doc.add_paragraph()
p.add_run("The tower itself stays closed until March. ").italic = True
p.add_run(
    "The stairs are being re-pointed, and the scaffolding "
    "makes a fine photograph even if it spoils the view."
)

doc.add_paragraph("Thank you, as ever, for keeping the light on.")
doc.add_paragraph("Margaret Ellison")
doc.add_paragraph("Secretary, Friends of Harbour Light")

doc.save("harbour-letter.docx")
print("wrote harbour-letter.docx")
