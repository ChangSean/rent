driving = input('請問您會開車嗎?:')
if driving != '會' and driving != '不會':
	print('請回答會或不會')
	raise SystemExit


age = input('請問您的年齡?:')
age = int(age)
if driving == '會':
	if age >= 18:
		print('您可以租車了!')
	else:
		print('抱歉您還沒資格租車喔~')
elif driving == '不會':
	if age >= 18:
		print('我們租車需要會開車喔~')
	else:
		print('抱歉!我們無法租車給您~')