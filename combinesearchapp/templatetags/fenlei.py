from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag()
def actionone(current_url,nid,name):
    sp_url = current_url.split('-')
    old = sp_url[1]
    if old == str(nid):
        temp = '<a class="active" href="%s">%s</a>'
    else:
        temp = '<a href="%s">%s</a>'
    sp_url[1] = str(nid)
    tp = '-'.join(sp_url)
    tag = temp % (tp,name)
    return mark_safe(tag)


@register.simple_tag()
def actiontwo(current_url,nid,name):
    sp_url = current_url.split('-')
    old = sp_url[2]
    if old == str(nid):
        temp = '<a class="active" href="%s">%s</a>'
    else:
        temp = '<a href="%s">%s</a>'
    print('url,old,nid:', current_url,old, nid)
    sp_url[2] = str(nid)
    tp = '-'.join(sp_url)
    tag = temp % (tp,name)
    print('old,nid:',old,nid)
    return mark_safe(tag)


@register.simple_tag()
def actionthree(current_url,nid,name):
    sp_url = current_url.split('-')
    old = sp_url[3].strip('/')

    if old == str(nid):
        temp = '<a class="active" href="%s">%s</a>'
    else:
        temp = '<a href="%s">%s</a>'
    sp_url[3] = str(nid)
    tp = '-'.join(sp_url)
    tag = temp % (tp,name)
    return mark_safe(tag)

@register.simple_tag()
def all(current_url,id):
    sp_url = current_url.split('-')
    if int(id) == 3:
        sp_url[3] = sp_url[3].strip('/')
    if sp_url[id] == '0':
        temp = '<a class="active" href="%s">全部</a>'
    else:
        temp = '<a href="%s">全部</a>'
    sp_url[id] = '0'
    tp = '-'.join(sp_url)
    tag = temp % (tp)
    return mark_safe(tag)