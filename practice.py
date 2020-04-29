products = []
while True:
	name = input('快輸入商品名稱: ')
	if name == 'q':
		break
	price = input('輸入商品價格呀: ')
	place = input('產地呢: ')
	#理解的寫法 p = []
	#理解的寫法 p.append(name)
	#理解的寫法 p.append(price) 
	#簡潔寫法 p = [name, price, place] 
	products.append([name, price, place])  #把小火車裝進大火車products清單中,更簡寫法
print(products)

for p in products: #印出清單中的每個東西
	print(p[0], '是來自於', p[2]) #印出每一個小清單的第0格及價格
