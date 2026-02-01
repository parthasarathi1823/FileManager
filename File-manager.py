from pathlib import Path
import logging

logging.basicConfig(filename="main.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def organize_files(source_folder:str):

    source_path=Path(source_folder)

    if not source_path.is_dir() and not source_path.exists():
        print("Source folder does not exist")
        logging.error(f"Invalid source folder: {source_folder}")
        return

    file_types={
        "Image":[".jpg",".png",".jpeg",".gif"],
        "Document":[".txt",".pdf",".doc",".docx"],
        "Text":[".txt"],
        "Json":[".json"],
        "csv":[".csv"],
    }

    for file in source_path.rglob("*"):
        if file.is_file() and file.exists():

            ext=file.suffix

            for folder,extensions in file_types.items():
                if ext in extensions:

                    folder=Path(source_folder)/folder
                    folder.mkdir(exist_ok=True)

                    dest=folder/file.name
                    file.rename(dest)

                    print(f"Moved {file.name} to {folder} folder")
                    logging.info(f"Moved {file.name} to {folder} folder")

                    break

            else :

                other_folder=Path(source_folder)/"Others"
                other_folder.mkdir(exist_ok=True)

                file.rename(other_folder/file.name)

                logging.info(f"Moved {file.name} to 'Others' folder")
                print(f"Moved {file.name} to 'Others' folder")


try :
    dir=input("Enter Your Folder Path: ")
except ValueError as e:
    print("Invalid Directory Path : {}".format(e))
    logging.error(f"Invalid Directory Path: {e}")
else :
    organize_files(dir)


