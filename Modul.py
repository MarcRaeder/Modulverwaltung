from Studiengang import Studiengaenge, Studiengang


class Modul:
    def __init__(self, kuerzel, bezeichnung) -> None:
        self.kuerzel: str = kuerzel
        self.bezeichnung: str = bezeichnung
        self.studiengaenge: list = []
        self.istBachelorStudiengang: bool

    def fuegeHinzu(self, studiengang: Studiengang) -> None:
        if studiengang in self.studiengaenge:

            raise Exception("Der Studiengang existiert bereits")

        if len(self.studiengaenge) == 0:
            self.istBachelorStudiengang = Studiengaenge.istBachelorStudiengang(
                studiengang
            )
        if (
            Studiengaenge.istBachelorStudiengang(studiengang)
            != self.istBachelorStudiengang
        ):
            raise Exception(
                "Ein Modul kann nicht gleichzeitig zu Bachelor- und Masterstudiengang gehören."
            )

        self.studiengaenge.append(studiengang)
