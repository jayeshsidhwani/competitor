import pickle, pandas
from nltk.tokenize import sent_tokenize
from tagger import Extractor

class Analyse():

    def __init__(self):
        data = pickle.load(open('company_data_crunchbase.p'))
        self.panda = pandas.DataFrame.from_dict(data.values())
        del self.panda['website']
        del self.panda['category']
        del self.panda['description']
        self.tokens = {}
        self.imp_pos = ['NN', 'JJ']

    def extract_keywords(self):
        phrase_occurrence = {}
        for val in self.panda.values:
            name = val[0]
            print 'Analysing: %s' %name
            try:
                for sent in sent_tokenize(val[1]):
                    phrases = Extractor().extract(sent)
                    for phrase in phrases:
                        if phrase:
                            _p = ' '.join(phrase)
                            freq = phrase_occurrence.get(_p, 0) + 1
                            phrase_occurrence[_p] = freq
            except Exception as e:
                print e.message
                continue

        f = open('frequency_analysis.csv', 'w')
        for word, count in phrase_occurrence.items():
            f.write("%s,%s\n" %(word, count))
        f.close()

if __name__ == '__main__':
    Analyse().extract_keywords()
