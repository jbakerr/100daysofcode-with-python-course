from collections import defaultdict, namedtuple, Counter, deque
import csv
import random
from urllib.request import urlretrieve


# user = ("bob", "IT admin")

# User = namedtuple("User", "name role")

# user = User(name = "bob", role = "IT admin")

# print(f'{user.name} is a {user.role}')


# challenges_done = [('mike', 10), ('mike', 5), ("john", 9), ('ben', 1)]

# challenge = defaultdict(list)

# for name, challenges in challenges_done:
#     challenge[name].append(challenges)
# print(challenge)


words = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec suscipit tortor quis tortor dapibus hendrerit. Vestibulum a venenatis velit. Integer aliquam justo dolor, eu venenatis quam faucibus quis. Morbi et lorem nec nunc luctus congue. Vivamus a dolor vulputate, vestibulum ipsum vel, porttitor orci. Nulla auctor hendrerit eros et lobortis. Ut dignissim, mauris nec mollis maximus, ligula ex convallis mauris, et laoreet orci leo non nisi."
words = words.split(' ')

print(Counter(words).most_common(1))
