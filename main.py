"""
CSE 163
Eric Kim, Daniel Lee, Zachary Zhang

Runs the different tasks to generate the data used in report.md
"""
import file_processing
import task_1
import task3

import pickle


def main():
    with open('./data/avocados_shp.df', 'rb') as f:
        data = pickle.load(f)
    task_1.plot_total_volume(data)
    task_1.plot_average_price(data)
    task_1.plot_price_vs_volume(data)
    task_1.plot_seattle(data)

    data3 = file_processing.avocados_for_a_home()
    task3.plot_avocados_for_a_house(data3)
    task3.plot_avocado_toast_for_a_house(data3)


if __name__ == '__main__':
    main()
