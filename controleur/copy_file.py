import os
import shutil


class Clone:
    def __init__(self, folder_source, folder_destination):
        self.folder_source = folder_source
        self.folder_destination = folder_destination
        self.copy_file(self.folder_source, self.folder_destination)
        self.deleted_file(self.folder_source, self.folder_destination)
        print("Opération terminé les dossiers sont a jour")

    def copy_file(self, folder_source, folder_destination):
        list_files_in_folder_source = os.listdir(folder_source)
        list_files_in_folder_destination = os.listdir(folder_destination)

        for file in list_files_in_folder_source:
            if file not in list_files_in_folder_destination:
                # L'élément n'est pas dans la destination
                if os.path.isdir(folder_source + file):
                    # Créer un dossier dans la destination
                    os.mkdir(folder_destination + file, mode=700)
                    print(f"Creation du dossier {folder_destination, file}")
                    # On compare se qu'il se trouve dans le dossier en rappelant récursivement la fonction
                    self.copy_file(folder_source + file + "/", folder_destination + file + "/")
                else:
                    # C'est pas un dossier on peux le copier simplement
                    print(f"Copier {folder_destination, file}")
                    shutil.copy2(folder_source + file, folder_destination + file)
            else:
                # L'élément est dans la destination
                if os.path.isdir(folder_source + file):
                    # On compare se qu'il se trouve dans le dossier en rappelant récursivement la fonction
                    self.copy_file(folder_source + file + "/", folder_destination + file + "/")
                elif os.path.getsize(folder_source + file) != os.path.getsize(folder_destination + file):
                    # C'est un fichier et il est dans la destination
                    # il n'a pas la meme taille que dans le fichier de la destination
                    # On le recopie pour le remplacer
                    print(f"Copier {folder_destination, file}")
                    shutil.copy2(folder_source + file, folder_destination + file)

    def deleted_file(self, folder_source, folder_destination):
        list_files_in_folder_source = os.listdir(folder_source)
        list_files_in_folder_destination = os.listdir(folder_destination)

        for file in list_files_in_folder_destination:
            if file not in list_files_in_folder_source:
                # L'élément n'est pas dans la destination
                if os.path.isdir(folder_destination + file):
                    # si c'est un dossier, on le supprimer et se qu'il contient
                    print(f"Supprimer dossier {folder_destination, file}")
                    shutil.rmtree(folder_destination + file)
                else:
                    # C'est un fichier, je supprime
                    print(f"Supprimer {folder_destination, file}")
                    os.chmod(folder_destination + file, 0o0700)
                    os.remove(folder_destination + file)
            else:
                # L'élément est dans la destination
                if os.path.isdir(folder_destination + file):
                    # L'élément est un dossier, j'appelle recursivement la fontion
                    self.deleted_file(folder_source + file + "/", folder_destination + file + "/")
