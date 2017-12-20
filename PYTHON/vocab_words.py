# learning new vocab with Python3


# Interesting Word List
vocab_list = ["gerontocracy","connote","inquest","moribund","poseur","ossified"]
learned_vocab = []

def learning_vocab(unlearned, learned):
	while unlearned:
		current_word = unlearned.pop()
		print("Learning Vocab: " + current_word)
		learned.append(current_word)

#TODO 
def show_unlearned_vocab(vocab_list):
	"""hopfully does not change the original list"""
	print("\nThe following models have been printed:")
	for vocab in vocab_list:
		print(vocab)

def show_learned_vocab(vocab_list):
	"""displays the list that is passed in"""
	print("\nThe following models have been printed:")
	for vocab in vocab_list:
		print(vocab)


learning_vocab(vocab_list[:], learned_vocab) # this is stable
show_learned_vocab(learned_vocab)
show_learned_vocab(vocab_list)

learning_vocab(vocab_list, learned_vocab) # this modifies the code/unstable
show_learned_vocab(learned_vocab) # should double up
show_learned_vocab(vocab_list)

