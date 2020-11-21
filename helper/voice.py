#! /usr/bin/env python

import argparse
import os
import subprocess


def speech(wav_path):
    if not os.path.exists(wav_path):
        print(f"ERROR: {wav_path} does not exist.")
        return
    subprocess.run([
        'mplayer',
        '-ao',
        'alsa:device=bt-receiver',
        wav_path,
    ])


def main():
    parser = parser = argparse.ArgumentParser()
    wav_sample = 'voices/raspi_temperature_recover.wav'
    parser.add_argument('files', nargs='*', default=[wav_sample])
    args = parser.parse_args()
    print(args.files)
    for path in args.files:
        print(path)
        speech(path)


if __name__ == '__main__':
    main()
