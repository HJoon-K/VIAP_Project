import json
from urllib.parse import urlencode
from django.shortcuts import render, redirect


from django.core import serializers
from django.http import HttpResponse

# Create your views here.
from django.views import View
# from join.models import Member
from community.models import Rboard
from home.models import Sidonggu
from join.models import Member
from question.models import Question


class IntroView(View):
    def get(self, request):
        return render(request,'intro.html')


    def post(self, request):
        pass


class AdminView(View):
    def get(self, request):
        return render(request, 'admin.html')

    def post(self, request):
        pass


# 로그인 처리
class LoginView(View):
     def post(self, request):
        form = request.POST.dict()

        returnPage = '/loginfail'

        from join.models import Member
        isExisted = Member.objects.filter(userid= form['userid'], passwd=form['passwd']).exists();

        if isExisted:

            user =Member.objects.get(userid=form['userid'])
            request.session['userinfo'] =form['userid']+'|'+str(user.id)

            returnPage = '/'
            
        return redirect(returnPage)
    

# 로그아웃 처리
class LogoutView(View):
    def get(self, request):
        #세션변수
        request.session.flush()

        return redirect('/')

    def post(self, request):
        pass

#로그인 실패시 보여줄 페이지 지정
class LoginFailView(View):
    def get(self, request):
        return render(request, 'loginfail.html')


class AdremoveView(View):
    def get(self, request):
        form = request.GET.dict()


        Question.objects.filter(id=form['qname']).delete()

        return redirect('/admin')



class SigunguView(View):
    def get(self, request):
        form = request.GET.dict()
        print('form=',form)
        result = Sidonggu.objects.filter(sido=form['sido']).order_by('-sigungu')
        print(result)

        sigungu1 = result.values_list('sigungu', flat=True).distinct();
        print('sigungu =', sigungu1);

        data = [val for val in sigungu1 if val]

        result = {'sigungu': data}
        print(result)

        return HttpResponse(json.dumps(result), content_type='application/json')
    pass


class HomeView(View):
    def get(self, request):

        sido = Sidonggu.objects.all().order_by('-sido')
        print("sido=", sido);

        sido_d = sido.values_list('sido', flat=True).distinct();
        print('sido_d =', sido_d);

        context = {'sido_d': sido_d}

        return render(request, 'index.html', context)

    def post(self,request):
        form = request.POST.dict();
        print('form=',form);

        sido = Sidonggu.objects.all().order_by('-sido')
        print("sido=", sido);

        sido_d= sido.values_list('sido', flat=True).distinct();
        print('sido_d =',sido_d);


        context = {'sido_d':sido_d}

        return render(request,'index.html', context)

class MypageView(View):
        def get(self, request):
            form = request.session['userinfo'].split('|')[0]
            myinfo = Member.objects.select_related().filter(userid=form)
            context = {'mi': myinfo}

            return render(request, 'mypage.html', context)

        def post(self, request):
            return render(request, 'mypage.html')

class MypageupView(View):
        def get(self, request):
            form = request.session['userinfo'].split('|')[0]
            myinfo = Member.objects.select_related().filter(userid=form)
            context = {'mi': myinfo}

            return render(request, 'mypageup.html', context)

        def post(self, request):
            return render(request, 'mypageup.html')
