from bs4 import BeautifulSoup
import requests, time

target = '3060'

def get_avg_price(key):
####################
    if any(a in key.lower() for a in ['super','супер','0s','0с']):
           stop_words = ['ti','lhr']
           print('ищу super')
    
    elif any(a in key.lower() for a in [' ti', '0ti','ti']):
           stop_words = ['super','супер','0s','0с','lhr','1050','1060','1070','1080','1650','1660','1670','2050','2060','2070','2080','3050','3070','3080','3090','4050','4060','4070','4080','4090']
           print('ищу ti')
    else:
         stop_words = ['ti','lhr','super', '0s', 'супер','1050','1060','1070','1080','1650','1660','1670','2050','2060','2070','2080','3050','3070','3080','3090','4050','4060','4070','4080','4090']
    pagin = 15 
    count = 0 
    sum = 0 
    mimo = 0 

    for p in range(pagin):
        p=p+1 
        url = f'https://www.avito.ru/all/tovary_dlya_kompyutera/komplektuyuschie/videokarty?p={p}&q={key}'
        request =requests.get(url)
        bs = BeautifulSoup(request.text,'html.parser')
        products = bs.find_all('div', class_='iva-item-root-_lk9K photo-slider-slider-S15A_ iva-item-list-rfgcH iva-item-redesign-rop6P iva-item-responsive-_lbhG items-item-My3ih items-listItem-Gd1jN js-catalog-item-enum')
        print(f'page {p}:\n\n')
        for product in products:
            name = product.find('h3',class_='title-root-zZCwT iva-item-title-py3i_ title-listRedesign-_rejR title-root_maxHeight-X6PsH text-text-LurtD text-size-s-BxGpL text-bold-SinUO')
            if any(word in name.string.lower() for word in stop_words):
                print('stop_word!!!: ', name.string) 
                mimo+=1
            else: 
                id = product['id']
                dicription = product.meta['content'] 
                value = product.find('span',class_='price-text-_YGDY text-text-LurtD text-size-s-BxGpL')
                value = value.text.replace('₽','')
                price = value.replace('\xa0','')
                if price !='Цена не указана': 
                    print(int(price), name.string) 
                    count +=1
                    sum+=int(price)

        time.sleep(1) 

    avg_price = round(sum/count,2)
    print (f'_____________\nкол-во = {count}\nмимо = {mimo}\navg = {avg_price} RUB')

def main():
    print('na4al')
    get_avg_price(target)
    print('end')

if __name__ == '__main__':
    main()
