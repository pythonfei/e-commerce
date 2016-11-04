from django import template
register = template.Library()

@register.filter
def xiaoTotal(price,count):
	total=float(price)*int(count)
	return '%.2f'% total
