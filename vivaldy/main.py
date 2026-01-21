import time
import vivaldy

def main():

    # audio = pydub.AudioSegment.from_wav('audio.wav')
    # play(audio)

    # async def play(audio, sample_rate=44100):
    #     await loop.run_in_executor(None, sounddevice.play, audio, sample_rate)

    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(play(audio, sample_rate=sample_rate))

    ## Toy example for vivaldy

    # Let's start waiting!
    music = MusicOnHold()
    music.start()

    for i in range(10):
        print(f"Processing {i+1:d}/10...")
        time.sleep(5)

    # And now we are done
    music.done()


if __name__ == '__main__':
    main()
