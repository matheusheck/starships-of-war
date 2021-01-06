# -*- coding: utf-8 -*-

import src.modules.starships.services.InsertStarshipsService as InsertStarshipsService
import src.modules.starships.services.ListStarshipsRankedService as ListStarshipsRankedService
import src.modules.starships.services.CreateStarshipsTableService as CreateStarshipsTableService

def rank():
    print ('Welcome to Starships of War!')

    CreateStarshipsTableService.execute()
    spaceships = ListStarshipsRankedService.execute()

    if not spaceships:
        print('\n### Filling database...')
        InsertStarshipsService.execute()
        spaceships = ListStarshipsRankedService.execute()

    print('\n### All spaceships, ranked by Hyperdriver class:')

    for spaceship in spaceships:
        if spaceship.hyperdrivespeed > 0:
            print(f'{spaceship.name} has a {spaceship.hyperdrivespeed} hyperdriver class and a {spaceship.sublightspeed}000 sublight speed.')
            print('')

        else:
            print(f'{spaceship.name} has no hyperdriver class but a {spaceship.sublightspeed}000 sublight speed.')
            print('')

if __name__ == '__main__':
    rank()