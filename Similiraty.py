from base64 import decode
import json
from urllib import response
import numpy as np
from sentence_transformers import SentenceTransformer
import requests

tosend = []
sbert_model = SentenceTransformer('bert-base-nli-mean-tokens')


def cosine(u, v):
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))


def similiraty(tag):
    response = requests.get(
        "https://smartification.glitch.me/select_all_tags")
    sentences = json.loads(response.text)
    print(sentences)
    tosend = []
    desc = sbert_model.encode([tag])[0]
    bestSim = -1
    bestRes = ''
    bestRes2 = ''
    for sent in sentences:
        if bestRes == sent['tag']:
            continue
        if bestRes2 == sent['tag']:
            continue
        sim = cosine(desc, sbert_model.encode([sent['tag']])[0])
        if sim > bestSim:
            bestRes = sent['tag']
            bestSim = sim
            continue
    if(bestSim < 0.85):
        bestRes = tag
    # guardar as tags com mais de 85%
    print("Input: " + tag)
    print("Similiraty level: ")
    print(bestSim)
    print("Best Match:" + bestRes)
    res = bestRes.rstrip()
    tosend.append(res)
    tosend.append(bestSim)
    return tosend
