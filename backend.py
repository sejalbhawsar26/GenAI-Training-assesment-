import librosa
import soundfile as sf
import numpy as np

def change_pitch_and_speed(input_file, output_file, pitch_shift=0, time_stretch=1.0):
    try:
        y, sr = librosa.load(input_file, sr=None)
        if pitch_shift != 0:
            y = librosa.effects.pitch_shift(y, sr=sr, n_steps=pitch_shift)
        if time_stretch != 1.0:
            y = librosa.effects.time_stretch(y, rate=time_stretch)
        sf.write(output_file, y, sr)
        return True, None
    except Exception as e:
        return False, str(e)

def apply_style(input_file, output_file, style="chipmunk"):
    if style == "chipmunk":
        return change_pitch_and_speed(input_file, output_file, pitch_shift=8)
    elif style == "deep":
        return change_pitch_and_speed(input_file, output_file, pitch_shift=-6)
    elif style == "robotic":
        return change_pitch_and_speed(input_file, output_file, pitch_shift=0, time_stretch=1.2)
    elif style == "vibrato":
        return change_pitch_and_speed(input_file, output_file, pitch_shift=2)
    elif style == "slow":
        return change_pitch_and_speed(input_file, output_file, time_stretch=0.7)
    elif style == "fast":
        return change_pitch_and_speed(input_file, output_file, time_stretch=1.5)
    else:
        return change_pitch_and_speed(input_file, output_file)
