#!/bin/bash

minimap2 -x ava-ont -t32 /webapp/media/ecoli.fasta /webapp/media/ecoli.fasta -K5M | gzip -1 > /webapp/media/ecoli.paf.gz
miniasm -2S6 -f/webapp/media/ecoli.fasta /webapp/media/ecoli.paf.gz > /webapp/media/ecoli.gfa
grep '^S' /webapp/media/ecoli.gfa | awk '{print">"$2"\n"$3}' > /webapp/media/ecoli_contigs.fasta
abricate  /webapp/media/ecoli_contigs.fasta > /webapp/media/myfiles
grep ">" ${file}_contigs.fasta | wc -l
assembly-stats ./${file}_contigs.fasta



