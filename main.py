import pandas
from typing import Dict


class rows():
    POPULATION = 'Численность населения, занятого в экономике МО'
    SALARY = 'Средняя заработная плата по МО'
    NORMATIV_NDFL = 'Норматив отчисления НДФЛ в бюджете МО'
    INCOME_PLAN = 'Консолидированные доходы бюджета МО (план)'
    INCOME_FACT = 'Консолидированные доходы бюджета МО (факт)'

    @classmethod
    def get_all_params(self):
        return [self.NORMATIV_NDFL, self.POPULATION, self.SALARY, self.INCOME_PLAN, self.INCOME_FACT]


def make_calculation(population: float, salary: float, Nndfl: float, Bp: float, Bf: float) -> float:
    '''Returns result of calculation by formula

        >>> make_calculation(23_000, 30_000, 20, 20, 10)
        20.001

        >>> make_calculation(230_000, 40_000, 240, 210, 110)
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
    empty dict

    >>> read_excel('wrong_test1.xlsx')
    Ошибка с параметром "Численность населения, занятого в экономике МО"
    {}

    >>> read_excel('wrong_test2.xlsx')
    Ошибка с параметром "Норматив отчисления НДФЛ в бюджете МО"
    {}

    >>> read_excel('right-test.xlsx')
    {'Норматив отчисления НДФЛ в бюджете МО': 10, 'Численность населения, занятого в экономике МО': 20, 'Средняя заработная плата по МО': 30, 'Консолидированные доходы бюджета МО (план)': 40, 'Консолидированные доходы бюджета МО (факт)': 50}

    '''
    df = pandas.read_excel(file_name)
    result = dict()
    for key in rows.get_all_params():
        try:
            result[key] = df[key][0]

        except:
            print(f'Ошибка с параметром "{key}"')

            return {}

    return result

def make_output_file(PNndfl, file_name) -> None:
    '''Gets result of calculation (float) and puts it
    in an excel file.'''
    pandas.DataFrame({'PNndfl': [PNndfl, ]}).to_excel(file_name)


df = read_excel('input data.xlsx')

if len(df) != 0:
    result_of_calculations: float = make_calculation(*df.values())
    make_output_file(result_of_calculations, 'result.xlsx')

