
# layer 0: Background Objects
# layer 1: Foreground Objects
# layer 2: Crash Object
# layer 3: Heart Image
objects = [[],[],[]]


def add_object(o, layer):
    objects[layer].append(o)


def remove_object(o):
    for i in range(len(objects)):
        if o in objects[i]:
            objects[i].remove(o)
            del o
            return


def clear():
    global objects
    for o in all_objects():
        del o
    objects.clear()
    objects = [[], [], []]


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def check_object(layer):
    for i in objects[layer]:
        yield i


def all_objects():
    for i in range(len(objects)):
        for o in objects[i]:
            yield o

