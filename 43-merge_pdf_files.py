"""
    If we want to merge PDF files, we can do it with Python. We
    can use the PyPDF2 module. With this module, you can
    merge as many files as you want. First, install the module using pip.
"""

import PyPDF2
from PyPDF2 import PdfMerger, PdfReader
# Create a list of files to merge
listl = ['file1.pdf', 'file2.pdf']
merge = PyPDF2.PdfMerger(strict=True)
for file in listl:
    merge.append(PdfReader(file,'rb+'))
    # Merge the files and name the merged file
    merge.write('mergedfile.pdf')
merge. close()
# Reading the created file
created_file = PdfReader('mergedfile.pdf')
created_file


"""
    For this code to run successfully, make sure that the files
    you are wanting to merge are saved in the same location as
    your Python file. Create a list of all the files that you are
    trying to merge. The output simply confirms that the
    merged file has been created. The name of the file is mergedfile.pdf
"""
