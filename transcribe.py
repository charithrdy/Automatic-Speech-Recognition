#!/usr/bin/env python3

import os
import config

def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return


def to_wav(input_dir = None, filename = None, output_dir = None, output_filename = None, sampling_rate = '16000', bit_rate = '16'):
    mkdir(output_dir)
    os.system(' '.join(['ffmpeg', '-i', input_dir+filename, '-ar', sampling_rate, '-ac', '1',
						'-ab', bit_rate, output_dir+output_filename, '-y']))
    return 

if __name__ == "__main__":
    # Paths
    input_dir = config.input_dir
    wav_dir = config.wav_dir
    model_dir = config.deepspeech_models
    output_dir = config.output_dir
    # Create output dir
    mkdir(output_dir)
    files = os.listdir(input_dir)
    try: files.remove('.DS_Store')
    except: pass
    files.sort()
    for file in files:
        # convert to 16kHz and 16bit wav
        converted_filename = file[:-4]+'_16khz.wav'
        to_wav(input_dir = input_dir, filename=file, output_dir = wav_dir,output_filename=converted_filename,sampling_rate='16000', bit_rate = '16')

        if config.deepspeech:
            command = 'deepspeech --model {0}deepspeech-0.8.1-models.pbmm --scorer {0}deepspeech-0.8.1-models.scorer --audio {1} >> {2}'.format(model_dir, wav_dir+converted_filename, output_dir+file[:-4]+'_deepspeech.txt')
            os.system(command)
    if config.remove_wav_dir:
        os.system('rm -r '+config.wav_dir)






