import subprocess
import os

def docx_to_pdf(input_file):
    libreoffice_path = "C:\\Program Files\\LibreOffice\\program\\soffice.exe"
    
    if not os.path.exists(libreoffice_path):
        print("LibreOffice non è installato. Installa LibreOffice e riprova.")
        return
        
    try:
        subprocess.run([libreoffice_path, '--headless', '--convert-to', 'pdf', input_file], check=True)
        print(f"Conversione completata con successo: {input_file.replace('.docx', '.pdf')}")
    except subprocess.CalledProcessError as e:
        print(f"Errore durante la conversione: {e}")

input_file = input("Inserisci il nome del file .docx (inclusa l'estensione): ")
docx_to_pdf(input_file)
