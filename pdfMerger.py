from PyPDF2 import PdfMerger

merger = PdfMerger()
pdfs  = []

n = int(input("How many pdf you want to merge?\n"))

for i in range(n):
    name = input(f"Enter the Name of pdf {i+1} (with .pdf extension): ")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()

print("✅ Merged PDF saved as 'merged-pdf.pdf'")
