from datetime import datetime
import requests

def decor(func):
  def foo(*args, **kwargs):
    date_time = datetime.now()
    func_name = func.__name__
    result = func(*args, **kwargs)
    with open('decoratorlogs.txt', 'w', encoding='utf-8') as file:
      file.write(f'Дата/время: {date_time}\n'
                 f'Имя функции: {func_name}\n'
                 f'Аргументы: {args, kwargs}\n'
                 f'Результат: {result}\n')
    return result
  return foo

@decor
def get_status(*args, **kwargs):
    url = ','.join(args)
    response = requests.get(url=url)
    return response.status_code
get_status('https://github.com/')
