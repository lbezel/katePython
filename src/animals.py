from random import randrange
# from functools import total_ordering

# @total_ordering
class Animal:
    """
    Животное которое мы размножаем
    """
    is_merry = False
    max_animal_live_year = 4
    min_animal_live_year = 0

    def __init__(self, id, id_pa = None, id_ma = None, current_year = 0, sread_index = None):
        self.id = id
        self.id_pa = id_pa
        self.id_ma = id_ma
        self.sex = randrange(2)
        self.current_year = current_year
        self.birth = current_year
        self.death = current_year + self.min_animal_live_year + randrange(self.max_animal_live_year - self.min_animal_live_year)
        self.sread_index = sread_index

    def get_age(self):
        return self.current_year - self.birth

    def get_info(self):
        return '\n' + str(self.id) + ' | ' + str(self.id_pa) + ' | ' + str(self.id_ma) + ' | ' + str(self.sex) + ' | ' + str(self.birth) + ' | ' + str(self.death) + ' | ' + str(self.is_merry) 

    def set_merry_status(self, is_merry):
        self.is_merry = is_merry