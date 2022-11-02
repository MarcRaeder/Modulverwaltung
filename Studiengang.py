from enum import Enum


class Studiengang:
    def __init__(self, isBachelor: bool) -> None:
        self.isBachelor: bool = isBachelor


class Studiengaenge(Enum):
    IN_BA = Studiengang(True)
    MI_BA = Studiengang(True)
    WI_BA = Studiengang(True)
    IN_MA = Studiengang(False)
    MI_MA = Studiengang(False)
    WI_MA = Studiengang(False)

    def istBachelorStudiengang(studiengang: Studiengang) -> bool:
        return studiengang.value.isBachelor
