class Atom(object):
    """
    原子の基底クラス。

    Parameters
    ----------
    valence : int
        原子の原子価
    """
    @property
    def valence(self) -> int:
        return self.valence


class Hydrogen(Atom):
    """
    水素
    """
    valence: int = 1


class Fluorine(Atom):
    """
    フッ素
    """
    valence: int = 1


class Chlorine(Atom):
    """
    塩素
    """
    valence: int = 1


class Bromine(Atom):
    """
    臭素
    """
    valence: int = 1


class Iodine(Atom):
    """
    ヨウ素
    """
    valence: int = 1


class Oxygen(Atom):
    """
    酸素
    """
    valence: int = 2


class Sulfur(Atom):
    """
    硫黄
    """
    valence: int = 2


class Nitrogen(Atom):
    """
    窒素
    """
    valence: int = 3


class Carbon(Atom):
    """
    炭素
    """
    valence: int = 4
