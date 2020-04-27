from django import template

register = template.Library()

def get_item(dictionary, key):
    return dictionary.get(key)

def len_dict(dictionary):
    return len(dictionary)
    
register.filter('get_item', get_item)
register.filter('len_dict', len_dict)