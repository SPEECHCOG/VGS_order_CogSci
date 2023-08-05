# VGS_seq_or_parallel_CogSci

This repository contains the instructions and scripts to replicate experiments reported in Khorrami, Cruz Blandon & Räsänen: Computational Insights to Acquisition of Phonemes, Words, and Word Meanings in Early Language: Sequential or Parallel Acquisition? Proc. CogSci-2023, Sydney, Australia. Accepted for publication. 

# Model Source

This project's model is based on the work from the following repository:

https://github.com/jasonppy/FaST-VGS-Family

Please make sure to check out the original repository and give credit to the creators for their contributions. 

For setting the weight of the audio (SSL) and audio-visual (VGS) losses (i.e., alpha coefficient), you need to modify the "weight_loss" function within the "steps/trainer.py" file of the model's source code. 

# Model Description

The VGS+ model combines a wav2vec 2.0-based speech self-supervised learning (SSL) and a transformer-based visually grounded speech (VGS) learning mechanisms within one model. It has shown that the speech representations obtained from hidden layers of the trained VGS+ model contain phonemic and lexical information. 

# How to Use

## Phoneme discrimination score

For obtaining the speech representations from a hidden layer of the speech encoder and decoder, please first provide the input (data) and output (speech representations) path within the "abx.py" file. 

For measuring the ABX phoneme discrimination score, please follow the instructions in following repository:

https://github.com/zerospeech/zerospeech2021

You can use the template provided at "abx.sh" to obtain abx score for different layers (0:11) of any specific model (specified by the path to the bundle file of the model). 

For test data, you need to download dev-clean subset of LibriSpeech data from https://www.openslr.org/12 .

## Lexical score

For obtaining the speech representations from a hidden layer of the speech encoder and decoder, please first provide the input (data) and output (speech representations) path within the "lexical.py" file.

For measuring the lexical score, please follow the instruction in the following repository:

https://github.com/SPEECHCOG/CDI_lextest

You can use the template provided at "lexica.sh" to obtain lexical score for different layers (0:11) of any specific model (specified by the path to the bundle file of the model). 
