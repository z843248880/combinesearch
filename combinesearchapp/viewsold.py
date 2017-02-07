from django.shortcuts import render

# Create your views here.

from combinesearchapp import models

def video(request,**kwargs):
    direction_id = kwargs.get('direction_id', '0')
    classfication_id = kwargs.get('classfication_id', '0')
    current_url = request.path_info
    q = {}
    if direction_id == '0':
        if classfication_id == '0':
            CList = models.Classification.objects.values('id', 'name')
        else:
            q['classification__id'] = classfication_id
            CList = models.Classification.objects.values('id', 'name')
    else:
        obj = models.Direction.objects.get(id=direction_id)
        temp = obj.classification.all().values('id', 'name')
        id_list = list(map(lambda x: x['id'], temp))
        CList = temp
        if classfication_id == '0':
            q['classification__id__in'] = id_list
        else:
            print('cc:',classfication_id,id_list)
            if int(classfication_id) in id_list:
                q['classification__id'] = classfication_id
            else:
                q['classification__id__in'] = id_list
                url_list = current_url.split('-')
                url_list[2] = "0"
                current_url = '-'.join(url_list)
                print(current_url)
            print('curl:',current_url)

    level_id = kwargs.get('level_id', None)
    if level_id != '0':
        q['level'] = level_id

    result = models.Video.objects.filter(**q)
    print(result)




    DList = models.Direction.objects.values('id','name')
    VList = models.Video.level_choice
    return render(request,'video.html',{'DList':DList,'CList':CList,'VList':VList,'current_url':current_url})
