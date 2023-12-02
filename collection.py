#from collections import Counter
#a = "aaaaaaabbbbbbcccc"
#my_counter = Counter(a)
#print(my_counter)
#print(list(my_counter.elements()))
#from collections import namedtuple
#point = namedtuple('point','x,y')
#pt = point(1,-4)
#print(pt.x,pt.y)

#from collections import OrderedDict
#ordered_dict = OrderedDict()
#ordered_dict['b'] = 2
#ordered_dict['c'] = 3
#ordered_dict['d'] = 4
#ordered_dict['e'] = 5
#ordered_dict['f'] = 6
#ordered_dict['g'] = 1
#print(ordered_dict)

#from collections import defaultdict
#d = defaultdict(list)
#d['a'] = 1
#d['b'] = 2
#print(d['c'])

from collections import deque
d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
print(d)
d.extendleft([4,5,6])
print(d)
d.rotate(-1)
print(d)