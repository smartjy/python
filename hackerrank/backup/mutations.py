def mutate_string(string, position, character):
    return

if __name__ == '__main__':
    s = input('abracadabra')
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)