import os
import shutil
from pathlib import Path


FILE_TYPES={
     "PDF": [".pdf"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Docs": [".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"]
}


def organize_files(folder):
    folder_path=Path(folder)

    if not folder_path.exists() or not folder_path.is_dir():
        print(f"Erreur:le dossier '{folder}' n'exsite pas ou n'est pas un dossier valide ")
        return
    
    for file in folder_path.iterdir():
        if file.is_file():
            file_extension=file.suffix.lower()
            for category,extensions in FILE_TYPES.items():
                if file_extension in extensions:
                    target_folder=folder_path/category
                    target_folder.mkdir(exist_ok=True)
                    shutil.move(str(file),str(target_folder/file.name))
                    print(f"Moved:{file.name}->{category}")
                    break
                

if __name__=="__main__":
    folder_input=input("Entrez le chemin du dossier a Organiser : ")
    organize_files(folder_input)
    print("File organization completed")