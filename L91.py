lines = ["Haiku frogs in snow",
        "A limerick came from Nantucket",
        "Tetrametric drum-beats thrumming, Hiawathianic rhythm."]
def breakify(list):
    return "<br>".join(list)

print(breakify(lines))
