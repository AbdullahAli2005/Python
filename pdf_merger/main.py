import PyPDF2
import os

pdf_files = ['1.pdf' , '2.pdf']

# PDF Merger Object
merger = PyPDF2.PdfMerger()

for pdf in pdf_files:
    if os.path.exists(pdf):
        merger.append(pdf)
    else:
        print(f"File {pdf} does not exist and will be skipped.")

output_pdf = 'merged_output.pdf'
merger.write(output_pdf)
merger.close()

print(f"PDF files merged successfully into {output_pdf}.")