output_div = Element("output-pane")
error_div = Element("errors-pane")

antall = 15
tur = "A"
start = {}


def clear(*args, **kwargs):
    output_div.element.innerText = ""
    error_div.element.innerText = ""


def info(antall):
    print(f"Antall: {antall}")


def spill(spiller):
    global antall, tur
    if antall <= 0:
        return
    navn = spiller.__name__.capitalize()
    valg = max(min(spiller(antall), min(antall, 3)), 1)
    print(f"{tur}: {navn} tar {valg}")
    antall -= valg
    tur = "A" if tur == "B" else "B"
    info(antall)
    if antall <= 0:
        print(f"{navn} tapte")
