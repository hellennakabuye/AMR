# AMR

These scripts are part of a major Django web application that analyses minION sequences for antimicrobial resistance genes, and produces a PDF file containing results.

The fasta.sh contains shell/bash script that analyses the input fasta file in 4 steps, using miniasm and minimap2

The views.py file contains the preprocessing code for the input fasta file using SeqIO of Biopython and then analyses the results of the fasta.sh script to output a PDF file of the results.

The results file contains the AMR genes found, plus the antibiotics they infer resistance to.
