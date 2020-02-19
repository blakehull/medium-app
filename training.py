from core.ml import RelatedTags

RelatedTags().train("data/tags.txt", 150, 3, 1, "./core/model/tagmodel.model")
