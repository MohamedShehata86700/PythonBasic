import telebot , requests , json ; from telebot import types
import telebot
s=requests.session()
bot = telebot.TeleBot('6333255778:AAHjKE-mOYBWcdKHUzNwO41Nkgy3M8MkR2E')
@bot.message_handler(commands=['start'])
def start(message):
  start = types.InlineKeyboardButton(text='- معرفة النتيجة',callback_data='start')
  Ronaldo = types.InlineKeyboardMarkup(row_width=2) ; Ronaldo.add(start)
  bot.send_message(message.chat.id,text='- اهلا بك عزيزي في بوت King of Deepweb ',reply_markup=Ronaldo)
@bot.callback_query_handler(func=lambda call:True)
def start2(call):
  if call.data=='start':
    ji = bot.send_message(call.message.chat.id,text="""
    اهلاً بَك عزيزي ارسل رقمك القومي ثم 
    مسافه ثم الباسورد ثم مسافه ثم رقم السنه علي سطر واحد
    مع العلم 
    رقم 0 لنتيجة السنه الحاليه
    رقم 1 لنتيجة السنه ال قبلها وهكذا كل ما تذود رقم تقل سنه
    مثال:-
    30102012618171 Aamm999 0
    البوت صالح لجميع السنوات من اولي لرابعه
    Developer @M_S_H_VIP
    """)
    bot.register_next_step_handler(ji,dow)
def dow(message):
    chat_id = message.chat.id
    parts = message.text.split(" ")
    Id = parts[0]
    password = parts[1]
    year=int(parts[2])
    headersc = {
        'Accept': '*/*',
        'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://stda.minia.edu.eg',
        'Referer': 'http://stda.minia.edu.eg/',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    datac = {
        'UserName': Id,
        'Password': password,
    }

    responsec = s.post('http://stda.minia.edu.eg/Portallogin', headers=headersc, data=datac, verify=False).cookies['PortalStudentUserID']


    ######get UUID #####
    cookiesd = {
        'PortalStudentUserID':responsec,
    }

    headersd = {
        'Accept': '*/*',
        'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://stda.minia.edu.eg',
        'Referer': 'http://stda.minia.edu.eg/?num=28741',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    datad = {
        'param0': 'Portal.General',
        'param1': 'GetStudentPortalData',
        'param2': '{"UserID":""}',
    }

    responsed = s.post('http://stda.minia.edu.eg/PortalgetJCI', cookies=cookiesd, headers=headersd, data=datad, verify=False)
    for i in responsed.json():
        StdName=i['StdName']
    import re
    w_patternd = r'"UUID": "(.*?)"'
    w_matchd = re.search(w_patternd, responsed.text)
    if w_matchd:
        Ud = w_matchd.group(1)
        print(Ud)
    else:print("Token not found.")


    ##### get results ####
    cookies = {
        'PortalStudentUserID':responsec,
    }
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://stda.minia.edu.eg',
        'Referer': 'http://stda.minia.edu.eg/?num=26977',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    data = {
        'param0': 'Portal.Results',
        'param1': 'GetAllResults',
        'param2': f'{{"UUID":"{Ud}"}}',
    }
    import json

    response = s.post('http://stda.minia.edu.eg/PortalgetJCI', cookies=cookies, headers=headers, data=data, verify=False).json()[year]['ds']

    # افتح ملف نصي للكتابة
    with open('results.txt', 'a+') as file:
        file.write(f' {message}\n')
        file.write(f' {StdName}\n')
        for item in response:
            z = item['StudyYearCourses']
            for it in z:
                Degree = it['Total']
                try:
                    file.write(f'الدرجة الخاصة بك: {Degree}\n')
                    bot.send_message(chat_id, text=f'    الدرجه الخاصه بك {Degree}')
                except:
                    pass
                Max = it['Max']
                try:
                    file.write(f'القيمة العظمى للمادة: {Max}\n')
                    bot.send_message(chat_id, text=f'      القيمه العظمي للماده {Max}')
                except:
                    pass
                GraderName = it['GradeName']
                try:
                    file.write(f'تقديرك: {GraderName}\n')
                    bot.send_message(chat_id, text=f'    تقديرك {GraderName}')
                except:
                    pass
                x = it['Parts']
                for i in x:
                    CoursePartName = i['CoursePartName']
                    try:
                        file.write(f'{CoursePartName}\n{"*" * 20}\n')
                        bot.send_message(chat_id, text=CoursePartName+""+"*"*20)
                    except:
                        pass               
    Result=f"""
    نتيجتك من موقع.  King of deep web


    {CoursePartName} 
    الدرجه الخاصه بك {Degree}

      القيمه العظمي للماده {Max}

    تقديرك {GraderName}


   Developer @M_S_H_VIP 
    """
    print (Result)        

    bot.send_message(chat_id, text=Result)

if __name__ == "__main__":
    bot.infinity_polling()

