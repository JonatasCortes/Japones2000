import os

# Caminho da pasta kana_sounds (no mesmo diretório do script)
folder_path = os.path.join(os.path.dirname(__file__), "kana_sounds")

# Percorre todos os arquivos da pasta
for filename in os.listdir(folder_path):
    if filename.lower().endswith(".mp3"):
        file_path = os.path.join(folder_path, filename)
        try:
            os.remove(file_path)
            print(f"Deletado: {filename}")
        except Exception as e:
            print(f"Erro ao deletar {filename}: {e}")
