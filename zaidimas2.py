import random

class Zaidimas:
    def __init__(self):
        self.pasirinkimai = {"akmuo": 0, "zirkles": 1, "popierius": 2}
        self.rezultatas = {
            "Laimeta": 0,
            "Pralaimeta": 0,
            "Lygiosios": 0,
        }

    def random_pasirinkimas(self):
        return random.choice(list(self.pasirinkimai.keys()))

    def patikrinti_zaidima(self, zaidejas, kompiuteris):
        baigtis = ["Lygiosios", "Pralaimeta", "Laimeta"][(zaidejas - kompiuteris) % 3]

        self.rezultatas[baigtis] += 1

        baigties_zinute = {
            "Lygiosios": "Lygiosios!",
            "Laimeta": "Laimejote!",
            "Pralaimeta": "Pralaimejote!",
        }
        print(baigties_zinute[baigtis])

    def atspausdinti_rezultata(self):
        laimejimai = self.rezultatas["Laimeta"]
        pralaimejimai = self.rezultatas["Pralaimeta"]
        lygiosios = self.rezultatas["Lygiosios"]

        print(f"\nJus turite {laimejimai} laimejimu\n{pralaimejimai} pralaimejimu\n{lygiosios} lygiuju")

    def paleisti_zaidima(self):
        while True:
            vartotojo_pasirinkimas = input("Iveskite savo norima pasirinkima : Akmuo, Zirkles, Popierius\n").lower()
            if vartotojo_pasirinkimas in self.pasirinkimai.keys():
                break
            else:
                print("Netinkamas pasirinkimas!")
        kompiuteris = self.random_pasirinkimas()
        print(f" Jus pasirinkote : {vartotojo_pasirinkimas},\n Kompiuteris pasirinko : {kompiuteris}.")
        self.patikrinti_zaidima(self.pasirinkimai[vartotojo_pasirinkimas], self.pasirinkimai[kompiuteris])


if __name__ == "__main__":
    zaidimas = Zaidimas()
    while True:
        zaidimas.paleisti_zaidima()
        zaidimas.atspausdinti_rezultata()

        while True:
            testi = input("\nAre norite testi zaidima? (taip/ne):  ").lower()
            if testi == "ne":
                print("Viso gero!")
                exit()
            elif testi == "taip":
                break
            else:
                print("Neteisingas pasirinkimas!\n")
                continue
