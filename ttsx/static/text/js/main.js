$(function(){

	$.ajax({
		url: 'js/user.json',
		type: 'GET',
		dataType: 'json'
	})
	.done(function(data) {

		if(data.code==1)
		{
			$('.login_info').html('欢迎您：<em>'+ data.userinfo.name +'</em>').show();
			$('.login_btn').hide();
		}
	})
	.fail(function() {
		//console.log("error");
	});


	$.ajax({
		url: 'js/goods.json',
		type: 'GET',
		dataType: 'json'
	})
	.done(function(data) {

		if(data.code==1)
		{
			var len = data.goodsinfo.recommend.length;
			var str = '<span>|</span>';
			for(var i=0;i<len;i++)
			{
				str+='<a href="'+ data.goodsinfo.recommend[i].goodslink +'">'+ data.goodsinfo.recommend[i].goodsname +'</a>';
			}

			$('#hot_goods01').html(str);


			var len2 = data.goodsinfo.goodslist.length;
			var str2 = '';

			for(var i=0;i<len2;i++)
			{
				str2 += '<li>'+
						'<h4>'+ data.goodsinfo.goodslist[i].goodsname +'</h4>'+
						'<a href="'+ data.goodsinfo.goodslist[i].goodslink +'"><img src="'+ data.goodsinfo.goodslist[i].goodspic +'" alt="商品图片"></a>'+
						'<p>¥ '+ (data.goodsinfo.goodslist[i].price).toFixed(2) +'</p>'+
						'</li>';
			}

			$('#goods_list01').html(str2);

		}
		


	})
	.fail(function() {
		alert('服务器超时，请重试！');
	})


});