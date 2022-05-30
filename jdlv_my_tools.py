# -*- coding: utf-8 -*-
"""

"""
from random import randint
from os import listdir
from os.path import isfile, join
import random
import time
import json

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

from jdlv_data import *
from jdlv_model import *
from jdlv_outils import *

def clean_grid (grid):
    for i in range (default_grid_size):
        for j in range (default_grid_size):
            grid.cases [i][j]['s'] = death_status
            grid.cases [i][j]['c'] = death_color
    return grid


def apply_game_of_life_rules (grid):
    previous_grid = grid
    previous_cases = previous_grid.cases
    cases = grid.cases # cases is a list of lists of dictionnaries
    next_grid = Grid (len (cases))
    next_cases = next_grid.cases
    for i in range (1, len(cases)-1):
        for j in range (27, 78):
                previous_status = cases [i][j]['s']
                voisins = get_voisins (cases, i, j)
                nbre_alive_voisins = count_alive_voisins (voisins)
                if nbre_alive_voisins == 3:
                    next_cases [i] [j] = revive_case (next_cases [i] [j])
                elif nbre_alive_voisins <= 1 or nbre_alive_voisins >= 4:
                    next_cases [i] [j] = kill_case (next_cases [i] [j])
                else:
                    next_cases [i] [j] = cases [i] [j]
    for i in range (26, len(cases)-1):
        for j in range (1, 26):
                previous_status = cases [i][j]['s']
                voisins = get_voisins (cases, i, j)
                nbre_alive_voisins = count_alive_voisins (voisins)
                if nbre_alive_voisins == 3:
                    next_cases [i] [j] = revive_case (next_cases [i] [j])
                elif nbre_alive_voisins <= 1 or nbre_alive_voisins >= 4:
                    next_cases [i] [j] = kill_case (next_cases [i] [j])
                else:
                    next_cases [i] [j] = cases [i] [j]
    for i in range (1, 22):
        for j in range (1, 23):
                previous_status = cases [i][j]['s']
                voisins = get_voisins (cases, i, j)
                nbre_alive_voisins = count_alive_voisins (voisins)
                if nbre_alive_voisins == 3:
                    next_cases [i] [j] = revive_case (next_cases [i] [j])
                elif nbre_alive_voisins <= 1 or nbre_alive_voisins >= 4:
                    next_cases [i] [j] = kill_case (next_cases [i] [j])
                else:
                    next_cases [i] [j] = cases [i] [j]
    for i in range (1, len(cases)-1):
        for j in range (77, len(cases)-1):
            next_cases[i][j]['s'] = cases[i][j]['s']
            next_cases[i][j]['c'] = cases[i][j]['c']
    for i in range (1, 22):
        for j in range (24, 26):
            next_cases[i][j]['s'] = cases[i][j]['s']
            next_cases[i][j]['c'] = cases[i][j]['c']
    for i in range (23, 25):
        for j in range (24, 26):
            next_cases[i][j]['s'] = cases[i][j]['s']
            next_cases[i][j]['c'] = cases[i][j]['c']
    return next_grid

def apply_game_of_life_rulesA (grid):
    previous_grid = grid
    previous_cases = previous_grid.cases
    cases = grid.cases # cases is a list of lists of dictionnaries
    next_grid = Grid (len (cases))
    next_cases = next_grid.cases
    for i in range (1, len(cases)-1):
        for j in range (26, 78):
                previous_status = cases [i][j]['s']
                voisins = get_voisins (cases, i, j)
                nbre_alive_voisins = count_alive_voisins (voisins)
                if nbre_alive_voisins == 3:
                    next_cases [i] [j] = revive_case (next_cases [i] [j])
                elif nbre_alive_voisins <= 1 or nbre_alive_voisins >= 4:
                    next_cases [i] [j] = kill_case (next_cases [i] [j])
                else:
                    next_cases [i] [j] = cases [i] [j]
    for i in range (25, len(cases)-1):
        for j in range (1, 26):
                previous_status = cases [i][j]['s']
                voisins = get_voisins (cases, i, j)
                nbre_alive_voisins = count_alive_voisins (voisins)
                if nbre_alive_voisins == 3:
                    next_cases [i] [j] = revive_case (next_cases [i] [j])
                elif nbre_alive_voisins <= 1 or nbre_alive_voisins >= 4:
                    next_cases [i] [j] = kill_case (next_cases [i] [j])
                else:
                    next_cases [i] [j] = cases [i] [j]
    for i in range (1, len(cases)-1):
        for j in range (77, len(cases)-1):
            next_cases[i][j]['s'] = cases[i][j]['s']
            next_cases[i][j]['c'] = cases[i][j]['c']
    for i in range (1, 22):
        for j in range (24, 25):
            next_cases[i][j]['s'] = cases[i][j]['s']
            next_cases[i][j]['c'] = cases[i][j]['c']
    for i in range (23, 24):
        for j in range (24, 25):
            next_cases[i][j]['s'] = cases[i][j]['s']
            next_cases[i][j]['c'] = cases[i][j]['c']
    return next_grid


