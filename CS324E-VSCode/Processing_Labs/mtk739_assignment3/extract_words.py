import sys
import re
from collections import Counter


def write_unique_words(word_freq):
	sorted_word_freq = sorted(word_freq,key=lambda tup: tup[1])
	unique_words_txt = open("uniquewords.txt", "w")
	for tup in sorted_word_freq:
		if tup[1] == 1:
			unique_words_txt.write(tup[0]+"\n")
	unique_words_txt.close()



def word_freq(novel_arr):

	word_freq_dict = Counter(novel_arr).most_common()

	freqs = []
	for x in word_freq_dict:
		freqs.append(int(x[1]))
	word_freq_freq_dict = Counter(freqs).most_common()
	word_freq_freq_dict.sort(key=lambda tup: tup[0])

	return word_freq_dict, word_freq_freq_dict


def write_word_freq(word_freq_freq):
	word_freq_txt = open("wordfrequency.txt", "w")
	for tup in word_freq_freq:
		word_freq_txt.write("{}: {}\n".format(tup[0], tup[1]))
	word_freq_txt.close()


def all_words(lines):
	all_words_list = []
	for line in lines:
		for word in line:
			all_words_list.append(word)
	return all_words_list


def write_all_words(novel_all_words):
	all_words_txt = open("allwords.txt", "w")
	for word in novel_all_words:
		all_words_txt.write(word+"\n")
	all_words_txt.close()



def main():
	
	inLines = sys.stdin.readlines()
	novel_lower = [entry.lower() for entry in inLines]
	novel_unformatted = [re.findall(r'[a-z]+', line) for line in novel_lower]
	novel_lines = []

	for line in novel_unformatted:
		if line:
			novel_lines.append(line)

	novel_all_words = all_words(novel_lines)
	write_all_words(novel_all_words)
	word_freq_return = word_freq(novel_all_words)
	word_frequency = word_freq_return[0] # not needed?
	word_frequency_frequency = word_freq_return[1]
	write_word_freq(word_frequency_frequency)
	write_unique_words(word_frequency)

if __name__ == "__main__":
  main()
