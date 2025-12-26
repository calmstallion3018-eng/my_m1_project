from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'title': 'M-1決勝ネタ 文字起こし'}
    return render(request, 'myapp/index.html', context)

def yarlens(request):
    context = {'title': 'ヤーレンズ　「結婚」'}
    return render(request, 'myapp/yarlens.html', context)

def mezon(request):
    context = {'title': 'めぞん　「女友達」'}
    return render(request, 'myapp/mezon.html', context)

def kanamestone(request):
    context = {'title': 'カナメストーン　「ダーツの旅」'}
    return render(request, 'myapp/kanamestone.html', context)

def evers1(request):
    context = {'title': 'エバース　1本目　「ドライブデート」'}
    return render(request, 'myapp/evers1.html', context)

def shinkujessica(request):
    context = {'title': '真空ジェシカ　「ペーパードライバー講習」'}
    return render(request, 'myapp/shinkujessica.html', context)

def yoneda2000(request):
    context = {'title': 'ヨネダ2000　「バスケットボール」'}
    return render(request, 'myapp/yoneda2000.html', context)

def takuro1(request):
    context = {'title': 'たくろう　1本目　「バスケットボール」'}
    return render(request, 'myapp/takuro1.html', context)

def dondecollete1(request):
    context = {'title': 'ドンデコルテ　1本目　「デジタルデトックス」'}
    return render(request, 'myapp/dondecollete1.html', context)

def gokaicaptain(request):
    context = {'title': '豪快キャプテン　「小さいカバン」'}
    return render(request, 'myapp/gokaicaptain.html', context)

def mamatarte(request):
    context = {'title': 'ママタルト　「初詣」'}
    return render(request, 'myapp/mamatarte.html', context)

def dondecollete2(request):
    context = {'title': 'ドンデコルテ　2本目　「名物おじさん」'}
    return render(request, 'myapp/dondecollete2.html', context)

def evers2(request):
    context = {'title': 'エバース　2本目　「腹話術」'}
    return render(request, 'myapp/evers2.html', context)

def takuro2(request):
    context = {'title': 'たくろう　2本目　「ビバリーヒルズ」'}
    return render(request, 'myapp/takuro2.html', context)