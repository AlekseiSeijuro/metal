from django.shortcuts import render, redirect
from .models import Application, Prices
# Create your views here.
def home(request):
    return render(request, 'main/main_page.html')

def form(request):
    if request.method == 'POST':
        name=request.POST['name']
        phone = request.POST['phone']

        metal_names=['Медь: ', 'Аллюминий: ', 'Латунь: ', 'Олово: ', 'Никель: ', 'Цинк: ', 'Сталь: ', 'Чугун: ', 'Железо: ']

        metals=''

        checks=request.POST.getlist('checks[]')
        for el in checks:
            metals+=metal_names[int(el)]+str(request.POST['met_'+el+'_num'])+'кг\n'

        newApplication=Application.objects.create(name=name, phone_number=phone, product=metals)
        newApplication.save()

        return redirect('success')
    return render(request, 'main/form.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def success(request):
    return render(request, 'main/success.html')

def prices(request):
    prices=Prices.objects.all()

    data={
        'prices': prices
    }

    #for elem in prices:
      #  data[elem.metal]=elem.price

    return render(request, 'main/prices.html', data)

def cards(request):
    cards=[['МАТЕРИНСКАЯ ПЛАТА НОВАЯ','main/img/cards/mtnew.jpg'],
           ['МАТЕРИНСКАЯ ПЛАТА СТАРАЯ', 'main/img/cards/mtold.jpg'],
           ['ПЛАТЫ БЫТОВЫЕ И ПЛАТЫ СССР', 'main/img/cards/sssr.jpg'],
           ['СЕТЕВЫЕ, ЗВУКОВЫЕ', 'main/img/cards/sound.jpg'],
           ['ПЛАТА СЕРВЕРА', 'main/img/cards/serv.jpg'],
           ['ПЛАТЫ CD-ROM', 'main/img/cards/cdrom.jpg'],
           ['МОНИТОРНАЯ ПЛАТА', 'main/img/cards/mon.jpg'],
           ['ПЛАТЫ СЕРИИ 155 НАПОЛНЕНИЕ 40%', 'main/img/cards/155.jpg'],
           ['ВИДЕОКАРТА', 'main/img/cards/video.jpg'],
           ['ОПЕРАТИВНАЯ ПАМЯТЬ С ЖЕЛТОЙ ЛАМЕЛЬЮ', 'main/img/cards/op.jpeg'],
           ['ПЛАТА ЖЕСТКОГО ДИСКА', 'main/img/cards/disk.jpg'],
           ['ПЛАТА GSM', 'main/img/cards/jsm.jpg'],
           ['ПЛАТА МОБИЛЬНОГО ТЕЛЕФОНА КНОПКА', 'main/img/cards/phone.jpg'],
           ['ПЛАТА СМАРТФОНОВ И ПЛАНШЕТОВ', 'main/img/cards/smartphone.jpg'],
           ['ПЛАТА ОТ НОУТБУКА', 'main/img/cards/nout.jpg'],
           ['ПЛАТЫ УПРАВЛЕНИЯ 1.3-', 'main/img/cards/1.3-.jpg'],
           ['ПЛАТЫ УПРАВЛЕНИЯ 1.3+', 'main/img/cards/1.3+.png'],
           ['СРЕЗКА С ПЛАТ', 'main/img/cards/srez.png'],
           ['ОРГТЕХНИКА', 'main/img/cards/org.jpg'],
           ['AHTEHНA GSM В СБОРЕ', 'main/img/cards/antena.jpg'],
           ['МОБИЛЬНЫЕ ТЕЛЕФОНЫ В СБОРЕ', 'main/img/cards/phonesbor.jpg'],
           ['POS ТЕРМИНАЛ В СБОРЕ', 'main/img/cards/pos.jpg'],
           ['КЕРАМИЧЕСКИЙ ПРОЦЕССОР', 'main/img/cards/kproc.jpg'],
           ['ПРОЦЕССОР С ЭЛЕМЕНТОМ ОХЛАЖДЕНИЯ', 'main/img/cards/coldproc.jpg'],
           ]
    data={
        'cards': cards
    }

    return render(request,'main/cards.html', data)