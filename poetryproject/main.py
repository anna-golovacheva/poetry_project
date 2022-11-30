import datetime


def do_something():
    name = input('Hello! Please, enter your name: ')
    now = datetime.datetime.now()
    today = now.strftime('%d, %b %Y')
    print(f'Dear {name}! Today is {today}. What a wonderful day to remind yourself you are amazing person! Thank you for making this world a better place!')
   

if __name__ == '__main__':
    do_something()

