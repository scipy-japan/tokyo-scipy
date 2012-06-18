# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <markdowncell>

# # Kan.Scipy #1
# 
# Welcome to Kan.Scipy #1!
# 
# ## Introducing NLTK
# 
# ### First, some imports:

# <codecell>

import nltk
import MeCab
from nltk import Tree
from nltk.corpus import brown, gutenberg, treebank
from nltk.tokenize.api import TokenizerI

# <markdowncell>

# ### Corpora
# 
# NLTK has several built-in corpora and resources

# <codecell>

treebank.sents()

# <codecell>

nltk.download('treebank')

# <codecell>

print treebank.parsed_sents()[0]

# <markdowncell>

# NLTK's CorpusReader classes manage files:

# <codecell>

print brown.abspaths()[:5]

# <markdowncell>

# 
# ### Tokenization
# 
# NLTK has a built-in tokenizer for English:

# <codecell>

text = 'The quick brown fox jumped over the lazy dog.'
nltk.word_tokenize(text)

# <markdowncell>

# #### For Japanese:
# 
# You can call MeCab from Python:

# <codecell>

jtext = u'すばしっこい茶色の狐が怠け者の犬の上を飛んでいったとさ。'
mecab = MeCab.Tagger()
print mecab.parse(jtext.encode('euc-jp')).decode('euc-jp')

# <markdowncell>

# Or define a new NLTK tokenizer using MeCab: (code copied from `https://mhagiwara.googlecode.com/svn/trunk/nltk/jpbook/jptokenizer.py` )

# <codecell>

class JPMeCabTokenizer(TokenizerI):
    def __init__(self):
        import MeCab
        self.mecab = MeCab.Tagger('-Owakati')

    def tokenize(self, text):
        result = self.mecab.parse(text.encode('euc-jp'))
        return result.decode('euc-jp').strip().split(' ')

print JPMeCabTokenizer().tokenize(jtext)
print u' '.join(JPMeCabTokenizer().tokenize(jtext))

# <markdowncell>

# ### Ngram Language Models
# 
# NLTK provides functionality to build n-gram language models.
# 
# A language model is a probabilistic model of language that allows
# us to measure how likely a given sequence of words is.
# 
# An n-gram is a sequence of n words; we count n-grams in a text and
# calculate a conditional probability distribution like:
# 
# $$
# P(X_i|X_{i-1},..,X_{i-n+1})
# $$

# <codecell>

from nltk.model.ngram import NgramModel
from nltk.probability import WittenBellProbDist, LidstoneProbDist

train_words = brown.words()[:-500]
test_words = brown.words()[-500:]
lm = NgramModel(2, train_words, lambda fd, b: LidstoneProbDist(fd, 0.2))

# <codecell>

lm.entropy(test_words)

# <markdowncell>

# ### Counting
# 
# For example, how many words in a corpus are not in WordNet?

# <codecell>

from nltk.corpus import wordnet
from nltk.probability import ConditionalFreqDist

cfd = ConditionalFreqDist(
      (pos, len(wordnet.synsets(word)) > 0) for word,pos in treebank.tagged_words()
)

cfd.tabulate()

# <markdowncell>

# ### Missing functionality
# 
# #### Head word identification
# 
# NLTK has no functionality to identify the head words of phrases. In this noun phrase, 'man' is the head word,
# but it is not straightforward to identify it.

# <codecell>

np = Tree('(NP (D The) (N man) (PP (P with) (NP (D a) (N gun))))')
np.draw()

# <markdowncell>

# # Last words:
# 
# ## A tip
# 
# Did you know you can add arbitrary attributes to an object instance?

# <codecell>

class MyClass: pass

mc = MyClass()

mc.foo = 'bar'

print mc.foo

# <markdowncell>

# This is useful for dynamic programming, but how do you test for presence/abscence?

# <codecell>

print mc.baz is None

# <codecell>

print hasattr(mc, 'baz')

# <markdowncell>

# But `hasattr` is controversial and may disappear

# <codecell>

try:
    print mc.baz is None
except AttributeError:
    pass

# <codecell>

def tryattr(obj, attr, default=None):
    try:
        return getattr(obj, attr)
    except AttributeError:
        return default

print tryattr(mc, 'baz')
print tryattr(mc, 'foo')

