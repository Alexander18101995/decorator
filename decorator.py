from datetime import datetime

l = 'logger.txt'

def dec(func):
  def logger(a,b):
    now = datetime.now()
    res = func(a,b)
    with open('logger.txt','a', encoding='utf-8') as log:
       log.write(f'Вызов функции {func}, время - {now}\n  с результатом {res}')
  print(f'путь к логам {l}')
  return logger


@dec  
def sum(a,b):
  return a + b 

sum(4,5)