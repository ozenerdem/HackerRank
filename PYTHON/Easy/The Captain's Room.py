if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
liste = sorted(integer_list)
for i in range(len(liste)):
    if i+1 < len(liste):
        if (liste[i] != liste[i - 1] and liste[i] != liste[i + 1]):
            print(liste[i])
            break;
    else:
        print(liste[i])














