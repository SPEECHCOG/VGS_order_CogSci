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

[Provide instructions on how to use the model in your repository. Include installation steps, dependencies, and usage examples.]
