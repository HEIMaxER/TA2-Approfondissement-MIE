from .models import *

def nourrir(id) :

    if lit_etat(id) == 'affame':

        if verifie_disponibilite('mangeoire') == 'libre' :

            change_lieu(id, 'mangeoire')
            change_etat(id, 'repus')

        else :
            return("Désolé, la mangeoire est occupée par %s" % [cherche_occupant('mangeoire')])

    else:
        print("Désolé, %s n'a pas faim" % id)

def divertir(animal_id) :

    if lit_etat(animal_id) == 'repus':

        if verifie_disponibilite('roue') == 'libre' :

            change_lieu(animal_id, 'roue')
            change_etat(animal_id, 'fatigué')

        else :
            return("Désolé, la roue est occupée par %s" % (cherche_occupant('roue'),))

    else:
        print("Désolé, %s n'est pas en état de faire du sport!" % animal_id)

def coucher(animal_id) :
    print('Done')
    if lit_etat(animal_id) == 'fatigué':
        print('Done')
        if verifie_disponibilite('nid') == 'libre' :

            change_lieu(animal_id, 'nid')
            print('Done')
            change_etat(animal_id, 'endormi')
        else :
            return("Désolé, le nid est occupée par ", cherche_occupant('nid'))

    else:
        print("Désolé, %s n'est pas fatigué!" % animal_id)

def reveiller(animal_id) :

    if lit_etat(animal_id) == 'endormi':

        if verifie_disponibilite('litière') == 'libre' :
            print('Done')
            change_lieu(animal_id, 'litière')
            change_etat(animal_id, 'affamé')

        else :
            return("Désolé, la littière est occupée par ", cherche_occupant('litière'))

    else:
        print("Désolé, %s ne dors pas !" % animal_id)