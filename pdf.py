from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph

def create_pdf(filename, userdata):
    my_doc = SimpleDocTemplate(filename)
    flowables = []
    my_doc.build(flowables)
    sample_style_sheet = getSampleStyleSheet()
    paragraph_1 = Paragraph("A title", sample_style_sheet['Heading1'])
    var = "this is %s user firstname, %s user lastname and age %d" % (userdata['firstname'],userdata['lastname'], userdata['age'])
    paragraph_2 = Paragraph(
       var, sample_style_sheet['BodyText'])
    flowables.append(paragraph_1)
    flowables.append(paragraph_2)
    my_doc.build(flowables)

