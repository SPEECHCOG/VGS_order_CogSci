#!/bin/sh
NAME="modelname"
OUTFOLDER="/path/to/ZeroSpeech/output/AC"/$NAME
mkdir $OUTFOLDER
MFOLDER="/path/to/model"/$NAME/"exp"


M="EX_bundle.pth"

OUTNAME="EXLayer0"
OUTFILE=$OUTFOLDER/$OUTNAME
source activate fastvgs
python abx.py --target_layer 0 --twd $MFOLDER/$M
conda activate zerospeech2021
mkdir $OUTFILE
zerospeech2021-evaluate /path/to/ZeroSpeech/data/  /path/to/ZeroSpeech/submission/ -o $OUTFILE -j12 --no-lexical --no-syntactic --no-semantic --force-cpu
rm -r /path/to/ZeroSpeech/submission/phonetic/dev-clean

for LAYERNAME in 1 2 3 4 5 6 7 8 9 10 11
do
    OUTNAME="EXLayer"$LAYERNAME
    OUTFILE=$OUTFOLDER/$OUTNAME
    conda activate fastvgs
    python abx.py --target_layer $LAYERNAME --twd $MFOLDER/$M
    conda activate zerospeech2021
    mkdir $OUTFILE
    zerospeech2021-evaluate /path/to/ZeroSpeech/data/  /path/to/ZeroSpeech/submission/ -o $OUTFILE -j12 --no-lexical --no-syntactic --no-semantic --force-cpu
    rm -r /path/to/ZeroSpeech/submission/phonetic/dev-clean
done


