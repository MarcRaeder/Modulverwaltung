from Modul import Modul
import operator


class Modulverwaltung:
    def __init__(self) -> None:
        self.module: list = []

    def fuegeHinzu(self, modul: Modul) -> None:
        if modul in self.module:
            raise Exception("Das Modul ist bereits vorhanden")

        self.module.append(modul)

    def gibModule(self, fuerBachelor: bool):
        modulListe = []
        if fuerBachelor == True:
            for modul in self.module:
                if modul.istBachelorStudiengang == fuerBachelor:
                    modulListe.append(modul)
        elif fuerBachelor != True:
            for modul in self.module:
                if modul.istBachelorStudiengang != True:
                    modulListe.append(modul)

        modulListe = sorted(modulListe, key=operator.attrgetter("kuerzel"))

        return modulListe
