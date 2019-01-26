from django.db import models

class Animal(models.Model):

    animal_id = models.CharField(max_length=255)
    race = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    etat = models.CharField(max_length=255)
    lieu = models.CharField(max_length=255)



class Equipement(models.Model):
    lieu =  models.CharField(max_length=255)
    disponibilite =  models.CharField(max_length=255)

    def __str__(self):
        return self.lieu

def lit_etat(id) :

    animal = Animal.objects.get(pk=id)
    try :
        return(animal.etat)

    except :
        print("Désolé, %s n'est pas un animal connu" % id)
        return None

def lit_lieu(id) :
    animal = Animal.objects.get(pk=id)
    try:
        return (animal.lieu)

    except:
        return("Désolé, %s n'est pas un animal connu" % id)


def verifie_disponibilite(lieu):


    equipement = Equipement.objects.get(pk=lieu)

    try :
        return(equipement.disponibilite)

    except :
        return("Désolé, %s n'est pas un equipement connu" % id)



def cherche_occupant(id):

    occupants = Animal.objects.filter(lieu=id)

    if len(occupants) != 0:
        return occupants

    else :
        return("Désolé, %s n'est pas un lieu connu" % id)

def change_etat(ida, ide):
    etats_autho = {'affame', 'fatigue', 'repus', 'endormi'}

    animal = Animal.objects.get(animal_id=ida)
    try :

        if ide in etats_autho :
            animal.etat = ide
            animal.save()

    except :
        print("Désolé, %s n'est pas un animal connu"% ida)
        return None

def change_lieu(ida, ide):

    lieu_autho = {"littière","mangeoire", "roue", "nid"}

    if ide in lieu_autho :

        if verifie_disponibilite(ide) == 'libre':

            animal = Animal.objects.get(pk=ida)

            try :
                l2 = animal.lieu
                equipement = Equipement.objects.get(pk=l2)
                equipement.disponibilite = 'libre'


                if animal.lieu != 'littière':
                    equipement1 = Equipement.objects.get(pk=ide)
                    equipement1.disponibilite = 'occupé'


                animal.lieu = ide


            except :
                print("Désolé, %s n'est pas un animal connu" % ida)
                return None
        else :
            print('%s est occupé' % ide)
            return None

    else :
        print("Désolé, %s n'est pas un lieu connu" % ide)
        return None
