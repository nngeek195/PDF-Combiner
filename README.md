# PDF Combiner
PDF Combiner is a lightweight and user-friendly desktop application built in Python that allows you to merge multiple PDF files into a single document effortlessly. Whether you're organizing reports, assignments, or any multi-page documents, this tool makes it easy with a simple interface and intuitive workflow.

## Why Use PDF Combiner?
- Simple & Lightweight : No bloated dependencies or complex setup.
- No External Software Needed : Works standalone — no need to install additional tools.
- Sort by Name or Custom Order : Combine PDFs in alphabetical order or drag-and-drop to customize the sequence.
- Cross-Platform : Built using Python, works on Windows, macOS, and Linux.
- Fast & Reliable : Merges hundreds of pages in seconds without losing quality.

  
🧩 How It Works
This app lets you:
  Select multiple PDF files from your computer
  View the list of selected files
  Reorder them if needed
  Combine them into one PDF file
  Save the output to your desired location
  The merging process follows alphabetical order by default , but also supports manual reordering via drag-and-drop.

### For Developers
Prerequisites
Python 3.x
PyInstaller (to build the .exe)
Required libraries: PyQt5, PyPDF2, or similar PDF handling library

```bash
    # Clone the repository
    git clone https://github.com/yourusername/pdf-combiner.git 
    cd pdf-combiner
    
    # Create and activate virtual environment
    python -m venv .venv
    .venv\Scripts\activate   # On Windows
    source .venv/bin/activate # On macOS/Linux
    
    # Install dependencies
    pip install pyqt5 pypdf2
```

### For Users
1.  Steps to Use the App
- Download the Executable
    Go to the dist/ folder in the repo.
2.  Download the PDFCombiner.exe (or equivalent for macOS/Linux).
- Run the Application
    Double-click the executable to launch the app.
3.  Select PDF Files
  - Click "Add PDFs" to select multiple PDF files from your computer.
4.  You can manually reorder them using drag-and-drop.
  - Combine PDFs
    Click "Combine PDFs" .
    Choose the save location and confirm.
5. Done!
    Your merged PDF will be saved at the specified location.


![7eef9795-01b9-466d-be3f-282eb0631a4f1](https://github.com/user-attachments/assets/95ebf266-c02e-499e-a23a-37e760ac97d1)
