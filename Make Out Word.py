"""
Make Out Word
https://codingbat.com/prob/p129981

Give an "outside" string, length of 4, such as "<<>>" or "[[]]", and a word, return a new string where the word is in the 
middle of the out string, e.g. "<<word>>".

make_out_word('<<>>', 'Yay') → '<<Yay>>'
make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
make_out_word('[[]]', 'word') → '[[word]]'
"""
def make_out_word(out, word):
    left = out[:2]
    right = out[2:]
    print(left + word + right)

make_out_word("[[]]", "Carol Baskin")