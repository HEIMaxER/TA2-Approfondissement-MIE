from django.db import models

class Animal(models.Model):

    animal_id = models.CharField(max_length=255)
    race = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    etat = models.CharField(max_length=255)
    lieu = models.CharField(max_length=255)

    def __str__(self):
        return self.animal_id

class Equipement(models.Model):
    lieu =  models.CharField(max_length=255)
    disponibilite =  models.CharField(max_length=255)


def lit_etat(animal_id) :

    with open('animal.json', "r") as f:
        animal = json.load(f)

    try :
        poca = animal[animal_id]
        return( poca['ETAT'])

    except :
        print("Désolé, %s n'est pas un animal connu" % animal_id)
        return None

def lit_lieu(animal_id) :

    with open('animal.json', "r") as f:
        animal = json.load(f)

    try :
        poca = animal[animal_id]
        return( poca['LIEU'])

    except :
        print("Désolé, %s n'est pas un animal connu" % animal_id)
        return None

def verifie_disponibilite(equipement_id):

    with open('équipement.json', "r") as f:
        equipement = json.load(f)

    try :
        poca = equipement[equipement_id]
        return( poca['DISPONIBILITÉ'])

    except :
        print("Désolé, %s n'est pas un equipement connu" % equipement_id)
        return None


def cherche_occupant(lieu):

    with open('animal.json', "r") as f:
        animal = json.load(f)

    occupants = []
    for k in animal :

        if animal[k]['LIEU'] == lieu :
            occupants.append(k)

    if len(occupants) != 0:
        return occupants

    else :
        print("Désolé, %s n'est pas un lieu connu" % lieu)
        return None

def change_etat(animal_id, etat):
    etats_autho = {'affamé', 'fatigué', 'repus', 'endormi'}

    with open('animal.json', "r") as f:
        animal = json.load(f)

    try :
        poca = animal[animal_id]
        if etat in etats_autho :
            poca['ETAT'] = etat
        with open('animal.json', "w") as g:
            json.dump(animal, g)

    except :
        print("Désolé, %s n'est pas un animal connu"% animal_id)
        return None

def change_lieu(animal_id, lieu):

    lieu_autho = {"littière","mangeoire", "roue", "nid"}

    if lieu in lieu_autho :

        if verifie_disponibilite(lieu) == 'libre':

            with open('animal.json', "r") as f:
                animal = json.load(f)

            try :
                poca = animal[animal_id]

                l2 = poca['LIEU']
                with open('équipement.json', "r") as f:
                    equipement = json.load(f)

                poca2 = equipement[l2]
                poca2['DISPONIBILITÉ'] = 'libre'


                if poca['LIEU'] != 'littière':
                    poca3 = equipement[lieu]
                    poca3['DISPONIBILITÉ'] = 'occupé'

                with open('équipement.json', "w") as g:
                    json.dump(equipement, g)

                poca['LIEU'] = lieu
                with open('animal.json', "w") as g:
                    json.dump(animal, g)

            except :
                print("Désolé, %s n'est pas un animal connu" % animal_id)
                return None
        else :
            print('%s est occupé' % lieu)
            return None

    else :
        print("Désolé, %s n'est pas un lieu connu" % lieu)
        return None
