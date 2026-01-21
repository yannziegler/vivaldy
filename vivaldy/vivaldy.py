#!/usr/bin/env python

import os

import ffmpeg
import pydub
import pytubefix
from playsound3 import playsound

# import asyncio
# from pydub.playback import play
# import sounddevice

YT_DEFAULT_URL = 'https://www.youtube.com/watch?v=l-dYNttdgl0'

HOLD_MESSAGE = "Please wait, your processing is going to start..."

class MusicOnHold():

    def __init__(self,
                 src=YT_DEFAULT_URL,
                 dest='vivaldy.wav',
                 hold_message=HOLD_MESSAGE,
                 start=False):
        self.audio_source = src
        self.audio_filepath = dest
        self.audio_format = 'wav'
        # self.ready = False

        self.hold_message = hold_message
        if self.hold_message:
            print(self.hold_message)

        if 'watch?v=' in self.audio_source:
            self.youtube = pytubefix.YouTube(self.audio_source)
            try:
                self.download_audio()
            except URLError:
                # raise ValueError("Please provide a valid URL for music source")
                # Temporary fallback solution
                self.audio_source = 'vivaldy.wav'
                self.audio_filepath = self.audio_source
        else:
            if not os.path.isfile(self.audio_source):
                raise ValueError("Please provide a valid filepath for music source")

        # Note: self-control is important while waiting
        self.control = None

    def download_audio(self):
        # Get the URL of the video stream
        stream_url = self.youtube.streams[0].url

        # Probe the audio streams
        probe = ffmpeg.probe(stream_url)
        audio_streams = next((stream for stream in probe['streams'] \
                              if stream['codec_type'] == 'audio'), None)
        self.sample_rate = int(audio_streams['sample_rate'])

        # Read audio into memory buffer.
        # Get the audio using stdout pipe of ffmpeg sub-process.
        # The audio is transcoded to PCM codec in WAC container.
        # Select WAV output format, and pcm_s16le auidio codec. My add ar=sample_rate
        self.audio_buffer, err = ffmpeg.input(stream_url) \
                                       .output("pipe:",
                                               format=self.audio_format,
                                               acodec='pcm_s16le',
                                               ar=self.sample_rate,
                                               loglevel='quiet') \
                                       .run(capture_stdout=True)

        self.write_audio()

    def write_audio(self):
        # Write the audio buffer to file
        with open(self.audio_filepath, 'wb') as f:
            f.write(self.audio_buffer)

    def start(self):
        self.control = playsound(self.audio_filepath, block=False)

    def stop(self):
        if self.control is not None:
            self.control.stop()

    def done(self):
        self.stop()

    def wait(self):
        if self.control.is_alive():
            self.control.wait()
