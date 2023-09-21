#!/bin/bash

minimap2 -x ava-ont -t32 /home/nakabuye/Desktop/AMR_APP/webapp/media/ecoli.fasta /home/nakabuye/Desktop/AMR_APP/webapp/media/ecoli.fasta -K5M | gzip -1 > /home/nakabuye/Desktop/AMR_APP/webapp/media/ecoli.paf.gz
miniasm -2S6 -f /home/nakabuye/Desktop/AMR_APP/webapp/media/ecoli.fasta /home/nakabuye/Desktop/AMR_APP/webapp/media/ecoli.paf.gz > /home/nakabuye/Desktop/AMR_APP/webapp/media/ecoli.gfa
grep '^S' /home/nakabuye/Desktop/AMR_APP/webapp/media/ecoli.gfa | awk '{print">"$2"\n"$3}' > /home/nakabuye/Desktop/AMR_APP/webapp/media/ecoli_contigs.fasta
abricate  /home/nakabuye/Desktop/AMR_APP/webapp/media/ecoli_contigs.fasta > /home/nakabuye/Desktop/AMR_APP/webapp/media/myfiles
        # grep ">" ${file}_contigs.fasta | wc -l
        # assembly-stats ./${file}_contigs.fasta



