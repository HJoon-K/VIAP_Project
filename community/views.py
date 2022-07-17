from django.shortcuts import render, redirect
from django.views import View
from urllib.parse import urlencode
from math import ceil
# Create your views here.
from community.models import Rboard, Info
from join.models import Member


class FaqView(View):
    def get(self, request):
        return render(request, 'community/faq.html')

    def post(self, request):
        pass


class InfoView(View):
    def get(self, request):
        form = request.GET.dict()
        infolist = Info.objects.select_related()

        context = {'Info_list': infolist}
        return render(request, 'community/information.html', context)

class ReviewView(View):
    def get(self, request, perPage=10):
        form = request.GET.dict()
        qry = ''

        review = Rboard.objects.select_related()

        pages = ceil(review.count() / perPage)

        rpage = 1
        if request.GET.get('rpage') is not None: rpage = form['rpage']

        start = (int(rpage) - 1) * perPage
        end = start + perPage

        review = review[start:end]

        stpgn = int((int(rpage) - 1) / 10) * 10 + 1
        jum = Rboard.objects.count()
        workjum5 = Rboard.objects.filter(workjum='5').count()
        workjum4 = Rboard.objects.filter(workjum='4').count()
        workjum3 = Rboard.objects.filter(workjum='3').count()
        workjum2 = Rboard.objects.filter(workjum='2').count()
        workjum1 = Rboard.objects.filter(workjum='1').count()
        workjump5 = round((workjum5 / jum) * 100)
        workjump4 = round((workjum4 / jum) * 100)
        workjump3 = round((workjum3 / jum) * 100)
        workjump2 = round((workjum2 / jum) * 100)
        workjump1 = round((workjum1 / jum) * 100)
        supjum5 = Rboard.objects.filter(supjum='5').count()
        supjum4 = Rboard.objects.filter(supjum='4').count()
        supjum3 = Rboard.objects.filter(supjum='3').count()
        supjum2 = Rboard.objects.filter(supjum='2').count()
        supjum1 = Rboard.objects.filter(supjum='1').count()
        supjump5 = round((supjum5 / jum) * 100)
        supjump4 = round((supjum4 / jum) * 100)
        supjump3 = round((supjum3 / jum) * 100)
        supjump2 = round((supjum2 / jum) * 100)
        supjump1 = round((supjum1 / jum) * 100)
        context = {'bds': review, 'pages': pages, 'range': range(stpgn, stpgn + 10), 'qry': qry, 'workjum5': workjum5,
                   'workjum4': workjum4, 'workjum3': workjum3, 'workjum2': workjum2, 'workjum1': workjum1,
                   'workjump5': workjump5, 'workjump4': workjump4, 'workjump3': workjump3, 'workjump2': workjump2, 'workjump1': workjump1,
                   'supjum5': supjum5, 'supjum4': supjum4, 'supjum3': supjum3, 'supjum2': supjum2, 'supjum1': supjum1,
                   'supjump5': supjump5, 'supjump4': supjump4, 'supjump3': supjump3, 'supjump2': supjump2, 'supjump1': supjump1}

        return render(request, 'community/review.html', context)

    def post(self, request):
        pass

class Review_writeView(View):
    def get(self, request):

        name = request.session.get('userinfo').split('|')[0]

        context = {'name': name}
        return render(request, 'community/review_write.html', context)

    def post(self, request):
        form = request.POST.dict()

        q = Rboard(workjum=form['workjum'],
                   supjum=form['supjum'],
                   name=Member.objects.get(userid=form['name']),
                   contents=form['contents'])
        q.save()

        return redirect('/community/review/?rpage=1&')

class AboutUsView(View):
    def get(self, request):
        return render(request, 'community/about_us.html')

    def post(self, request):
        pass