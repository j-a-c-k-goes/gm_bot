''' gm bot self messages '''
def gm_bot_self():
    output_a = f'gm_bot™\tbooting from terminal'
    output_b = f'--- going to Trav\'s World Server @ {SERVER}\tworking in {TEST_CHANNEL} ---'
    outputs = [output_a, output_b]
    xyz = random.choice(outputs)
    return xyz
if __name__ == '__main__':
    print('--- gmBot to self ---')
    gm_bot_self()
