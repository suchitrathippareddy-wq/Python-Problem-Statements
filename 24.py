#Write a Python program to count how many times each word appears in a sentence using a dictionary. Take the sentence as runtime input
def word_frequency(a):
    freq = {}
    for i in a.split():
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    print("Word frequency =", freq)
a = input("Enter a sentence: ")
word_frequency(a)