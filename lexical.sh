#!/bin/sh
NAME="modelname"
OUTFOLDER="outputdir"/$NAME
mkdir $OUTFOLDER
MFOLDER="modeldir"/$NAME/"exp"

source activate fastvgs
module load matlab
M="EpochX_bundle.pth"
for LAYERNAME in 0 1 2 3 4 5 6 7 8 9 10 11
do
    OUTNAME="EXLayer"$LAYERNAME
    OUTFILE=$OUTFOLDER/$OUTNAME
    python lexical.py --target_layer $LAYERNAME --twd $MFOLDER/$M
    mkdir $OUTFILE
    cd /path/to/lextest/folder/
    sh CDI_lextest.sh '/path/to/lextest/data/CDI/' '/path/to/save/embeddings/lextest/' 'full' 1 $OUTFILE
    rm -r '/path/to/save/embeddings/'
done

