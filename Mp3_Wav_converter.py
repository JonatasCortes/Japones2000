import os
import subprocess

# Caminho relativo para a pasta de áudio
sounds_path = os.path.join(os.path.dirname(__file__), "kana_sounds")

# Verifica todos os arquivos na pasta
for filename in os.listdir(sounds_path):
    if filename.lower().endswith(".mp3"):
        mp3_file = os.path.join(sounds_path, filename)
        wav_file = os.path.join(sounds_path, os.path.splitext(filename)[0] + ".wav")

        # Converte usando ffmpeg
        subprocess.run([
            "venv\\Lib\\site-packages\\ffmpeg-7.1.1-essentials_build\\bin\\ffmpeg.exe",
            "-y",  # sobrescreve arquivos existentes
            "-i", mp3_file,
            wav_file
        ], check=True)

        print(f"Convertido: {filename} → {os.path.basename(wav_file)}")
