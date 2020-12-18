import PyPDF2

# with open('./scripting_pdf/213_dummy.pdf', 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     print(reader.numPages)


# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfFileMerger()
#     for pdf in pdf_list:
#         merger.append(pdf)
#     merger.write('super.pdf')


# pdf_combiner(['./scripting_pdf/213_dummy.pdf',
#               './scripting_pdf/213_twopage.pdf'])

template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))

watermark = PyPDF2.PdfFileReader(open('./scripting_pdf/215_wtr.pdf', 'rb'))

out = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    out.addPage(page)

    with open('water.pdf', 'wb') as file:
        out.write(file)
