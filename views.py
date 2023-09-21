from django.shortcuts import render
from Bio import SeqIO
import subprocess
import pandas as pd
from fpdf import FPDF
# Create your views here.


def face(request):
    return render(request, 'face.html')


def fasta(request):
    if request.method == "POST":
        try:
            text_file = request.FILES['fasta']
            list_1, list_2 = sequence_extract_fasta(text_file)
            if '.fasta' in text_file.name:
                x, y, z = fasta_files(text_file)
                print(x)

            else:
                return render(request, 'add.html')

            context = {'files': text_file, 'z': z}
            return render(request, 'upload.html', context)
        except:
            text_file = ''
        context = {'files': text_file}

    return render(request, 'face.html')


def sequence_extract_fasta(fasta_file):
    # Defining empty list for the Fasta id and fasta sequence variables
    fasta_id = []
    fasta_seq = []
    # fasta_file = fasta_file.chunks()
    # print(fasta_file)
    # opening given fasta file using the file path

    # crating a backup file with original uploaded file data
    with open('media/ecoli.fasta', 'wb+') as destination:
        for chunk in fasta_file.chunks():
            destination.write(chunk)

    # opening created backup file and reading
    with open('media/ecoli.fasta', 'r') as fasta_file:
        # extracting multiple data in single fasta file using biopython
        for record in SeqIO.parse(fasta_file, 'fasta'):  # (file handle, file format)

            fasta_seq.append(record.seq)
            fasta_id.append(record.id)

    # returning fasta_id and fasta sequence to both call_compare_fasta and call_reference_fasta

    return fasta_id, fasta_seq


def fasta_files(sequence):
    code = subprocess.run('myapp/fasta.sh', shell=True)

    file = pd.read_table('/webapp/media/myfiles')
    df = pd.DataFrame(file)
    print(df.shape)
    # print(df.head(5))
    result = df['RESISTANCE']
    sample = df.iloc[0,0]

    with open('/webapp/media/results.txt', 'w') as f:
        for word in result:
            f.write(word)
            f.write('\n')

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt="MINION-UGANDA PROJECT",
             ln=1, align='C')
    pdf.cell(200, 10, txt="AMR SEQUENCE ANALYSIS REPORT",
             ln=1, align='C')
    pdf.cell(200, 10, txt="Antibiotic resistance Found FOR THESE DRUGS:",
             ln=1, align='L')
    pdf.cell(200, 10, txt=sample, ln=1, align='C')
    f = open("/webapp/media/results.txt", "r")
    for x in f:
        pdf.cell(200, 10, txt=x, ln=1, align='L')

    report = pdf.output("/pilot.pdf")
    return code, report, result

