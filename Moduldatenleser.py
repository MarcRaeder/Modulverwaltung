from Modul import Modul
from Modulverwaltung import Modulverwaltung
from Studiengang import Studiengaenge


class Moduldatenleser:
    def lies(modulverwaltung: Modulverwaltung) -> None:
        modulFile = open("Module.txt", "r")
        modulData = modulFile.read().split(";")
        newModul = Modul(modulData[0], modulData[1])
        modulData = modulData[2].replace("\n", "").split(",")
        for modul in modulData:
            newModul.fuegeHinzu(Studiengaenge[modul])

        modulverwaltung.fuegeHinzu(newModul)
