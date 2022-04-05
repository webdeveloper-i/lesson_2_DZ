some_list = [57.8, 46.51, 97, 57.8, 4546.51, 44.97, 567.85, 406.1, 907, 5557.8, 4651, 0.97, 2572, 4.51, 97.5, 57.08, 6.51, 9.7]
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