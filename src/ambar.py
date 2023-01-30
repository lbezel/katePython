import time
from random import randrange
from functools import lru_cache
from src import Animal

class Ambar:
    """
    Live and animals information
    """

    current_year = 1
    max_year = 15
    max_children_len = 4
    min_children_len = 0
    animals_list = []
    grave_list = []
    history = []

    def __init__(self, name, start_animals_len):
        self.name = name
        self.start_animals_len = start_animals_len
        for i in range(start_animals_len):
            self.animals_list.append(Animal(i))

    def get_animals_live_death(self, animals_list = []):
        live_animals = []
        death_animals = self.grave_list
        if len(animals_list) == 0:
            animals_list = self.animals_list

        for i in range(len(animals_list)):
            if animals_list[i].death >= self.current_year:
                live_animals.append(animals_list[i])
            else:
                death_animals.append(animals_list[i])

        return [live_animals, death_animals]

    def log_history(self):
        animals_live_death = self.get_animals_live_death(self.animals_list)
        self.history.append('\n' + str(self.current_year) + ' | ' + str(len(animals_live_death[0]) + len(animals_live_death[1])) + ' | ' + str(len(animals_live_death[0])) + ' | ' + str(len(animals_live_death[1])))

    @lru_cache
    def get_short_info(self):
        def get_animals_history():
            info = ''
            for i in range(len(self.history)):
                info += self.history[i]
            return info

        return f"""year | all | live | death
-----|-----|------|------{get_animals_history()}
"""

    def get_info(self):
        animals_live_death = self.get_animals_live_death(self.animals_list)

        def get_animals_info():
            info = ''
            animals = self.animals_list[:500] 
            for i in range(len(animals)):
                info += self.animals_list[i].get_info()
            return info

        return f"""# THE ANIMALS { self.name }

Len  : { str(len(self.animals_list)) }
Live : { str(len(animals_live_death[0])) }
Death: { str(len(animals_live_death[1])) }

## history

{self.get_short_info()}

## All animals

id | id_pa | id_ma | sex | birth | death | is_merry
---|-------|-------|-----|-------|-------|---------{get_animals_info()}
"""

    def create_info_file(self):
        with open("./animals/animals_" + str(self.max_year) + "_" + str(time.time()) + ".md", "w") as f: 
            f.write(self.get_info())

    def get_opposite_animals_list(self, current_animal):
        opposite_animals_list = []
        for opposite_animal_id in range(len(self.animals_list)):
            if (self.animals_list[opposite_animal_id].sex != current_animal.sex) and (self.animals_list[opposite_animal_id].is_merry == False) and (self.animals_list[opposite_animal_id].death < self.current_year) and (self.animals_list[opposite_animal_id].id != current_animal.id_pa) and (self.animals_list[opposite_animal_id].id != current_animal.id_ma): 
                opposite_animals_list.append(self.animals_list[opposite_animal_id])
        return opposite_animals_list

    def add_childrens(self, pa_id, ma_id):
        for i in range(self.min_children_len + randrange(self.max_children_len - self.min_children_len)):
            self.animals_list.append(Animal(
                len(self.animals_list),
                pa_id,
                ma_id,
                self.current_year,
                i
            ))

    def spread_animal(self):
        for i in range(len(self.animals_list)):
            current_animal = self.animals_list[i]

            if current_animal.death < self.current_year:
                # На будущее
                # self.grave_list.append(self.animals_list[i])
                # del self.animals_list[i]
                continue

            opposite_animals_list = self.get_opposite_animals_list(current_animal)
            if len(opposite_animals_list) == 0:
                continue

            current_animal_partner = opposite_animals_list[randrange(len(opposite_animals_list))]
            current_animal_partner.set_merry_status(True)
            current_animal.set_merry_status(True)

            pa_id = None
            ma_id = None

            if current_animal.sex == 0:
                ma_id = current_animal.id
                pa_id = current_animal_partner.id
            else:
                ma_id = current_animal_partner.id
                pa_id = current_animal.id

            self.add_childrens(pa_id, ma_id)

    def spread(self):
        for year in range(self.max_year):
            self.current_year = year
            self.log_history()
            # set status is merry on False
            for i in range(len(self.animals_list)):
                self.animals_list[i].set_merry_status(False)

            self.spread_animal()