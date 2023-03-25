# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля
from operator import itemgetter

csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_users_list():
    data = read_data(csv=csv)
    data = filter_data(data)
    result = sort_data(data)
    return result


def read_data(csv):
    data = []
    for line in csv.split('\n'):
        name, age = line.split(';')
        data.append({'name': name, 'age': int(age)})
    return data


def filter_data(data):
    for person in data:
        if int(person['age']) < 10:
            data.remove(person)
    return data


def sort_data(data):
    return sorted(data, key=itemgetter('age'))


if __name__ == '__main__':
    print(get_users_list())
