import pandas
from typing import Dict, List

ROWS_OF_TABLE = {'численность': 'Численность населения, занятого в экономике МО',
                'зарплата': 'Средняя заработная плата по МО',
                 'норматив ндфл': 'Норматив отчисления НДФЛ в бюджете МО',
                 'доходы (план)': 'Консолидированные доходы бюджета МО (план)',
                 'доходы (факт)': 'Консолидированные доходы бюджета МО (план)',
                 }

def make_calculation(population: float, salary: float, Nndfl: float, Bp: float, Bf: float):
    ndfl: float = population * (salary * 0.13 * 12) / 1000
    Db: float = Bp - Bf
    PNndfl: float = (Nndfl / (ndfl * Nndfl / 100)) * (ndfl * Nndfl / 100 + Db)
    return PNndfl


def read_excel(file_name):
    df = pandas.read_excel(file_name)
    try:
        population = df[ROWS_OF_TABLE['численность']][0]
        salary = df[ROWS_OF_TABLE['зарплата']][0]
        Nndfl = df[ROWS_OF_TABLE['норматив ндфл']][0]
        Bp = df[ROWS_OF_TABLE['доходы (план)']][0]
        Bf = df[ROWS_OF_TABLE['доходы (факт)']][0]
        return {'population': population, 'salary': salary, 'Nndfl': Nndfl, 'Bp': Bp, 'Bf': Bf}
    except:
        print("In the file is not necessary data")
        return None


def make_output_file(PNndfl, file_name):
    pandas.DataFrame({'PNndfl': [PNndfl, ]}).to_excel(file_name)


data_from_excel = read_excel('input data.xlsx')

if data_from_excel is not None:
    result_of_calculations = make_calculation(*data_from_excel.values())
    make_output_file(result_of_calculations, 'result.xlsx')
    print("Successful!")
else:
    print('Here are errors with input data.')