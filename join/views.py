import json

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from django.views import View

from join.models import Zipcode, Member


class JoinmeView(View):
    def get(self, request):
        return render(request, 'join/joinme.html')

    def post(self, request):

        form = request.POST.dict()

        email = form['email1'] + '@' + form['email2']

        m = Member(userid=form['userid'],
                   passwd=form['passwd'],
                   name=form['name'],
                   phone=form['phone'],
                   # zip=Zipcode.objects.get(seq=zip.seq),
                   zip=Zipcode.objects.get(seq=form['seq']),
                   addr=form['addr2'],
                   email=email)
        m.save()

        return redirect('/join/joinok?userid=' + form['userid'])

class JoinokView(View):
    def get(self, request):
        # join/joinok?userid=***
        form = request.GET.dict()

        # select * from member join zipcode on m.zipcode = z.seq
        # where m.userid = ****
        m = Member.objects.select_related().get(userid=form['userid'])
        context ={'member':m}
        return render(request, 'join/joinok.html',context)

    def post(self, request):

        pass


class AgreeView(View):
    def get(self, request):
        return render(request, 'join/agree.html')

    def post(self, request):
        pass



class ZipcodeView(View):
    def get(self, request):
        form = request.GET.dict()

        # select * from zipcode where dong = '동이름';
        # 테이블모델명.objects.get(조건) : 1개의 결과값만 처리
        # result = Zipcode.objects.get(dong='사당동')
        # print(result.values())

        # 테이블모델명.objects.filter(조건) : 1개이상 결과값 처리
        result = Zipcode.objects.filter(dong=form['dong'])
        # print(result.values())

        # 조회결과를 JSON객체로 생성
        json_data = serializers.serialize('json', result)
        # print(json_data, form['dong'])

        # 생성된 JSON객체를 HTTP 응답객체로 전송
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request):
        pass


class UseridView(View):
    def get(self, request):
        #/join/userid?userid=***
        #응답 메세지 =>{'result':0또는 1}
        form = request.GET.dict()


        #select*from member where userid = ?
        count = Member.objects.filter(userid=form['userid']).count()
        # print(count)

        # 조회된 카운트를 json형식의 데이터로 생성
        # json_data ={}
        # json_data['count']=count
        json_data ={'count':count}
        #print(json_data)




        # 생성된 json데이터를 직렬화함 - 지원안됨(직렬화시 정보부족)
        #json_data = serializers.serialize('json', json_data)

       #카운트는 json.dumps함수로 간단하게 문자열로 직렬화
        return HttpResponse(json.dumps(json_data), content_type='application/json')


        # return render(request, 'join/agree.html')

    def post(self, request):
        pass