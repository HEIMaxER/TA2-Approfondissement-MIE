from django.test import TestCase


from .models  import lit_etat
from .controleur import *

def test_lit_etat():
    assert lit_etat('Tac') == 'affame'


def test_lit_etat_nul():
    assert lit_etat('Bob') == None


def test_lit_lieu():
    assert lit_lieu('Tac') == 'litiere'


def test_lit_lieu_nul():
    assert lit_lieu('Bob') == None

def test_vérifie_disponibilité():
    assert verifie_disponibilite('litiere') == 'libre'
    assert verifie_disponibilite('nid') == 'occupe'

def test_vérifie_disponibilité_nul():
    assert verifie_disponibilite('nintendo') == None

def test_cherche_occupant():
    assert cherche_occupant('nid') == ['Pocahontas']
    assert 'Tac' in cherche_occupant('litiere')
    assert 'Tac' not in cherche_occupant('mangeoire')

def test_cherche_occupant_nul():
    assert cherche_occupant('casino') == None

def test_change_état():
    change_etat('Totoro', 'fatigue')
    assert lit_etat('Totoro') == 'fatigue'
    change_etat('Totoro', 'excité comme un pou')
    assert lit_etat('Totoro') == 'fatigue'
    change_etat('Bob', 'fatigue')
    assert lit_etat('Bob') == None

def test_change_lieu():
    change_lieu('Totoro', 'roue')
    assert lit_lieu('Totoro') == 'roue'
    assert verifie_disponibilite('litiere') == 'libre'
    assert verifie_disponibilite('roue') == 'occupe'

def test_change_lieu_occupé():
    change_lieu('Totoro', 'nid')
    assert lit_lieu('Totoro') == 'roue'

def test_change_lieu_nul_1():
    change_lieu('Totoro', 'nintendo')
    assert lit_lieu('Totoro') == 'roue'

def test_change_lieu_nul_2():
    change_lieu('Bob', 'litiere')
    assert lit_lieu('Bob') == None

def test_nourrir():
    if verifie_disponibilite('mangeoire') == 'libre' and lit_etat('Tic') == 'affame':
        nourrir('Tic')
    assert verifie_disponibilite('mangeoire') == 'occupe'
    assert lit_etat('Tic') == 'repus'
    assert lit_lieu('Tic') == 'mangeoire'
    nourrir('Tac')
    assert lit_etat('Tac') == 'affame'
    assert lit_lieu('Tac') == 'litiere'
    nourrir('Pocahontas')
    assert lit_etat('Pocahontas') == 'endormi'
    assert lit_lieu('Pocahontas') == 'nid'
    nourrir('Bob')
    assert lit_etat('Bob') == None
    assert lit_lieu('Bob') == None
    assert verifie_disponibilite('mangeoire') == 'occupe'