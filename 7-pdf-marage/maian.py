import PyPDF2

pdffiles = ["7-pdf-marage/1.pdf","7-pdf-marage/2.pdf"]  #here provide list of pdf that you want the mararge in the single
merger = PyPDF2.PdfMerger()

for filename in pdffiles:  
   pdfFile = open(filename,'rb')
   pdfReader = PyPDF2.PdfReader(pdfFile)
   merger.append(pdfReader)

pdfFile.close()
merger.write('merged.pdf')  #in name save the maraged pdf