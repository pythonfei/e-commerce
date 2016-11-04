# coding=utf-8
from django.shortcuts import render
from django.http import *
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from models import *
from .decrator import *
# Create your views here.

@view_name
def index(request,dic):
	goods_list = Goods_list.objects.all()

	fruit = goods_list[0]
	count = fruit.goods_info_set.count()
	num = count - 4
	fruit_four = fruit.goods_info_set.filter(id__gte=num)
	fruit_show = fruit.goods_info_set.all()[1:4]

	seafood = goods_list[1]
	count = seafood.goods_info_set.count()
	num = count - 4
	seafood_four = seafood.goods_info_set.filter(id__gte=num)
	seafood_show = seafood.goods_info_set.all()[1:4]

	meet = goods_list[2]
	count = meet.goods_info_set.count()
	num = count - 4
	meet_four = meet.goods_info_set.filter(id__gte=num)
	meet_show = meet.goods_info_set.all()[1:4]

	egg = goods_list[3]
	count = egg.goods_info_set.count()
	num = count - 4
	egg_four = egg.goods_info_set.filter(id__gte=num)
	egg_show = egg.goods_info_set.all()[1:4]

	vegetables = goods_list[4]
	count = vegetables.goods_info_set.count()
	num = count - 4
	vegetables_four = vegetables.goods_info_set.filter(id__gte=num)
	vegetables_show = vegetables.goods_info_set.all()[1:4]

	ice = goods_list[5]
	count = ice.goods_info_set.count()
	num = count - 4
	ice_four = ice.goods_info_set.filter(id__gte=num)
	ice_show = ice.goods_info_set.all()[1:4]

	request.session['uname']='张三'
	uname = request.session['uname']
	
	#将购物车里的所有商品数量显示
	cart = Cart.objects.all()
	goods_count = 0
	for cart_one in cart:
		goods_count += cart_one.goods_num
	dic['goods_count'] = goods_count
	#商品分类列表
	dic['goods_list'] = goods_list
	dic['fruit_four']=fruit_four
	dic['fruit_show']=fruit_show
	dic['fruit']=fruit
	dic['seafood_four']=seafood_four
	dic['seafood_show']=seafood_show
	dic['seafood']=seafood
	dic['meet_four']=meet_four
	dic['meet_show']=meet_show
	dic['seafood']=seafood
	dic['meet_four']=meet_four
	dic['meet_show']=meet_show
	dic['meet']=meet
	dic['egg']=egg
	dic['vegetables_four']=vegetables_four
	dic['vegetables_show']=vegetables_show
	dic['vegetables']=vegetables
	dic['ice_four']=ice_four
	dic['ice_show']=ice_show
	dic['ice']=ice
	#获取用户名通过session
	dic['data']=uname
	return render(request, 'text/index.html', dic)


def list(request, id):
	return render(request, 'text/list.html')


# def detail(request, id):
#     dic = {'id': id}
#     return render(request, 'text/detail.html', dic)
@view_name
def detail(request,dic,id):
	#商品列表
	goods_list = Goods_list.objects.all()
	#单个商品详情
	goods = Goods_info.objects.get(pk=id)
	dic['goods']=goods
	dic['goods_list']=goods_list
	dic['list_id'] = goods.goods_list_id_id
	dic['list_name'] = goods.goods_list_id.goods_list_name
	dic['goods_info'] =Goods_info.objects.all().order_by('-id')[0:2]
	#获取购物车所有商品的数量
	cart = Cart.objects.all()
	goods_count = 0
	for cart_one in cart:
		goods_count += cart_one.goods_num
	dic['goods_count'] = goods_count
	return render(request,'text/detail.html',dic)

def base(request):
	return render(request, 'text/base.html')


def logout(request):
	del request.session['uname']
	return redirect(reverse('main:index'))

def place_order(request, order_num=1232,cart_id = [1,2]):
	#测试
	name = 'name'
	# name = request.session.get('uname')
	user = User_db.objects.get(user_name=name)
	receiver = user.receiver_set.last()
	address = receiver.receiver_address
	rece_name = receiver.receiver_name
	rece_phone = receiver.receiver_phone
	# 获取订单号对应的订单表信息
	user_ord = Ord.objects.get(order_num=order_num)
	# 通过对象获得订单号对应的的用户名
	uname = user_ord.order_user_id.user_name
	#判断cart_id的对应的购物车的用户和session对应的name是不是一样

	# 如果名字一样，则订单号和用户匹配，找订单号对应的商品
	if uname == name:
		# 获取订单详情里面最新的一条
		dorder = user_ord.order_detail_set.last()
		goods_num = dorder.odetail_goods_num
		pre_price = dorder.odetail_totalprice
		# goods = dorder.odetail_goods_id
		total_price = user_ord.total_price
		cart = user.cart_set.filter(pk__in=cart_id)
		# total_price = (goods.goods_price)*goods_num
		dic = {
				'address': address,
				'rece_name': rece_name,
				'rece_phone': rece_phone,
				'goods_num':goods_num,
				# 'goods':goods,
				'total_price':total_price,
				'cart':cart,
			   }
		return render(request, 'text/place_order.html', dic)

def cart(request):
	return render(request,'text/cart.html')
def success(request):
	return render(request,'text/success.html')