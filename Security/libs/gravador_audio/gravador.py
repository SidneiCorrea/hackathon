import pyaudio
import wave
import subprocess
import os
import time
import threading


class Recorder():
    def __init__(self, chunk=1024, channels=2, rate=16000):
        self.CHUNK = chunk
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = channels
        self.RATE = rate
        self._running = True
        self._frames = []

    def start(self):
        threading._start_new_thread(self.__recording, ())

    def __recording(self):
        self._running = True
        self._frames = []
        p = pyaudio.PyAudio()
        stream = p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK)

        while(self._running):
            data = stream.read(self.CHUNK)
            self._frames.append(data)

        stream.stop_stream()
        stream.close()
        p.terminate()

    def stop(self):
        self._running = False

    def save(self, filename):
        print("Salvando")
        p = pyaudio.PyAudio()
        if not filename.endswith(".wav"):
            filename = filename + ".wav"
        wf = wave.open(filename, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self._frames))
        wf.close()
        print("Salvo")

    @staticmethod
    def delete(filename):
        os.remove(filename)

    @staticmethod
    def wavTomp3(wav):
        mp3 = wav[:-3] + "mp3"

        if os.path.isfile(mp3):
            Recorder.delete(mp3)

        subprocess.call('ffmpeg -i "'+wav+'" "'+mp3+'"')


if __name__ == "__main__":
    rec = Recorder()
    print("Começo da gravação")
    rec.start()
    time.sleep(5)
    print("Pausa da gravação")
    rec.stop()
    print("Salvando")
    rec.save("test.wav")
    Recorder.wavTomp3("test.wav")
    Recorder.delete("test.wav")