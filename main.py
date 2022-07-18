import pandas
from typing import Dict

class rows():
    POPULATION = 'Численность населения, занятого в экономике МО'
    SALARY = 'Средняя заработная плата по МО'
    NORMATIV_NDFL = 'Норматив отчисления НДФЛ в бюджете МО'
    INCOME_PLAN = 'Консолидированные доходы бюджета МО (план)'
    INCOME_FACT = 'Консолидированные доходы бюджета МО (факт)'


def make_calculation(population: float, salary: float, Nndfl: float, Bp: float, Bf: float) -> float:
    '''Returns result of calculation by formula

        >>>make_calculation(23_000, 30_000, 20, 20, 10)
        20.001

        >>>make_calculation(230_000, 40_000, 240, 210, 110)
        240.001
    '''

    ndfl: float = population * (salary * 0.13 * 12) / 1000
    Db: float = Bp - Bf
    PNndfl: float = (Nndfl / (ndfl * Nndfl / 100)) * (ndfl * Nndfl / 100 + Db)
    return round(PNndfl, 3)


def read_excel(file_name) -> Dict:
    '''Gets data from excel table,
    puts it in dict and returns it.
    If in a file are errors with data, returns
    empty dict'''
    df = pandas.read_excel(file_name)
    values = [elem for elem in df.values]
    return {rows.NORMATIV_NDFL: values[0], rows.POPULATION: values[1], rows.SALARY: values[2], rows.INCOME_PLAN: values[3], rows.INCOME_FACT: rows[4]}




def make_output_file(PNndfl, file_name) -> None:
    '''Gets result of calculation (float) and puts it
    in an excel file.'''
    pandas.DataFrame({'PNndfl': [PNndfl, ]}).to_excel(file_name)

df = pandas.read_excel('input data.xlsx')

#
# if len(df) != 0:
#     result_of_calculations: float = make_calculation(*df.values())
#     make_output_file(result_of_calculations, 'result.xlsx')
#     print("Successful!")
# else:
#     print('Here are errors with input data.')
