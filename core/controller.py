from fastapi import FastAPI
from cachetools import cached, TTLCache
from core.ml import RelatedTags


app = FastAPI()
rt = RelatedTags("./core/model/tagmodel.model")


@app.get("/")
def root():
    return 200


@app.get("/health")
@app.head("/health")
def health():
    return "We're up and running!"


@app.get("/similar_tags/{tag}")
@cached(cache=TTLCache(maxsize=100000, ttl=3600))
def get_similar_tags(tag: str, threshold: float = 0.99, k: int = 10):
    return rt.get_similar_tags(tag.lower().strip(), threshold, k)
