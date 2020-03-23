from django.shortcuts import render
from nltk.corpus import wordnet as wn

def index(request):
    return render(request, 'dict/index.html')

def meaning(request):
    '''
    process the words result and pass meaning as context to template
    '''
    meanings = []
    if request.method == 'GET':
        if 'word' in request.GET:
            word = request.GET['word']
            if wn.synsets(word):
                #word exists
                syns = wn.synsets(word)

                # create a empty list
                words, types, definitions, examples = ([] for _ in range(4)) 

                for syn in syns:
                    #append to respective lists
                    words.append(syn.name().split('.')[0].replace('_', ' '))
                    types.append(syn.lexname().split('.')[0])
                    definitions.append(syn.definition().capitalize() + '.')
                    examples.append(syn.examples())

                
                meanings = [{'word': t[0], 'type': t[1], 
                            'definition': t[2], 'example': t[3]} 
                            for t in zip(words, types, definitions, examples)]
                            
    context = {
        'q': word,
        'meanings': meanings,
    }
    
            
    return render(request, 'dict/meaning.html', context)
