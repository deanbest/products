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