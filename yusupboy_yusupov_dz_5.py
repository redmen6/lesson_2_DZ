from random import uniform
some_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]
print(some_list)
print(f' id до сортировки: {id(some_list)}')
some_list.sort()
print(id(some_list))
print(f' id после сортировки: {id(some_list)}')
new_list = sorted(some_list, reverse=True)[0:5]
new_list.sort()
print(f'id new_list: {id(new_list)}')
res_str = ''

for ind, element in enumerate(new_list):
    sena_v_kop = element*100
    sena_rub = int(sena_v_kop//100)
    sena_kop = int(sena_v_kop%100)
    sena_rub = str(sena_rub)
    sena_kop = str(sena_kop).zfill(2)
    res_str += f'{sena_rub} руб {sena_kop} коп, '
res_str = res_str[0:len(res_str)-2]+'.'
print(res_str)
