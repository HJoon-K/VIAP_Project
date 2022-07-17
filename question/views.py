from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from join.models import Member
from question.models import Question


class QuestionView(View):
    def get(self, request):

        name = request.session.get('userinfo').split('|')[0]

        # q = Member.objects.get(userid=name)

        context = {'name': name}

        return render(request, 'question/question.html', context)

    def post(self, request):
        form = request.POST.dict()

        q = Question(qname=Member.objects.get(userid=form['qname']), qphone=form['qphone'],
                     qemail=form['qemail'], qselect=form['qselect'],
                     qsubject=form['qsubject'], context=form['qtext'])
        q.save()


        return redirect('/question/questionok?qname=' + form['qname'])

class QuestionokView(View):
    def get(self, request):
        form = request.GET.dict()

        qq = Member.objects.select_related().get(userid=form['qname'])


        context = {'qq':qq}

        return render(request, 'question/questionok.html', context)


