# PDF → Markdown

Prosty konwerter plików PDF do Markdown z użyciem [`pymupdf4llm`](https://pymupdf.readthedocs.io/en/latest/pymupdf4llm/).  
Powstałe pliki Markdown nadają się m.in. do przygotowania dokumentów jako bazy wiedzy dla **LLM, AI i agentów**.

W repo są dwie wersje programu:

- `pdf_to_md.py` — zwykła, prosta konwersja plików
- `pdf_to_md_parallel.py` — wersja wieloprocesowa, przydatna przy większej liczbie PDF-ów

## Instalacja

Wymagany jest Python 3.9+.

```bash
pip install pymupdf4llm
```

## Użycie

Wrzuć pliki `.pdf` do wybranego folderu.

### Wersja prosta

Uruchom:

```bash
python pdf_to_md.py
```

Program:

1. szuka plików `.pdf` w bieżącym katalogu,
2. konwertuje każdy z nich do Markdown,
3. zapisuje wynik w:

```text
./skonwertowane_pliki/
```

Przykład:

```text
.
├── pdf_to_md.py
├── dokument1.pdf
├── dokument2.pdf
└── skonwertowane_pliki/
    ├── dokument1.md
    └── dokument2.md
```

Ścieżki wejściową i wyjściową można zmienić bezpośrednio w kodzie na końcu pliku:

```python
katalog_z_pdf = "."
katalog_docelowy = "./skonwertowane_pliki"
```

### Wersja wieloprocesowa

Uruchom:

```bash
python pdf_to_md_parallel.py
```

Program posiada proste menu, w którym można:

```text
1. Rozpocząć konwersję
2. Zmienić folder wejściowy
3. Zmienić folder wyjściowy
4. Zmienić liczbę procesów
5. Wyjść
```

Domyślnie używa **6 procesów**.

Przy większej liczbie dokumentów można zwiększyć tę wartość, np. do liczby rdzeni CPU:

```text
Podaj liczbę procesów (np. 2, 4, 6): 12
```

Nie ma jednak sensu ustawianie absurdalnie dużej liczby procesów — więcej nie zawsze oznacza szybciej.

## Po co Markdown?

PDF jest wygodny dla człowieka, ale niekoniecznie jest najlepszym formatem wejściowym dla systemów AI.

Konwersja do Markdown pozwala zachować m.in.:

- strukturę nagłówków,
- akapity,
- listy,
- tabele,
- podstawowe formatowanie,
- kolejność treści.

Dzięki temu wynik można później wykorzystać jako materiał do:

- RAG,
- bazy wiedzy,
- agentów AI,
- lokalnych LLM,
- wyszukiwania semantycznego,
- embeddingów,
- dokumentacji dla modeli.

Przykładowy workflow:

```text
PDF
 ↓
pymupdf4llm
 ↓
Markdown
 ↓
czyszczenie / podział na fragmenty
 ↓
embeddingi
 ↓
vector database
 ↓
RAG / agent AI
```

## Ważne

To nie jest OCR ani magiczne „naprawianie” każdego PDF-a. Jakość wyniku zależy od jakości dokumentu źródłowego. Szczególnie problematyczne mogą być skany, nietypowe układy stron czy bardzo skomplikowane dokumenty.

Projekt jest prostym narzędziem pomocniczym — bez GUI, bazy danych i zbędnej infrastruktury.
