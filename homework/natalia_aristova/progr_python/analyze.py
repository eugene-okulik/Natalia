import argparse
import os

def extract_context(line, keyword):
    words = line.strip().split()
    context = []
    for i, word in enumerate(words):
        if keyword in word:
            start = max(i - 5, 0)
            end = i + 6
            context = words[start:end]
            break
    return " ".join(context)

def search_logs(folder_path, keyword, show_all):
    if not os.path.isdir(folder_path):
        print("Указанный путь не является директорией.")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    for line_number, line in enumerate(f, start=1):
                        if keyword in line:
                            context = extract_context(line, keyword)
                            print(f"[{filename}] Строка {line_number}: {context}")
                            if not show_all:
                                return
            except Exception as e:
                print(f"Ошибка при чтении файла {filename}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="File name")
    parser.add_argument("-d", "--date", help="date for search")
    parser.add_argument("--full", help="date for search", action="store_true")
    args = parser.parse_args()

    search_logs(args.file, args.text, args.full)
