from dataprocessing.convert_all_midi_in_folder import convert_all_midi_files_in_folder, convert_all_midi_files_in_folder_mp
import os

# convert_all_midi_files_in_folder("E:\datasets\midi\\0", output_filename="E:\datasets\midi\converted", save_individually=True)
if __name__ == '__main__':
    convert_all_midi_files_in_folder_mp(f"E:\datasets\midi", output_filename="E:\datasets\midi\converted")

# if __name__ == '__main__':
#     # test multiprocessing speedup
#     import time
#
#     folder_path = "/Users/theodorforgaard/Downloads/lmd_matched/C/F/A"
#     output_path_mp = "./testmp"
#     output_path_serial = "./testserial"
#     os.makedirs(output_path_mp, exist_ok=True)
#     os.makedirs(output_path_serial, exist_ok=True)
#
#     t1_mp = time.time()
#     convert_mp(folder_path, output_path_mp)
#     t2_mp = time.time()
#
#     t1 = time.time()
#     convert_all_midi_files_in_folder(folder_path, output_path_serial, save_individually=True)
#     t2 = time.time()
#
#     print(f"mp time: {t2_mp - t1_mp}")
#     print(f"serial time: {t2 - t1}")