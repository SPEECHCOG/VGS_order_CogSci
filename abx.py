import os
#############################################################################
#twd = '/path/to/model/bundle.pth'
#target_layer = 0:11
total_layers = 12
trimTF = True
subset_name = 'dev_clean'

# Paths for LibriSpeech input and output
wav_path = '/path/to/ZeroSpeech/data/phonetic/'
audio_dataset_json_file = '/path/to/ZeroSpeech/data/phonetic/index.json'
save_path = '/path/to/ZeroSpeech/submission/phonetic/'
os.makedirs(save_path + 'dev-clean', exist_ok=True)

#############################################################################
# for data
import argparse
import soundfile as sf
import numpy as np
import torch
import json
import numpy
# for model
from models.w2v2_model import  Wav2Vec2Model_cls , ConvFeatureExtractionModel
from steps import trainer
from steps.utils import *
from steps.trainer_utils import *
from models import fast_vgs, w2v2_model
from datasets import spokencoco_dataset, libri_dataset
#############################################################################

def LoadAudio( path):
    x, sr = sf.read(path, dtype = 'float32')
    assert sr == 16000
    length_orig = len(x)
    audio_length = length_orig
    x_norm = (x - np.mean(x)) / np.std(x)
      
    return x_norm, audio_length

#############################################################################
# loading data
print ('............. it is reading audio json file .................')
with open(audio_dataset_json_file, 'r') as fp:
    data_json = json.load(fp)
    
test_clean = data_json['subsets'][subset_name]
wav_files_json = test_clean['items']['wav_list']['files_list']

#############################################################################
# loading Model
device = 'cpu'
# adding all args
parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--twd", help="the model dir")
parser.add_argument("--target_layer", help="the target layer")
#..............................................................................

parser.add_argument("--resume", action="store_true", dest="resume", help="load from exp_dir if True")
parser.add_argument("--validate", action="store_true", default=False, help="temp, if call trainer_variants rather than trainer")
parser.add_argument("--test", action="store_true", default=False, help="test the model on test set")
trainer.Trainer.add_args(parser)
w2v2_model.Wav2Vec2Model_cls.add_args(parser)
fast_vgs.DualEncoder.add_args(parser)
spokencoco_dataset.ImageCaptionDataset.add_args(parser)
libri_dataset.LibriDataset.add_args(parser)
args = parser.parse_args()
#..............................

# input args
twd = args.twd
args.layer_use = int(args.target_layer)
# fixed args
args.encoder_layers = total_layers
args.trim_mask = trimTF
args.normalize = True
args.encoder_attention_heads = 12

print ('###############################')
print(args)
print ('###############################')

############################################## defining the model based on ARGS
#..............................
conv1_trm1_trm3 = Wav2Vec2Model_cls(args)
conv1_trm1_trm3.to(device)
conv1_trm1_trm3.eval()


# loading Pre-trained weights

bundle = torch.load(twd)
conv1_trm1_trm3.carefully_load_state_dict(bundle['dual_encoder'])

#############################################################################

# changing device to gpu
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
conv1_trm1_trm3.to(device)
conv1_trm1_trm3.eval()

with torch.no_grad():
    for counter, wav_file in enumerate(wav_files_json):
        print(counter)
        signal_peng,l =  LoadAudio(wav_path + wav_file) 
        
        audio_signal = torch.tensor(signal_peng ,dtype=torch.float).to(device)
        input_signal = audio_signal.view(1, -1)
        trm13_out = conv1_trm1_trm3(input_signal,  mask=False, features_only=True, tgt_layer=args.layer_use)
        trm13_out_features = trm13_out['layer_feats']
        output_tensor = trm13_out_features[0]
        output_np_arr = output_tensor.cpu().detach().numpy()
        #print(len(output_np_arr))
        numpy.savetxt(save_path + wav_file [0:-4] + '.txt', output_np_arr )
        
        torch.cuda.empty_cache()
        del trm13_out,trm13_out_features,output_tensor,output_np_arr

