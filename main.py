from fastapi import FastAPI
import datetime
app = FastAPI()


@app.get("/")
def get_home():
     samo = [
        { "id" : 1 , "title" : "Samo textile - matoning yangi hayoti" , "discripe" : "Kompaniyamiz 1996-yildan beri zamonaviy trikotaj mahsulotlarini ishlab chiqarib kelmoqda. Yillar davomida to‘plangan tajriba, sifat nazorati, kolleksiyalarning doimiy yangilanib borilishi va arzon narxlar tufayli kompaniyamiz ishlab chiqarilgan mahsulotlarga tabiiy talabga ega bo‘ldi."},
        { "id" : 2 , "title" : "Har bir to'lovlar mukamallik bilan to'lanadi" , "discripe" : "Kompaniyamiz 1996-yildan beri zamonaviy trikotaj mahsulotlarini ishlab chiqarib kelmoqda. Yillar davomida to‘plangan tajriba, sifat nazorati, kolleksiyalarning doimiy yangilanib borilishi va arzon narxlar tufayli kompaniyamiz ishlab chiqarilgan mahsulotlarga tabiiy talabga ega bo‘ldi."},
        { "id" : 3 , "title" : "Samo textile - mukamalikka elituvchi yo'l" , "discripe" : "Kompaniyamiz 1996-yildan beri zamonaviy trikotaj mahsulotlarini ishlab chiqarib kelmoqda. Yillar davomida to‘plangan tajriba, sifat nazorati, kolleksiyalarning doimiy yangilanib borilishi va arzon narxlar tufayli kompaniyamiz ishlab chiqarilgan mahsulotlarga tabiiy talabga ega bo‘ldi."}
     ] ,
     about = [
          {"title" : "Samo Textile" , "descripe" : "Kompaniyamiz 1996-yildan beri zamonaviy trikotaj mahsulotlarini ishlab chiqarib kelmoqda. Yillar davomida to‘plangan tajriba, sifat nazorati, kolleksiyalarning doimiy yangilanib borilishi va arzon narxlar tufayli kompaniyamiz ishlab chiqarilgan mahsulotlarga tabiiy talabga ega bo‘ldi. Ishlab chiqarilayotgan mahsulotlarning 95 foizi quyidagi davlatlarga eksport qilinadi: Rossiya, Ukraina, Qozog‘iston, Qirg‘iziston, Moldova, Turkiya, Latviya, Italiya, Polsha, Portagul, Germaniya, Ruminiya, AQSh, Buyuk Britaniya yo‘l, bugun butun O‘zbekiston va xalqaro bozorni o‘ziga rom etgan sanoat imperiyasiga aylangan"}
     ]
     return samo  , about


@app.get("/products")
def get_products():
    
    item = [
         {"id" : 1 , "name" : "Double-spelling" , "title" : "He is very suitable for men and women in sewing hot suits, as well as to bet children's clothes." , "images" : "https://samo.uz/_next/image/?url=https%3A%2F%2Fback.samo.uz%2Fmedia%2Fproduct%2F637b772289e33_wBDzXDZ.jpg&w=640&q=75"},
         {"id" : 2 , "name" : "Spinning knitting" , "title" : "He is very suitable for men and women in sewing hot suits, as well as to bet children's clothes." , "images" : "https://samo.uz/_next/image/?url=https%3A%2F%2Fback.samo.uz%2Fmedia%2Fproduct%2F3iplik.jpg&w=640&q=75"},
         {"id" : 3 , "name" : "Interlic" , "title" : "He is very suitable for men and women in sewing hot suits, as well as to bet children's clothes." , "images" : "https://samo.uz/_next/image/?url=https%3A%2F%2Fback.samo.uz%2Fmedia%2Fproduct%2F637b76ddb0728_Bo2GRuR.jpg&w=640&q=75"},
         {"id" : 4 , "name" : "Double-spelling" , "title" : "He is very suitable for men and women in sewing hot suits, as well as to bet children's clothes." , "images" : "https://samo.uz/_next/image/?url=https%3A%2F%2Fback.samo.uz%2Fmedia%2Fproduct%2F637b772289e33_wBDzXDZ.jpg&w=640&q=75"},
         {"id" : 5 , "name" : "Double-spelling" , "title" : "He is very suitable for men and women in sewing hot suits, as well as to bet children's clothes." , "images" : "https://samo.uz/_next/image/?url=https%3A%2F%2Fback.samo.uz%2Fmedia%2Fproduct%2F637b772289e33_wBDzXDZ.jpg&w=640&q=75"},
         {"id" : 6 , "name" : "Double-spelling" , "title" : "He is very suitable for men and women in sewing hot suits, as well as to bet children's clothes." , "images" : "https://samo.uz/_next/image/?url=https%3A%2F%2Fback.samo.uz%2Fmedia%2Fproduct%2F637b772289e33_wBDzXDZ.jpg&w=640&q=75"}
    ]

    return item


@app.get("./gallery")
def get_Gallery():
     image = [
          { "id" : 1 , "image" : "https://samo.uz/_next/image/?url=https%3A%2F%2Fback.samo.uz%2F%2F%2Fmedia%2Fgallery%2F1_8_2.jpg&w=1920&q=75"},
          { "id" : 2 , "image" : "https://samo.uz/_next/image/?url=https%3A%2F%2Fback.samo.uz%2F%2F%2Fmedia%2Fgallery%2F2B3A1173_3.jpg&w=1920&q=75"},
          { "id" : 3 , "image" : "https://samo.uz/_next/image/?url=https%3A%2F%2Fback.samo.uz%2F%2F%2Fmedia%2Fgallery%2F2B3A5982_copy.jpg&w=1920&q=75"},
          { "id" : 4 , "image" : "https://samo.uz/_next/image/?url=https%3A%2F%2Fback.samo.uz%2F%2F%2Fmedia%2Fgallery%2F2B3A5939_copy.jpg&w=1920&q=75"},
          { "id" : 5 , "image" : "https://samo.uz/_next/image/?url=https%3A%2F%2Fback.samo.uz%2F%2F%2Fmedia%2Fgallery%2F1_8_2.jpg&w=1920&q=75"},
          { "id" : 6 , "image" : "https://samo.uz/_next/image/?url=https%3A%2F%2Fback.samo.uz%2F%2F%2Fmedia%2Fgallery%2F2B3A2157_2.jpg&w=1920&q=75"},
          { "id" : 7 , "image" : "https://samo.uz/_next/image/?url=https%3A%2F%2Fback.samo.uz%2F%2F%2Fmedia%2Fgallery%2F1_8_2.jpg&w=1920&q=75"}
     ]
     return image



@app.get("/news")
def get_News():

    time = datetime.datetime.now() 

    news = [
         {"id" : 1 , "real-time" : time , "title" : "SAMO-TIY Bee-togther.ru B2b platform: Together for stable "},
         {"id" : 2 , "real-time" : time , "title" : "New stage in research and production"},
         {"id" : 3 , "real-time" : time , "title" : "SAMO-TIY Bee-togther.ru B2b platform: Together for stable "},
         {"id" : 4 , "real-time" : time , "title" : "New stage in Samo Textile: Zimdor Roty Printing Machine is being"},
         {"id" : 5 , "real-time" : time , "title" : "SAMO-TIY Bee-togther.ru B2b platform: Together for stable "},
         {"id" : 6 , "real-time" : time , "title" : "The Mevki, with 3 more, increases the volume of 3 more, and this will increase production. "},
    ]
    return news