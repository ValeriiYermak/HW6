import sys
from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []
DOC_DOCUMENTS = []
DOCX_DOCUMENTS = []
TXT_DOCUMENTS = []
PDF_DOCUMENTS = []
XLSX_DOCUMENTS = []
PPTX_DOCUMENTS = []
MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []
MY_OTHER = []
ARCHIVES = []

REGISTER_EXTENSION = {
    'JPEG': JPEG_IMAGES,
    'JPG': JPG_IMAGES,
    'PNG': PNG_IMAGES,
    'SVG': SVG_IMAGES,
    'AVI': AVI_VIDEO,
    'MP4': MP4_VIDEO,
    'MOV': MOV_VIDEO,
    'MKV': MKV_VIDEO,
    'DOC': DOC_DOCUMENTS,
    'DOCX': DOCX_DOCUMENTS,
    'TXT': TXT_DOCUMENTS,
    'PDF': PDF_DOCUMENTS,
    'XLSX': XLSX_DOCUMENTS,
    'PPTX': PPTX_DOCUMENTS,
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,
    'ZIP': ARCHIVES,
    'GZ': ARCHIVES,
    'TAR': ARCHIVES,
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()


def get_extension(name: str) -> str:
    return Path(name).suffix[1:].upper()  # suffix[1:] -> .jpg -> jpg


def scan(folder: Path):
    for item in folder.iterdir():
        # Робота з папкою
        if item.is_dir():  # перевіряємо чи обєкт папка
            if item.name not in ('archives', 'video', 'audio', 'documents',
                                 'images', 'MY_OTHER'):
                FOLDERS.append(item)
                scan(item)
            continue

        # Робота з файлом
        extension = get_extension(item.name)  # беремо розширення файлу
        full_name = folder / item.name  # беремо повний шлях до файлу
        if not extension:
            MY_OTHER.append(full_name)
        else:
            try:
                REGISTER_EXTENSION[extension]
                EXTENSIONS.add(extension)
            except KeyError:
                UNKNOWN.add(extension)  # .mp4, .mov, .avi
                MY_OTHER.append(full_name)


if __name__ == '__main__':
    folder_process = sys.argv[1]
    scan(Path(folder_process))

    print(f'Images jpeg: {JPEG_IMAGES}')
    print(f'Images jpg: {JPG_IMAGES}')
    print(f'Images png: {PNG_IMAGES}')
    print(f'Images svg: {SVG_IMAGES}')

    print(f'VIDEO avi: {AVI_VIDEO}')
    print(f'VIDEO mp4: {MP4_VIDEO}')
    print(f'VIDEO mov: {MOV_VIDEO}')
    print(f'VIDEO mkv: {MKV_VIDEO}')

    print(f'DOCUMENTS doc: {DOC_DOCUMENTS}')
    print(f'DOCUMENTS docx: {DOCX_DOCUMENTS}')
    print(f'DOCUMENTS txt: {TXT_DOCUMENTS}')
    print(f'DOCUMENTS pdf: {PDF_DOCUMENTS}')
    print(f'DOCUMENTS xlsx: {XLSX_DOCUMENTS}')
    print(f'DOCUMENTS pptx: {PPTX_DOCUMENTS}')

    print(f'AUDIO ogg: {OGG_AUDIO}')
    print(f'AUDIO mp3: {MP3_AUDIO}')
    print(f'AUDIO wav: {WAV_AUDIO}')
    print(f'AUDIO amr: {AMR_AUDIO}')

    print(f'Archives gz: {ARCHIVES}')
    print(f'Archives zip: {ARCHIVES}')
    print(f'Archives tar: {ARCHIVES}')
    print(f'EXTENSIONS: {EXTENSIONS}')

    print(f'UNKNOWN: {UNKNOWN}')
