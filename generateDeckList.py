from pyPdf import PdfFileWriter, PdfFileReader
import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import urllib2
import re
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

packet = StringIO.StringIO()
# create a new PDF with Reportlab
can = canvas.Canvas(packet, pagesize=letter)

f = open('decklist', 'r')

#Fill in the country and name
can.setFont('Helvetica', 12)

#Country
Country = str(f.readline().rstrip('\n'))
can.drawString(200, 905, Country)
print("Country : "+Country)

#Name
Name = str(f.readline().rstrip('\n'))
can.drawString(180, 877, Name)
print("Name : "+Name)

#Fill in the left column 
for i in range(830, 270, -23):
	serialno = str(f.readline().rstrip('\n'))
	#write the card no 
	can.setFont('Helvetica', 12)
	can.drawString(100, i, serialno)
	
	#perform the search via ws-tcg

	resp = urllib2.urlopen("https://ws-tcg.com/cardlist/?cardno="+serialno+"&l")
	respData = resp.read()
	paragraphs = re.findall(r'<td colspan="3">(.*?)<br>',str(respData))
	pdfmetrics.registerFont(UnicodeCIDFont('HeiseiMin-W3'))
	can.setFont('HeiseiMin-W3', 12)
	can.drawString(190, i, paragraphs[0])	
	print(str(serialno)+" : "+str(paragraphs[0]))

#Fill in the right column
for i in range(830, 270, -23):
	serialno = str(f.readline().rstrip('\n'))
	#write the card no 
	can.setFont('Helvetica', 12)
	can.drawString(420, i, serialno)
	
	#perform the search via ws-tcg
	resp = urllib2.urlopen("https://ws-tcg.com/cardlist/?cardno="+serialno+"&l")
	respData = resp.read()
	paragraphs = re.findall(r'<td colspan="3">(.*?)<br>',str(respData))
	pdfmetrics.registerFont(UnicodeCIDFont('HeiseiMin-W3'))
	can.setFont('HeiseiMin-W3', 12)
	can.drawString(510, i, paragraphs[0])	
	print(str(serialno)+" : "+str(paragraphs[0]))

#Favourite Card
serialno = str(f.readline().rstrip('\n'))
#write the card no 
can.setFont('Helvetica', 12)
can.drawString(420, 245, serialno)

resp = urllib2.urlopen("https://ws-tcg.com/cardlist/?cardno="+serialno+"&l")
respData = resp.read()
paragraphs = re.findall(r'<td colspan="3">(.*?)<br>',str(respData))
pdfmetrics.registerFont(UnicodeCIDFont('HeiseiMin-W3'))
can.setFont('HeiseiMin-W3', 12)
can.drawString(510, 245, paragraphs[0])	
print("Favourite card: "+ str(serialno)+" : "+str(paragraphs[0]))

can.save()
f.close()

#move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(file("template.pdf", "rb"))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
# finally, write "output" to a real file
outputStream = file("printout.pdf", "wb")
output.write(outputStream)
outputStream.close()