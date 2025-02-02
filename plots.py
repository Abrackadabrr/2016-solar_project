import matplotlib.pyplot as plt


def get_params(filename):
    """
    Считываю данные из файлика в массив и возвращю его
    :param filename: имя файла в этой же директории
    return: лист времени и кортеж (лист[расстояние], лист[скорость])
    """
    list_of_velocity = []
    list_of_distance = []
    list_of_time = []
    list_of_data = []

    with open(filename, 'r') as in_file:
        list_of_strings = in_file.read().splitlines()

    for string in list_of_strings:
        list_of_data.append(string.split(" "))

    for lists in list_of_data:

        list_of_distance.append(float(lists[0]) / 150000000000)
        list_of_velocity.append(float(lists[1]) / 1000)
        list_of_time.append(float(lists[2]) / (60 * 60 * 23.965 * 365))

    return list_of_time, (list_of_distance, list_of_velocity)


def build_plot(name_of_subplot, tup_data, color):
    """
    Строит график на соответвующем поле
    **name_of_subplot** - имя поля
    **tup_dta** - кортеж из (х, у)
    **color** - цвет линии
    """
    name_of_subplot.plot(tup_data[0], tup_data[1], '-', label='stl', color=color)


def plot(together=False):
    """
    Строит графики по данным в файле "stats.txt"
    """
    time, planet_params = get_params("stats.txt")

    if together:
        fig, sub = plt.subplots(1, 3, figsize=(18, 6))

        build_plot(sub[0], (time, planet_params[1]), 'red')
        build_plot(sub[1], (time, planet_params[0]), 'blue')
        build_plot(sub[2], (planet_params[0], planet_params[1]), 'green')

        plt.grid()
        sub[0].set_xlabel('Time, s')
        sub[0].set_ylabel('Velocity, km/s')
        sub[1].set_xlabel('Time, s')
        sub[1].set_ylabel('Distance, au')
        sub[2].set_xlabel('Distance, au')
        sub[2].set_ylabel('Velocity, km/s')

        plt.show()
        fig.suptitle('Planet parameter\'s')
        fig.savefig('Planet param.png')
    else:
        fig, vel = plt.subplots()
        build_plot(vel, (time, planet_params[1]), 'red')

        vel.set_xlabel('Time, years')
        vel.set_ylabel('Velocity, km/s')
        vel.set_title('Speed versus time dependence')
        plt.grid()
        fig.savefig('vel.png')

        fig, dist = plt.subplots()
        build_plot(dist, (time, planet_params[0]), 'blue')

        dist.set_xlabel('Time, years')
        dist.set_ylabel('Distance, au')
        dist.set_title('Distance versus time dependence')
        plt.grid()
        fig.savefig('dist.png')

        fig, v_d = plt.subplots()
        build_plot(v_d, (planet_params[0], planet_params[1]), 'green')

        v_d.set_xlabel('Distance, au')
        v_d.set_ylabel('Velocity, km/s')
        v_d.set_title('Speed versus distance dependence')
        fig.savefig('dst_vel.png')

        plt.grid()
        plt.show()
