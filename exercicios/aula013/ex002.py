from time import sleep

for contador in range(10, -1, -1):
    print(f'\33[1;33m{contador}')

    sleep(1)

print('\n\33[1;32mImagine fogos de artifício estourando.\33[m')