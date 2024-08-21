import os
import moviepy.editor as mp
from pydub import AudioSegment
from pydub.utils import make_chunks
import speech_recognition as sr

video_path = input("Introduce la ruta del video: ")
audio_path = "./audio_extracted.wav"
os.makesdirs('chunks', exist_ok=True)

print("Cargando el video y extrayendo el audio...")
video = mp.VideoFileClip(video_path)
video.audio.write_audiofile(audio_path)
print("Extracción de audio completa. Archivo guardado en:", audio_path)

def divide_audio(audio_file_path, duration=30):
    print("Cargando el archivo de audio completo...")
    sound = AudioSegment.from_wav(audio_file_path)
    print("Dividiendo el audio en segmentos de", duration, "segundos...")
    chunks = make_chunks(sound, duration * 1000) 
    print("División completa. Total de segmentos:", len(chunks))
    return chunks

r = sr.Recognizer()
print("Dividiendo el audio...")
audio_chunks = divide_audio(audio_path)

full_transcript = ""
for i, chunk in enumerate(audio_chunks):
    chunk_path = f"./chunks/chunk{i}.wav"
    chunk.export(chunk_path, format="wav")
    print(f"Procesando segmento {i+1}/{len(audio_chunks)}...")
    
    with sr.AudioFile(chunk_path) as source:
        audio = r.record(source)
    try:
        transcript = r.recognize_google(audio, language='es-ES')
        full_transcript += transcript + " "
        print(f"Segmento {i+1} transcrito correctamente.")
    except sr.RequestError as e:
        print(f"Error en la API en el segmento {i+1}: {e}")
    except sr.UnknownValueError:
        print(f"No se pudo entender el audio del segmento {i+1}")

print("Transcripción completa. Guardando en archivo...")
with open("transcript.txt", "w") as file:
    file.write(full_transcript)
print("Transcripción guardada en 'transcript.txt'.")

if os.name == 'nt':
    os.system('rmdir /s /q chunks')
    os.system('del audio_extracted.wav')
else:
    os.system('rm -rf chunks')
    os.system('rm audio_extracted.wav')