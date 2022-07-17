from math import ceil

from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from community.models import Rboard
from join.models import Member
from urllib.parse import urlencode

from question.models import Question


class Admin_memberView(View):
    def get(self, request, perPage=10):
        form = request.GET.dict()
        qry = ''


        if request.GET.get('findid') is not None:
            minfo = Member.objects.select_related().filter(userid=form['findid'])
            qry = urlencode({'findid': form['findid']})
        else:
            minfo = Member.objects.select_related()


        pages = ceil(minfo.count() / perPage)
        mempage = 1
        if request.GET.get('mempage') is not None: mempage = form['mempage']

        start = (int(mempage) - 1) * perPage
        end = start + perPage

        minfo = minfo[start:end]

        stpgn = int((int(mempage) - 1) / 10) * 10 + 1

        context = {'mds': minfo, 'qry':qry, 'pages':pages, 'range': range(stpgn, stpgn + 10)}
        return render(request,'admin/admin_member.html', context)

class Admin_reviewView(View):
    def get(self, request, perPage=10):
        form = request.GET.dict()
        qry = ''

        if request.GET.get('findid2') is not None:
            reinfo = Rboard.objects.select_related().filter(name__userid=form['findid2'])
            qry = urlencode({'findid2': form['findid2']})
        else:
            reinfo = Rboard.objects.select_related()

        pages = ceil(reinfo.count() / perPage)
        repage = 1
        if request.GET.get('repage') is not None: repage = form['repage']

        start = (int(repage) - 1) * perPage
        end = start + perPage

        reinfo = reinfo[start:end]

        stpgn = int((int(repage) - 1) / 10) * 10 + 1

        context = {'rds':reinfo, 'qry':qry, 'pages':pages, 'range': range(stpgn, stpgn + 10)}
        return render(request, 'admin/admin_review.html', context)

    def post(self, request):
        form = request.POST.getlist('delck')
        print(form)
        for i in form:
           aa = Rboard.objects.filter(id=int(i)).delete()

        context = {'aa':aa}

        return render(request, 'admin.html', context)

class Admin_questionView(View):
    def get(self, request, perPage=10):
        form = request.GET.dict()
        qry = ''

        if request.GET.get('findid3') is not None:
            quinfo = Question.objects.select_related().filter(qname__userid=form['findid3'])
            qry = urlencode({'findid3': form['findid3']})
        else:
            quinfo = Question.objects.select_related()

        pages = ceil(quinfo.count() / perPage)
        qupage = 1
        if request.GET.get('qupage') is not None: qupage = form['qupage']

        start = (int(qupage) - 1) * perPage
        end = start + perPage

        quinfo = quinfo[start:end]

        stpgn = int((int(qupage) - 1) / 10) * 10 + 1


        context = {'qds': quinfo, 'qry': qry, 'pages':pages, 'range': range(stpgn, stpgn + 10)}
        return render(request, 'admin/admin_question.html', context)

    def post(self, request):
        form = request.POST.getlist('delck')

        for i in form:
           aa = Question.objects.filter(id=int(i)).delete()
        context = {'aa':aa}
        return render(request, 'admin.html', context)






