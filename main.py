import pandas


def make_calculation(population, salary, Nndfl, Bp, Bf):
    ndfl = population * (salary * 0.13 * 12) / 1000
    Db = Bp - Bf
    PNndfl = (Nndfl / (ndfl * Nndfl / 100)) * (ndfl * Nndfl / 100 + Db)
    return PNndfl


def read_excel(file_name):
    data_frame_object = pandas.read_excel(file_name)
    try:
        population = data_frame_object['Численность населения, занятого в экономике МО'][0]
        salary = data_frame_object['Средняя заработная плата по МО'][0]
        Nndfl = data_frame_object['Норматив отчисления НДФЛ в бюджете МО'][0]
        Bp = data_frame_object['Консолидированные доходы бюджета МО (план)'][0]
        Bf = data_frame_object['Консолидированные доходы бюджета МО (факт)'][0]
        return {'population': population, 'salary': salary, 'Nndfl': Nndfl, 'Bp': Bp, 'Bf': Bf}
    except Exception:
        print("В файле нет необходимых данных")


def make_output_file(PNndfl, file_name):
    pandas.DataFrame({'PNndfl': [PNndfl, ]}).to_excel(file_name)


data_from_excel = read_excel('input data.xlsx')
result_of_calculations = make_calculation(*data_from_excel.values())
make_output_file(result_of_calculations, 'result.xlsx')