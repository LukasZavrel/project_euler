#%%
ten = {
1: 'one',
2: 'two',
3: 'three',
4: 'four',
5: 'five',
6: 'six',
7: 'seven',
8: 'eight',
9: 'nine'}
twenty = {
10:	'ten',
11:	'eleven',
12:	'twelve',
13:	'thirteen',
14:	'fourteen',
15:	'fifteen',
16:	'sixteen',
17:	'seventeen',
18:	'eighteen',
19:	'nineteen',
}
hundred = {
20:	'twenty',
30:	'thirty',
40:	'forty',
50:	'fifty',
60:	'sixty',
70:	'seventy',
80:	'eighty',
90:	'ninety',
}
thousand = 'onethousand'
hundred_and = 'hundredand'
ten_count = sum([len(val) for val in ten.values()])
twenty_count = sum([len(val) for val in twenty.values()])
hundred_count = sum([len(val) for val in hundred.values()])
count_100 = twenty_count + 10 * hundred_count + 9*ten_count
count_1000 = count_100 * 10 + ten_count * 100 + 899*len(hundred_and)
print(count_1000)


