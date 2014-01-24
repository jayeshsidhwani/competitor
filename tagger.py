import nltk, os, code
from nltk.corpus import stopwords

nltk.data.path = [os.path.expanduser('~') + "/.shopsense/data_files/node/store/data/nltk_data/"]

# text = """The Buddha, the Godhead, resides quite as comfortably in the circuits of a digital
# computer or the gears of a cycle transmission as he does at the top of a mountain
# or in the petals of a flower. To think otherwise is to demean the Buddha...which is
# to demean oneself."""

class Extractor():

    def __init__(self):
        self.stopwords = stopwords.words('english')
        self.lemmatizer = nltk.WordNetLemmatizer()
        self.stemmer = nltk.stem.porter.PorterStemmer()
        self.sentence_re = r'''(?x)      # set flag to allow verbose regexps
              ([A-Z])(\.[A-Z])+\.?  # abbreviations, e.g. U.S.A.
            | \w+(-\w+)*            # words with optional internal hyphens
            | \$?\d+(\.\d+)?%?      # currency and percentages, e.g. $12.40, 82%
            | \.\.\.                # ellipsis
            | [][.,;"'?():-_`]      # these are separate tokens
        '''

        self.grammar = r"""
            NBAR:
                {<NN.*|JJ>*<NN.*>}  # Nouns and Adjectives, terminated with Nouns

            NP:
                {<NBAR>}
                {<NBAR><IN><NBAR>}  # Above, connected with in/of/etc...
        """
        self.chunker = nltk.RegexpParser(self.grammar)


    def extract(self, text):
        self.toks = nltk.regexp_tokenize(text, self.sentence_re)
        self.postoks = nltk.tag.pos_tag(self.toks)
        self.tree = self.chunker.parse(self.postoks)
        return self.get_terms(self.tree)

        # for term in terms:
        #     for word in term:
        #         print word,
        #     print


    def leaves(self, tree):
        """Finds NP (nounphrase) leaf nodes of a chunk tree."""
        for subtree in tree.subtrees(filter = lambda t: t.node=='NP'):
            yield subtree.leaves()

    def normalise(self, word):
        """Normalises words to lowercase and stems and lemmatizes it."""
        word = word.lower()
        # word = self.stemmer.stem_word(word)
        # word = self.lemmatizer.lemmatize(word)
        return word

    def acceptable_word(self, word):
        """Checks conditions for acceptable word: length, stopword."""
        accepted = bool(2 <= len(word) <= 40
            and word.lower() not in self.stopwords)
        return accepted


    def get_terms(self, tree):
        for leaf in self.leaves(tree):
            term = [ self.normalise(w) for w,t in leaf if self.acceptable_word(w) ]
            yield term
