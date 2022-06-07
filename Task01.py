sentence = input('Введите предложение:')
print(' '.join([i for i in sentence.split(' ') if i.find('абв') == -1]))