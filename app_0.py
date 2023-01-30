import atexit
from src import Ambar

@atexit.register
def end_func():
    print('>>> END\n')

if __name__ == '__main__':
    print('\n>>> START\n')
    is_animals_death = True
    count = 0
    while is_animals_death:
        ambar = Ambar('Super_Ambar', 10)
        ambar.spread()
        print(ambar.get_short_info())
        count += 1

        if len(ambar.get_animals_live_death()[0]) > 0:
            ambar.create_info_file()
            print('Итераций' + str(count))
            is_animals_death = False
            break
