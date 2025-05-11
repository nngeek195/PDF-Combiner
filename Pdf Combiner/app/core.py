import os
from PyPDF2 import PdfReader, PdfWriter

def combine_pdfs(pdf_folder, output_path):
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
    pdf_files.sort()

    if not pdf_files:
        return "No PDF files found."

    pdf_writer = PdfWriter()

    try:
        for filename in pdf_files:
            file_path = os.path.join(pdf_folder, filename)
            reader = PdfReader(file_path)

            for page in reader.pages:
                pdf_writer.add_page(page)

        with open(output_path, 'wb') as out_file:
            pdf_writer.write(out_file)

        return f"Successfully merged {len(pdf_files)} PDFs into '{output_path}'"
    except Exception as e:
        return f"Error merging PDFs: {e}"