import pandas
from typing import Dict
import rows
   


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
    try:
        population: float = df[rows.POPULATION][0]
        salary: float = df[rows.SALARY][0]
        Nndfl: float = df[rows.NORMATIV_NDFL][0]
        Bp: float = df[rows.INCOME_PLAN][0]
        Bf: float = df[rows.INCOME_FACT][0]
        return {'population': population, 'salary': salary, 'Nndfl': Nndfl, 'Bp': Bp, 'Bf': Bf}
    except:
        print("In the file is not necessary data")
        return dict()


def make_output_file(PNndfl, file_name) -> None:
    '''Gets result of calculation (float) and puts it
    in an excel file.'''
    pandas.DataFrame({'PNndfl': [PNndfl, ]}).to_excel(file_name)


data_from_excel: Dict = read_excel('input data.xlsx')

if len(data_from_excel) != 0:
    result_of_calculations: float = make_calculation(*data_from_excel.values())
    make_output_file(result_of_calculations, 'result.xlsx')
    print("Successful!")
else:
    print('Here are errors with input data.')
