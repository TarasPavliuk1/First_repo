from pathlib import Path
import shutil
import sys
import file_parser
from normalize import normalize

def handle_media(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    file_name.replace(target_folder / normalize(file_name.name))


# def handle_documents(file_name: Path, target_folder: Path):
#     target_folder.mkdir(exist_ok=True, parents=True)
#     file_name.replace(target_folder / normalize(file_name.name))

# def handle_audio(file_name: Path, target_folder: Path):
#     target_folder.mkdir(exist_ok=True, parents=True)
#     file_name.replace(target_folder / normalize(file_name.name))

# def handle_video(file_name: Path, target_folder: Path):
#     target_folder.mkdir(exist_ok=True, parents=True)
#     file_name.replace(target_folder / normalize(file_name.name))



def handle_archive(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / normalize(file_name.name.replace(file_name.suffix, ''))
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(file_name.absolute()), str(folder_for_file.absolute()))
    except shutil.ReadError:
        folder_for_file.rmdir()
        return
    file_name.unlink()

# бот дописав
# if __name__ == '__main__':
#     folder_process = sys.argv[1]
#     file_parser.scan(Path(folder_process))

#     # Обробка файлів згідно з file_parser
#     for img in file_parser.JPEG_IMAGES:
#         handle_media(img, Path('images'))

#     for mp3 in file_parser.MP3_AUDIO:
#         handle_media(mp3, Path('audio'))

#     for zip_file in file_parser.ARCHIVES:
#         handle_archive(zip_file, Path('archives'))