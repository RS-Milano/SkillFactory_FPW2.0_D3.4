from django import template
 
register = template.Library()

obscene_words = ["shit", "crap", "fuck", "damn", "nigger", "whore", "slut", "bitch", "faggot"]

@register.filter(name='censor')
def censor(value):
    words_list = value.split()
    for index, word in enumerate(words_list):
        if word.lower() in obscene_words:
            words_list[index] = "<...>"
    return " ".join(words_list)
