import gensim
import gensim.models
import warnings
from gensim.similarities.index import AnnoyIndexer as indexer

warnings.simplefilter(action='ignore', category=FutureWarning)


def split(line): return line.split("|")


class RelatedTags:

    def __init__(self, model_path=None):
        self.threshold = 0
        self.watcher = 0
        self.model_path = model_path
        if model_path is not None:
            self.model = gensim.models.Word2Vec.load(self.model_path)
            self.indexer = indexer(self.model, 15)

    def train(self, input_file, s, w, m, output_file="default.model"):
        # trains the word2vec model
        print("loading data...\n")
        with open(input_file) as file:
            documents = list(map(split, file.read().splitlines()))
        print("tag data parsed, training model...\n")
        model_run = gensim.models.Word2Vec(sentences=documents, size=s, window=w, min_count=m, workers=20, sg=1)
        model_run.save(output_file)
        print(f"model saved to {output_file}!")

    def vocab_size(self):
        if self.model_path is not None:
            model = self.model
            print(model.corpus_total_words)
            print(len(model.wv.vocab.keys()))
        else:
            raise Exception("You need a model to get vocab size")

    def create_tag(self, tag):
        return {"tag": tag[0]}

    def cutoffs(self, score):
        return score[1] < self.threshold

    def get_similar_tags(self, t, similarity_threshold, how_many):
        if self.model_path is not None:
            self.threshold = similarity_threshold
            try:
                value = self.model.wv.most_similar(t, topn=2500, indexer=self.indexer, restrict_vocab=300)
                to_craft = list(filter(self.cutoffs, value))[:how_many]
                return {'original': t, 'similar': list(map(self.create_tag, to_craft))}
            except:
                return {'original': t, 'similar': ""}
        else:
            raise Exception("You need a model to find similar tags")

    def search(self, similarity_threshold, how_many):
        if self.model_path is not None:
            print("type \"exit\" to quit program\n")
            print(f"initializing for {how_many} tags returned with similarity score less than {similarity_threshold}\n")
            t = ""
            self.threshold = similarity_threshold
            while t != 'exit':
                t = input("input tag:").lower().strip()
                try:
                    value = self.model.wv.most_similar(t, topn=2500, indexer=self.indexer, restrict_vocab=300)
                    to_craft = list(filter(self.cutoffs, value))[:how_many]
                    print({'original': t, 'similar': list(map(self.create_tag, to_craft))})
                except:
                    print({'original': t, 'similar': []})
        else:
            raise Exception("You need a model to find similar tags")