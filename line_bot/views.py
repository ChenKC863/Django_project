from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings




# 引入 linebot SDK
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage, TextMessage, StickerMessage
from linebot.models.messages

# 建立 linebot classs 進行連線
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


@csrf_exempt
def callback(request):
    if (request.method == "POST"):
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')


        # 嘗試解密event
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
       
        for event in events:
            print(event)
            
            x = ImageSet()
            
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                    res_text = event.message.text
                    
                    
                    print(res_text)
                    if event.message.text == "@我要報到":                     
                        line_bot_api.reply_message(event.reply_token, StickerMessage(package_id=6136, sticker_id = 10551376))
                    elif event.message.text == "@我的名牌":
                        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = res_text))                           
                    elif event.message.text == "@車號登入":
                        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = res_text))
                    else:
                        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = res_text))
        return HttpResponse()
    else:
        return HttpResponseBadRequest()

def sendMsg(requests, uid):
    line_bot_api.push_message(uid, TextSendMessage(text = "Hello"))
    return HttpResponse()

def sendMsg_new(requests, uid):
    line_bot_api.push_message(uid, TextSendMessage(text = "Hello--new"))
    return HttpResponse()

# from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
# # Create your views here.

# # Create your views here.
# #from datetime import datetime
# def callback(request):
#     return HttpResponse()
# # def index(requests):
# #     posts = Post.objects.all()
# #     now = datetime.now() # post.content
# #     return render(requests, "pages/index.html", locals())

# # from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

# # def showPost(requests, slug):
# #     #1.查詢資料庫
# #     try:
# #         post = Post.objects.get(slug=slug) #urlencoding
# #     except ObjectDoesNotExist:
# #         return redirect('/')
# #     except MultipleObjectsReturned:
# #         return redirect('/')
    
# #     return render(requests, 'pages/post.html', locals())
# # from django.http import JsonResponse
# # def testjson(requests):
# #     # QuerySet
# #     posts = list(Post.objects.all().values())
# #     return JsonResponse(posts, status=200, safe=False)