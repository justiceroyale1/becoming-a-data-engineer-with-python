class Artist:
    def __init__(self, gender, locality):
        self.gender = gender
        self.locality = locality

def list_artists(artist):
    match artist:
        case Artist(gender='male', locality='domestic'):
            print(['Davido', 'Rema', 'Asake'])
        case Artist(gender='female', locality='domestic'):
            print(['Tiwa Savage', 'Teni', 'Tems'])
        case Artist(gender='male', locality='foreign'):
            print(['Ed Sheeran', 'Jay Z', 'Eminem'])
        case Artist(gender='female', locality='foreign'):
            print(['Beyonce', 'Lady Gaga', 'Taylor Swift'])

list_artists(Artist('male', 'domestic'))
list_artists(Artist('female', 'domestic'))
list_artists(Artist('male', 'foreign'))
list_artists(Artist('female', 'foreign'))