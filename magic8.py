import random

ball = ('Outlook not so good','Yes','No way','Most Definitely','Cannot predict now','Reply hazy','Sorry, technical difficulties','50-50')

q = input('Whats ur question?\n')
if q=="":
    print("You didn't ask anything!")
elif not q.endswith('?'):
    print("Doesn't a question end with ?")
else:
    print(random.choice(ball))


