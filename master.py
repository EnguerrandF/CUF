import os
import shutil
import time

class Clone:
    def __init__(self, dossier_source, dossier_destination):
        self.dossier_source = dossier_source
        self.dossier_destination = dossier_destination
        
    def main(self):
        if os.listdir(self.dossier_destination) == []:
            self.copierFichierDossier(self.dossier_source, self.dossier_destination)
        else:   
            self.comparerFichier(self.dossier_source, self.dossier_destination)
  
    def comparerFichier(self, dossier_source, dossier_destination):
        list_dossier_1 = os.listdir(dossier_source)
        list_dossier_2 = os.listdir(dossier_destination)

        for fichier1 in range(len(list_dossier_1)):
                for fichier2 in range(len(list_dossier_2)):
                    if list_dossier_1[fichier1] == list_dossier_2[fichier2]:
                        if os.path.isdir(dossier_source + list_dossier_1[fichier1]):
                            self.comparerFichier(dossier_source + list_dossier_1[fichier1] + "/", dossier_destination + list_dossier_2[fichier2] + "/")
                            break
                        else:
                            
                            if os.path.getsize(dossier_source + list_dossier_1[fichier1]) != os.path.getsize(dossier_destination + list_dossier_2[fichier2]):
                                print("le fichier ne fais pas la meme taille")
                                print(os.path.getsize(dossier_source + list_dossier_1[fichier1]), os.path.getsize(dossier_destination + list_dossier_2[fichier2]))
                                self.copierFichier(dossier_source, dossier_destination, list_dossier_1[fichier1])
                            break
                        
                    elif fichier2 == (len(list_dossier_2) - 1):
                        self.copierFichier(dossier_source, dossier_destination, list_dossier_1[fichier1])

    def copierFichierDossier(self, source, destination):
        list_dossier = os.listdir(source)
        for fichier in list_dossier:
            self.copierFichier(source + '/', destination + '/', fichier)

    def copierFichier(self, source, destination, fichier_copier):
        if os.path.isdir(source + fichier_copier):
            if os.path.exists(destination + fichier_copier):
                self.copierFichierDossier(source + fichier_copier, destination + fichier_copier)

            else:
                os.mkdir(destination + fichier_copier, mode=700)
                print(f"creer le le dossier: {destination, fichier_copier}")
                self.copierFichierDossier(source + fichier_copier, destination + fichier_copier)

        else:
            print(f"copier le fichier: {destination, fichier_copier}")
            shutil.copy(f'{source}{fichier_copier}', f'{destination}{fichier_copier}')
            
            
class Supp(Clone):
    def __init__(self, dossier_source, dossier_destination):
        super().__init__(dossier_source, dossier_destination)
    
    def main(self):
        self.comparerElement(self.dossier_source, self.dossier_destination)
        
    def comparerElement(self, dossier_source, dossier_destination):
        list_dossier_source = os.listdir(dossier_source)
        list_dossier_destination = os.listdir(dossier_destination)
        
        for fichier_destination in range(len(list_dossier_destination)):
            for fichier_source in range(len(list_dossier_source)):
                if list_dossier_destination[fichier_destination] == list_dossier_source[fichier_source]:
                    if os.path.isdir(dossier_destination + list_dossier_destination[fichier_destination]):
                        #print(f"c'est un dossier on le relance le scann dans: {list_dossier_destination[fichier_destination]}")
                        self.comparerElement(dossier_source + list_dossier_source[fichier_source] + "/" , dossier_destination + list_dossier_destination[fichier_destination] + "/" )
                        break
                    else:
                        #print("c'est un fichier")
                        break
                elif (len(list_dossier_source) - 1) == fichier_source:
                    #print("supprimer", list_dossier_destination[fichier_destination])
                    if os.path.isdir(dossier_destination + list_dossier_destination[fichier_destination]):
                        print(f"supprimer le dossier dans {dossier_destination , list_dossier_destination[fichier_destination]}")
                        shutil.rmtree(dossier_destination + list_dossier_destination[fichier_destination])
                    else:
                        print(f"supprimer le fichier dans {dossier_destination , list_dossier_destination[fichier_destination]}")
                        os.remove(dossier_destination + list_dossier_destination[fichier_destination])
                        
            
#lancer le programm
def run(dossier1, dossier2):
    Clone(dossier1, dossier2).main()
    Supp(dossier1, dossier2).main()