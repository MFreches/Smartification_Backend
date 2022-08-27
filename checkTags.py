import json
from regex import R
import requests
from Similiraty import similiraty


def checkTags(resposta):
    tosend = []
    print('Start Check Tags Func')
    for tag in resposta:
        apiUrl = 'https://smartification.glitch.me/select_tag_tags_relations'
        myobj = {'search': tag}
        x = requests.post(apiUrl, json=myobj)
        sentences = json.loads(x.text)
        if len(sentences) == 0:
            # correr a similiaridade
            # adicionar ao vetor de respostas
            sim = similiraty(tag)
            if sim[1] > 0.85:
                apiUrl = 'https://smartification.glitch.me/select_tag'
                myobj = {'tag': sim[0]}
                x = requests.post(apiUrl, json=myobj)
                sentences = json.loads(x.text)
                tag_id = sentences[0]['tag_id']
                apiUrl = 'https://smartification.glitch.me/insert_tags_relations'
                myobj = {'tag_id': tag_id, 'expression': tag}
                x = requests.post(apiUrl, json=myobj)
            tosend.append(sim[0])
        else:
            # ir buscar a tag ao tagging atraves do tag_id
            # adicionar o tag ao vetor de respostas
            apiUrl = 'https://smartification.glitch.me/select_specific_tag'
            tag_id = sentences[0]['tag_id']
            myobj = {'tag_id': tag_id}
            x = requests.post(apiUrl, json=myobj)
            jsonT = json.loads(x.text)
            tag = jsonT[0]['tag']
            tosend.append(tag)
    print('End Check Tags Func\n')
    return tosend
