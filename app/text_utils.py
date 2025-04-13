def load_texts(file_paths):
    return [open(path, "r", encoding="utf-8").read() for path in file_paths]