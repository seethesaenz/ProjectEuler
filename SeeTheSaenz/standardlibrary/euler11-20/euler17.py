def number2wordcounter():
    number2word = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9:'nine',
                   10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
                   17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 100: 'hundred'}
    tens1 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    string = []
    end = ''
    count = 0
    for i in range(1000):
        if 1 <= i <= 19:
            string.append(number2word[i])
        elif 20 <= i <= 99:
            tens, belowten = divmod(i, 10)
            string.append(tens1[tens - 2])
            if belowten > 0:
                string.append(number2word[belowten])
        elif 100 <= i:
            hundreds, belowhundred = divmod(i, 100)
            stringhun = str(hundreds)
            string.append(number2word[int(stringhun[0])])
            string.append(number2word[100])
            if belowhundred > 0:
                string.append('and')
            if 1 <= belowhundred <= 19:
                string.append(number2word[belowhundred])
            elif 20 <= belowhundred <= 99:
                tens2, belowten1 = divmod(belowhundred, 10)
                string.append(tens1[tens2-2])
                if belowten1 > 0:
                    string.append(number2word[belowten1])
        stringhun = ''
        print(string)
    end = ''.join(string)
    for i in end:
        count += 1
    return count
print(number2wordcounter())
