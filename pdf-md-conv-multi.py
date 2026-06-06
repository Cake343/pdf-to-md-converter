import glob
import os
import pymupdf4llm
from concurrent.futures import ProcessPoolExecutor, as_completed

def convert_single_pdf(pdf_path, output_folder):
    """Funkcja konwertująca pojedynczy plik (uruchamiana w osobnym procesie)."""
    base_name = os.path.basename(pdf_path)
    md_filename = base_name.replace(".pdf", ".md")
    md_path = os.path.join(output_folder, md_filename)
    
    try:
        md_text = pymupdf4llm.to_markdown(pdf_path)
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md_text)
        return f"[✓] Sukces: {base_name} -> {md_filename}"
    except Exception as e:
        return f"[✗] Błąd przy pliku {base_name}: {e}"

def batch_convert(input_folder, output_folder, workers):
    """Funkcja zarządzająca pulą procesów."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    pdf_files = glob.glob(os.path.join(input_folder, "*.pdf"))
    if not pdf_files:
        print("\nNie znaleziono żadnych plików PDF w wybranym folderze.")
        return

    print(f"\nRozpoczynam konwersję {len(pdf_files)} plików...")
    print(f"Używana liczba procesów (rdzeni): {workers}\n")
    
    # ProcessPoolExecutor tworzy osobne procesy, idealne do zadań CPU-bound
    with ProcessPoolExecutor(max_workers=workers) as executor:
        # Zlecamy zadania dla każdego pliku PDF
        futures = {executor.submit(convert_single_pdf, pdf, output_folder): pdf for pdf in pdf_files}
        
        # as_completed pozwala wyświetlać wyniki natychmiast, gdy dany plik skończy się przetwarzać
        for future in as_completed(futures):
            print(future.result())
            
    print("\nKonwersja zakończona pomyślnie!")

def main():
    # Domyślne wartości
    input_folder = "."
    output_folder = "./skonwertowane_pliki"
    workers = 6  # Domyślnie ustawione na 6 procesów (idealne dla 6-rdzeniowych CPU)

    while True:
        print("\n" + "="*50)
        print("   KONWERTER PDF -> MARKDOWN (Wersja Wielordzeniowa)   ")
        print("="*50)
        print(f"1. Rozpocznij konwersję")
        print(f"2. Zmień folder wejściowy   (Obecnie: '{input_folder}')")
        print(f"3. Zmień folder wyjściowy   (Obecnie: '{output_folder}')")
        print(f"4. Zmień liczbę procesów    (Obecnie: {workers})")
        print("5. Wyjście")
        
        wybor = input("\nWybierz opcję (1-5): ").strip()
        
        if wybor == '1':
            batch_convert(input_folder, output_folder, workers)
        elif wybor == '2':
            nowy_input = input("Podaj nową ścieżkę do folderu z PDF: ").strip()
            if os.path.exists(nowy_input):
                input_folder = nowy_input
            else:
                print("⚠️ Taki folder nie istnieje!")
        elif wybor == '3':
            output_folder = input("Podaj nową ścieżkę do folderu wyjściowego: ").strip()
        elif wybor == '4':
            try:
                nowe_workers = int(input("Podaj liczbę procesów (np. 2, 4, 6): "))
                if nowe_workers > 0:
                    workers = nowe_workers
                else:
                    print("⚠️ Liczba procesów musi być większa od zera!")
            except ValueError:
                print("⚠️ To musi być liczba całkowita!")
        elif wybor == '5':
            print("Zamykanie programu...")
            break
        else:
            print("⚠️ Nieznana opcja. Spróbuj ponownie.")

# Instrukcja warunkowa niezbędna do poprawnego działania wieloprocesowości (zwłaszcza w Windows)
if __name__ == "__main__":
    main()