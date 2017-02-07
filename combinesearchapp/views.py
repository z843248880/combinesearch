from django.shortcuts import render

# Create your views here.

from combinesearchapp import models


# **kwargs，获取到url的值。
def video(request, **kwargs):
    # 方向id，默认是0
    direction_id = kwargs.get('direction_id', '0')

    # 分类id，默认是0
    classfication_id = kwargs.get('classfication_id', '0')

    # 当前url值
    current_url = request.path_info


# 如果方向id是0，也就是用户没有选择方向，则默认就将所有的分类（python、linux、openstatck、javascripts）显示
    if direction_id == '0':
        CList = models.Classification.objects.values('id', 'name')
    else:
        # 方向id不是0，则获取到用户选择的方向（比如是测试）的id对应的表对象
        obj = models.Direction.objects.get(id=direction_id)
        # 获取这个方向下的所有分类的id和name，因为测试这个方向下只有python一个分类，所以此处的temp是（1，‘python’）
        temp = obj.classification.all().values('id', 'name')
        # 获取该方向下的所有分类的id值
        id_list = list(map(lambda x: x['id'], temp))

        # 因为用户选择了方向，所以将这个方向下对应的分类显示，假如用户选择的“测试”，则此时页面的分类那一行只显示“python”，而不显示linux、openstack、javascript
        CList = temp

        if classfication_id != '0':
            if int(classfication_id) not in id_list:
                url_list = current_url.split('-')
                url_list[2] = "0"
                current_url = '-'.join(url_list)
                print(current_url)

    DList = models.Direction.objects.values('id', 'name')
    VList = models.Video.level_choice
    return render(request, 'video.html', {'DList': DList, 'CList': CList, 'VList': VList, 'current_url': current_url})
