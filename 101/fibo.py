from pyfiglet import Figlet


def fibonacci(quantity, font):
    sequence = [0, 1]
    f = Figlet(font=font)

    if quantity >= 2:
        for i in range(quantity - 2):
            sequence.append(sequence[i] + sequence[i + 1])
        print('The number you are looking for is', f.renderText(str(sequence[quantity - 1])))
    else:
        print('quantity must be >= 2')


if __name__ == '__main__':
    nice_font = 'char1___'
    super_font = 'doh'
    print('Enter N:')
    N = int(input())
    fibonacci(N, super_font)