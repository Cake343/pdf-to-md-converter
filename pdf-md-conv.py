import glob
import os
import pymupdf4llm 

def batch_convert_pdf_to_md(input_folder=".", output_folder="."):
    # Tworzymy folder wyjściowy, jeśli nie istnieje
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    # Szukamy wszystkich plików PDF w podanym katalogu
    pdf_files = glob.glob(os.path.join(input_folder, "*.pdf"))
    
    if not pdf_files:
        print("Nie znaleziono żadnych plików PDF w podanym folderze.")
        return

    for pdf_path in pdf_files:
        base_name = os.path.basename(pdf_path)
        md_filename = base_name.replace(".pdf", ".md")
        md_path = os.path.join(output_folder, md_filename)
        
        print(f"Konwertowanie: {base_name}...")
        try:
            # Ekstrakcja z optymalizacją pod modele językowe
            md_text = pymupdf4llm.to_markdown(pdf_path)
            
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(md_text)
                
            print(f"Sukces: Zapisano jako {md_filename}")
        except Exception as e:
            print(f"Błąd podczas konwersji {base_name}: {e}")

if __name__ == "__main__":
    # Ścieżki możesz dostosować do swoich potrzeb
    katalog_z_pdf = "." 
    katalog_docelowy = "./skonwertowane_pliki"
    
    batch_convert_pdf_to_md(input_folder=katalog_z_pdf, output_folder=katalog_docelowy)