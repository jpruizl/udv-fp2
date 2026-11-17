from ave import Ave
from gallina import Gallina
from paloma import Paloma


if __name__ == "__main__":
    print("Ave: ", end="")
    ave = Ave()
    ave.volar()

    for nombre, ave in (
        ("Gallina", Gallina()),
        ("Paloma", Paloma()),
    ):
        print(f"{nombre}: ", end="")
        ave.volar()