import random
when = ['A few year ago', 'yesterday', 'last night', 'on 15th july']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle', 'a cat']
name = ['sharad', 'sanjay', 'dhanraj', 'pankaj', 'kamal']
residence = ['india', 'germany', 'france', 'canada', 'england']
went = ['cinema', 'university', 'seminar', 'school', 'hotel']
happened = ['made a lot of friends', 'eats a pizza', 'found a key', 'wrote a book', 'solved a mistery']
print(random.choice(when) + ',' + random.choice(who) + 'named ' + random.choice(name) + ' that lives in ' + random.choice(residence) + ' , went to the ' + random.choice(went) + ' and ' + random.choice(happened))