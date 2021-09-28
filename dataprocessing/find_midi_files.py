from typing import List
from pathlib import Path





def get_midi_files(folder_path: str) -> List[str]:
    """Gets a list of midi file paths in the given folder, recursively"""

    midi_file_search_path = Path(folder_path)
    midi_file_paths = [str(midi_file_path.absolute()) for midi_file_path in midi_file_search_path.rglob("*.mid")]

    return midi_file_paths


if __name__ == "__main__":

    midi_files = get_midi_files("./midi_filer")
    for midi_file in midi_files:
        print(midi_file)



