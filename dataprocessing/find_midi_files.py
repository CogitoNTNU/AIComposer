from pathlib import Path

def get_midi_files(path: str):
    midi_file_search_path = Path(path)
    midi_file_paths = (midi_file_search_path.rglob("*.mid"))

    return midi_file_paths

if __name__ == "__main__":

    midi_files = get_midi_files("./midi_filer")
    for midi_file in midi_files:
        print(str(midi_file))