from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


# users/views.py


def index(request):
    # 示例新闻数据
    news_data = [
        {"title": "【卓越发展】大连理工大学2025届毕业生秋季双选会举办", "img": "https://news.dlut.edu.cn/__local/3/12/24/2B68BD4FAEF70CEE866EA957DEF_F1487DBE_77F85.jpg",
            "link": "https://news.dlut.edu.cn/info/1011/106594.htm"},
        {"title": "【科技日报】贾振元：探索高校科技创新工作新路径", "img": "https://news.dlut.edu.cn/__local/C/76/0C/80E2CE75E0C3808E34C2BD71FE5_D5FF7028_88B9E.jpg",
            "link": "https://news.dlut.edu.cn/info/1011/106244.htm"},
        {"title": "【光明日报】校地合作共赴振兴的故事", "img": "https://news.dlut.edu.cn/__local/7/01/33/FB5A2D07E989AA4316E77DF64BB_EF678744_5A251.jpg",
            "link": "https://news.dlut.edu.cn/info/1011/106474.htm"}
    ]

    return render(request, 'users/index.html', {'news_data': news_data})
