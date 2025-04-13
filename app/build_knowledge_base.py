import os
from text_utils import load_texts

def build_knowledge_base(directory_path="./texts"):
    file_paths = [
        os.path.join(directory_path, f)
        for f in os.listdir(directory_path)
        if f.endswith(".txt")
    ]
    texts = load_texts(file_paths)
    return texts