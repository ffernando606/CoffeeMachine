n1 = input()
n2 = input()
search = ''
strange = ['Strange', 'Quark', '1/2', '-1/3']
charm = ['Charm', 'Quark', '1/2', '2/3']
electron = ['Electron','Lepton', '1/2', '-1']
neutrino = ['Neutrino', 'Lepton', '1/2', '0']
photon = ['Photon', 'Boson', '1', '0']
particle = [strange, charm, electron, neutrino,photon]
for i in range(5):
    if n1 in particle[i] and n2 in particle[i]:
        search = particle[i]
        print(f"{search[0]} {search[1]}")
