#了不起的魔术师
def show_magicians(magicians):
    for magician in magicians:
        print(magician)


magician_names = ['ava', 'martin', 'jim', 'jack']
make_great = []
while magician_names:
    current_make_great = "the great " + magician_names.pop()
    make_great.append(current_make_great)


show_magicians(make_great)