def apply_game_of_life_rulesZ (grid):
    previous_grid = grid
    previous_cases = previous_grid.cases
    cases = grid.cases # cases is a list of lists of dictionnaries
    next_grid = Grid (len (cases))
    next_cases = next_grid.cases
    for i in range (1, len(cases)-1):
        for j in range (1, 78):
                previous_status = cases [i][j]['s']
                voisins = get_voisins (cases, i, j)
                nbre_alive_voisins = count_alive_voisins (voisins)
                if nbre_alive_voisins == 3:
                    next_cases [i] [j] = revive_case (next_cases [i] [j])
                elif nbre_alive_voisins <= 1 or nbre_alive_voisins >= 4:
                    next_cases [i] [j] = kill_case (next_cases [i] [j])
                else:
                    next_cases [i] [j] = cases [i] [j]
    for i in range (1, len(cases)-1):
        for j in range (77, len(cases)-1):
            next_cases[i][j]['s'] = cases[i][j]['s']
            next_cases[i][j]['c'] = cases[i][j]['c']
    return next_grid


def make_tank(grid, i, j, color):
    try:
        cases = grid.cases
        cases[i][j]['s'] = life_status
        cases[i][j]['c'] = color
        cases[i-1][j]['s'] = life_status
        cases[i-1][j]['c'] = color
        cases[i-1][j-1]['s'] = life_status
        cases[i-1][j-1]['c'] = color
        cases[i-1][j-2]['s'] = life_status
        cases[i-1][j-2]['c'] = color
        cases[i-1][j+1]['s'] = life_status
        cases[i-1][j+1]['c'] = color
        cases[i+1][j+1]['s'] = life_status
        cases[i+1][j+1]['c'] = color
        cases[i+2][j+1]['s'] = life_status
        cases[i+2][j+1]['c'] = color
        cases[i+1][j]['s'] = life_status
        cases[i+1][j]['c'] = color
        cases[i+2][j]['s'] = life_status
        cases[i+2][j]['c'] = color
        cases[i+1][j-1]['s'] = life_status
        cases[i+1][j-1]['c'] = color
        cases[i+2][j-1]['s'] = life_status
        cases[i+2][j-1]['c'] = color
        cases[i+1][j-2]['s'] = life_status
        cases[i+1][j-2]['c'] = color
        cases[i+2][j-2]['s'] = life_statusus
        cases[i+2][j-2]['c'] = color
    except:
        pass
    return grid

def make_bullet(grid, i, j, color):
    try:
        cases = grid.cases
        cases[i-1][j]['s'] = life_status
        cases[i-1][j]['c'] = color
        cases[i-1][j-1]['s'] = life_status
        cases[i-1][j-1]['c'] = color
        cases[i-1][j+1]['s'] = life_status
        cases[i-1][j+1]['c'] = color
        cases[i][j-1]['s'] = life_status
        cases[i][j-1]['c'] = color
        cases[i+1][j]['s'] = life_status
        cases[i+1][j]['c'] = color
    except:
        pass
    return grid

def wall(grid, color):
    try:
        cases = grid.cases
        for i in range(1, 22):
            for j in range(24, 26):
                cases[i][j]['s'] = life_status
                cases[i][j]['c'] = color
        for i in range(23, 25):
            for j in range(24, 26):
                cases[i][j]['s'] = life_status
                cases[i][j]['c'] = color
    except:
        pass
    return grid

def wallA(grid, color):
    try:
        cases = grid.cases
        for i in range(1, 22):
            for j in range(24, 25):
                cases[i][j]['s'] = life_status
                cases[i][j]['c'] = color
        for i in range(23, 24):
            for j in range(24, 25):
                cases[i][j]['s'] = life_status
                cases[i][j]['c'] = color
    except:
        pass
    return grid



def apply_rules (grid, compteur):
    next_grid = grid
    compt = len(cases) - 1
    for s in range(25):
        next_grid = clean_grid(grid)
        compt = compt - 1
        next_grid = make_tank(grid, 40, compt, red)
        next_grid = make_tank(grid, 55, compt, red)
        next_grid = make_tank(grid, 70, compt, red)
    next_grid = wall(grid, black)
    for d in range (1, 200):
        if compteur %20 == O:
            shoot = randint(1, 3)
            if shoot == 1:
                shoot = 45
            elif shoot == 2:
                shoot = 60
            else:
                shoot = 75
            next_grid = make_bullet(grid, shoot, 70, black)
        else:
            next_grid = apply_game_of_life_rules(grid)
    next_grid = wallA(grid)
    for d in range (1, 200):
        if compteur %20 == O:
            shoot = randint(1, 3)
            if shoot == 1:
                shoot = 45
            elif shoot == 2:
                shoot = 60
            else:
                shoot = 75
            next_grid = make_bullet(grid, shoot, 70, black)
        else:
            next_grid = apply_game_of_life_rulesA(grid)
    for f in range(1, 50):
        next_grid = apply_game_of_life_rulesZ(grid)
        next_grid = clean_grid(grid)
    return next_grid









