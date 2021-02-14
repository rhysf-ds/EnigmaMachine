alphab = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
i = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
ii = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'
iii = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
iv = 'ESOVPZJAYQUIRHXLNFTGKDCMWB'
v = 'VZBRGITYUPSDNHLXAWMJQOFECK'
vi = 'JPGVOUMFYQBENHZRDKASXLICTW'
vii = 'NZJHGRCXMYSWBOUFAIVLPEKQDT'
viii = 'FKQHTLXOCBJSPDZRAMEWNIUYGV'
reflectors = {'UKW-B':'YRUHQSLDPXNGOKMIEBFZCWVJAT', 'UKW-C':'FVPJIAOYEDRZXWGCTKUQSBNMHL' }

rotorconfigs = {'alphab': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'i': 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
                'ii': 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
                'iii': 'BDFHJLCPRTXVZNYEIWGAKMUSQO', 'iv': 'ESOVPZJAYQUIRHXLNFTGKDCMWB',
                'v': 'VZBRGITYUPSDNHLXAWMJQOFECK',
                'vi': 'JPGVOUMFYQBENHZRDKASXLICTW', 'vii': 'NZJHGRCXMYSWBOUFAIVLPEKQDT',
                'viii': 'FKQHTLXOCBJSPDZRAMEWNIUYGV'}

rotortickover = {'alphab': 25, 'i': 17,
                'ii': 5,
                'iii': 22, 'iv': 10,
                'v': 25,
                'vi': 13, 'vii': 13,
                'viii': 13}


class rotor:
    def __init__(self, rotortype, startingpos = 'A'):
        self.rotortype = rotortype
        self.startingpos = startingpos
        self.startingoffset = alphab.find(self.startingpos.upper())
        self.mapping = rotorconfigs[self.rotortype]
        self.tickover = rotortickover[self.rotortype[0]]
        self.inputside = alphab[self.startingoffset:] + alphab[:self.startingoffset]

    def __str__(self):
        return(f'this rotor is a type {self.rotortype}, with position set to {self.startingpos}')

    def encrypt(self, inputletter):
        return self.mapping[self.inputside.find(inputletter.upper())]

    def returnencrypt(self,inputletter):
        l = self.mapping.find(inputletter.upper())
        return self.inputside[l]


class reflector:
    def __init__(self, config = 'UKW-B'):
        self.config = config
        self.input = alphab
        self.mapping = reflectors[config]

    def __str__(self):
        return(f'This is a {self.config} type reflector')

    def output(self,inputletter):
        return self.mapping[self.input.find(inputletter.upper())]


def rotation(letter, rotationcount):
    if alphab.find(letter.upper()) + rotationcount >= 25:
        n = (alphab.find(letter.upper())+rotationcount) - 26
        return alphab[n]
    else:
        n = alphab.find(letter.upper()) + rotationcount
        return alphab[n]

def etw(lettern, count):
    return alphab[lettern - count]


def computation(x, counter, counter2, counter3):
    l1 = rotation(x, counter)
    r1 = rotor1.encrypt(l1)
    l2 = rotation(r1, counter2 - counter)
    r2 = rotor2.encrypt(l2)
    l3 = rotation(r2, counter3 - counter2)
    r3 = rotor3.encrypt(l3)
    rf = reflect.output(r3)
    l4 = rotation(rf, counter3)
    r32 = rotor3.returnencrypt(l4)
    l5 = rotation(r32, counter2 - counter3)
    r22 = rotor2.returnencrypt(l5)
    l6 = rotation(r22, counter - counter2)
    r12 = rotor1.returnencrypt(l6)
    l7 = rotation(r12, 0 - counter)
    return l7


phrase = 'dogsarethebestpet'
rotor1 = rotor('i')
rotor2 = rotor('ii')
rotor3 = rotor('iii')
reflect = reflector()


def enigma(phrase):
    counter = 0
    counter2 = 0
    counter3 = 0
    cryptphrase =''
    for x in phrase:
        if counter == 25:
            counter = 0
            if counter == rotor1.tickover:
                counter2 += 1
            else:
                pass
            if counter2 == rotor2.tickover:
                counter3 += 1
            else:
                pass
            if counter3 == 25:
                counter3 = 0
            else:
                pass
            l = computation(x, counter, counter2, counter3)
            cryptphrase += l
        else:
            counter += 1
            if counter == rotor1.tickover:
                counter2 += 1
            else:
                pass
            if counter2 == rotor2.tickover:
                counter3 += 1
            else:
                pass
            if counter3 == 25:
                counter3 = 0
            else:
                pass
            l = computation(x,counter, counter2, counter3)
            cryptphrase += l
    return(cryptphrase)


alphab.find('w'.upper())

''' l1, r1, l2, r2, l3, r3, rf, l4, r32, l5, r22, l6, r12, l7'''