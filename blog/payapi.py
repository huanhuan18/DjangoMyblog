from bs4 import BeautifulStoneSoup
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

from alipay.aop.api.AlipayClientConfig import AlipayClientConfig   # 客户端配置类
from alipay.aop.api.DefaultAlipayClient import DefaultAlipayClient   # 默认客户端类
from alipay.aop.api.domain.SettleDetailInfo import SettleDetailInfo   
from alipay.aop.api.domain.AlipayTradePagePayModel import AlipayTradePagePayModel  # 网站支付数据模型类
from alipay.aop.api.request.AlipayTradePagePayRequest import AlipayTradePagePayRequest  # 网站支付请求类
from alipay.aop.api.util.SignatureUtils import verify_with_rsa

from blog.models import Article, PayOrder
from rest_framework.response import Response
from rest_framework.decorators import api_view
import datetime
import random

@api_view(['POST'])
def getAlipayUrl(request):
    token = request.POST['token']

    user_token = Token.objects.filter(key=token)
    if len(user_token)==0:
        return Response('nologin')
    user = user_token[0].user
    article_id = request.POST['article_id']
    article = Article.objects.get(id=article_id)

    nowtime = datetime.datetime.now()
    new_payorder = PayOrder(belong_user=user,belong=article)
    new_payorder.order = str(nowtime.year) + str(random.randrange(10000000,99999999))
    # print(new_payorder.order)
    new_payorder.price = '9.9'

    alipay_client_config = AlipayClientConfig()
    alipay_client_config.server_url = 'https://openapi.alipay.com/gateway.do'
    alipay_client_config.app_id = '[your app_id]'
    alipay_client_config.app_private_key = '[your app private key]'
    alipay_client_config.alipay_public_key = '[alipay public key]'

    pay_link = "https://www.alipay.com/"
    return Response({'pay_link':pay_link})