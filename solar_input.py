from solar_objects import *
import math
STATS = open("stats.txt", 'w')


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star" or object_type == "planet":
                objectt = SpaceObject()
                parse_parameters(line, objectt)
                objects.append(objectt)
            else:
                print("Unknown space object")

    return objects


def parse_parameters(line, obj):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **obj** — небесный объект.
    """
    line = line.replace('\n', '')
    line = line.split(' ')
    obj.type = line[0]
    obj.R = int(line[1])
    obj.color = line[2]
    obj.m = float(line[3])
    obj.x = float(line[4])
    obj.y = float(line[5])
    obj.Vx = float(line[6])
    obj.Vy = float(line[7])


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """

    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            out_file.write(str(obj.type) + ' ' + str(obj.R) + ' ' + str(obj.color) + ' ' + str(obj.m) + ' ' + str(obj.x)
                           + ' ' + str(obj.y) + ' ' + str(obj.Vx) + ' ' + str(obj.Vy) + '\n')
    out_file.close()


def stats(space_objects, time):
    """
    Сохранение статистики в файл object
    Функция записывает на каждой итерации расчёта данные
    **space_objects** — список объектов планет и звёзд
    **time** - текущее время расчёта
    """
    star_x = 0
    star_y = 0
    for obj in space_objects:
        if obj.type == "Star":
            star_y = obj.y
            star_x = obj.x
        else:
            STATS.write(str(math.sqrt((obj.x - star_x)**2 + (obj.y - star_y)**2)) + ' '
                        + str(math.sqrt(obj.Vx**2 + obj.Vy**2)) + ' ' + str(time) + '\n')


if __name__ == "__main__":
    print("This module is not for direct call!")
