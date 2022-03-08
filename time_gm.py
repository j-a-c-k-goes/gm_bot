from emojis import *
from units_of_time import *
from like_as_with import *
from emo_ingredients import *

def time_gm(units_of_time, like_as_with, general_emojis, emo_ingredients):
    x = random.choice(units_of_time)
    y = random.choice(like_as_with)
    z = random.randrange(2,9999)
    a = random.choice(general_emojis)
    b = random.choice(emo_ingredients)
    output_a =  f'the first {z} {x} of this morning are yours'
    output_b = f'this morning happened in {z} {x} {a}'
    outputs = [ output_a, output_b]
    xyz = random.choice(outputs)
    return f'{xyz}'

if __name__ == "__main__":
    print('--- using time based gm reply ---')
    time_gm(units_of_time, like_as_with, general_emojis, emo_ingredients)