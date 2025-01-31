# def mainframe():
#     """Logic for execution task based on query"""
#     SR.scrollable_text_clearing()
#     greet()
#     query_for_future=None
#     try:
#         while(True):
#             query=SR.takeCommand().lower()          #converted the command in lower case of ease of matching

#             #wikipedia search
#             if there_exists(['search wikipedia for','from wikipedia'],query):
#                 SR.speak("Searching wikipedia...")
#                 if 'search wikipedia for' in query:
#                     query=query.replace('search wikipedia for','')
#                     results=wikipedia.summary(query,sentences=2)
#                     SR.speak("According to wikipedia:\n")
#                     SR.speak(results)
#                 elif 'from wikipedia' in query:
#                     query=query.replace('from wikipedia','')
#                     results=wikipedia.summary(query,sentences=2)
#                     SR.speak("According to wikipedia:\n")
#                     SR.speak(results)
#             elif there_exists(['wikipedia'],query):
#                 SR.speak("Searching wikipedia....")
#                 query=query.replace("wikipedia","")
#                 results=wikipedia.summary(query,sentences=2)
#                 SR.speak("According to wikipedia:\n")
#                 SR.speak(results)

#             #jokes
#             elif there_exists(['tell me joke','tell me a joke','tell me some jokes','i would like to hear some jokes',"i'd like to hear some jokes",
#                             'can you please tell me some jokes','i want to hear a joke','i want to hear some jokes','please tell me some jokes',
#                             'would like to hear some jokes','tell me more jokes'],query):
#                 SR.speak(pyjokes.get_joke(language="en", category="all"))
#                 query_for_future=query
#             elif there_exists(['one more','one more please','tell me more','i would like to hear more of them','once more','once again','more','again'],query) and (query_for_future is not None):
#                 SR.speak(pyjokes.get_joke(language="en", category="all"))

#             #asking for name
#             elif there_exists(["what is your name","what's your name","tell me your name",'who are you'],query):
#                 SR.speak("My name is Bonheur and I'm here to serve you.")
#             #How are you
#             elif there_exists(['how are you'],query):
#                 conn = sqlite3.connect('bobox.db')
#                 mycursor=conn.cursor()
#                 mycursor.execute('select sentences from howareyou')
#                 result=mycursor.fetchall()
#                 temporary_data=random.choice(result)[0]
#                 SR.updating_ST_No_newline(temporary_data+'😃\n')
#                 SR.nonPrintSpeak(temporary_data)
#                 conn.close()
#             #what is my name
#             elif there_exists(['what is my name','tell me my name',"i don't remember my name"],query):
#                 SR.speak("Your name is "+str(getpass.getuser()))

#             #calendar
#             elif there_exists(['show me calendar','display calendar'],query):
#                 SR.updating_ST(calendar.calendar(2021))

#             #google, youtube and location
#             #playing on youtube
#             elif there_exists(['open youtube and play','on youtube'],query):
#                 query='uwo yesu by papi clever and dorcas'
#                 if 'on youtube' in query:
#                     SR.speak("Opening youtube")
#                     pywhatkit.playonyt(query.replace('on youtube',''))
#                 else:
#                     SR.speak("Opening youtube")
#                     pywhatkit.playonyt(query.replace('open youtube and play ',''))
#                 break
#             elif there_exists(['play some songs on youtube','i would like to listen some music','i would like to listen some songs','play songs on youtube'],query):
#                 SR.speak("Opening youtube")
#                 pywhatkit.playonyt('play random songs')
#                 break
#             elif there_exists(['open youtube','access youtube'],query):
#                 SR.speak("Opening youtube")
#                 webbrowser.get(chrome_path).open("https://www.youtube.com")
#                 break
#             elif there_exists(['open google and search','google and search'],query):
#                 search_on_google()
#                 break
#             #image search
#             elif there_exists(['show me images of','images of','display images'],query):
#                  query = SR.takeCommand()
#                  search_google_images(query)
#                  break
#             elif there_exists(['search for','do a little searching for','show me results for','show me result for','start searching for'],query):
#                 SR.speak("Searching.....")
#                 if 'search for' in query:
#                     SR.speak(f"Showing results for {query.replace('search for','')}")
#                     pywhatkit.search(query.replace('search for',''))
#                 elif 'do a little searching for' in query:
#                     SR.speak(f"Showing results for {query.replace('do a little searching for','')}")
#                     pywhatkit.search(query.replace('do a little searching for',''))
#                 elif 'show me results for' in query:
#                     SR.speak(f"Showing results for {query.replace('show me results for','')}")
#                     pywhatkit(query.replace('show me results for',''))
#                 elif 'start searching for' in query:
#                     SR.speak(f"Showing results for {query.replace('start searching for','')}")
#                     pywhatkit(query.replace('start searching for',''))
#                 break

#             elif there_exists(['open google'],query):
#                 SR.speak("Opening google")
#                 webbrowser.open("http://www.google.com")
#                 break
#             elif there_exists(['find location of','show location of','find location for','show location for'],query):
#                 if 'of' in query:
#                     url='https://google.nl/maps/place/'+query[query.find('of')+3:]+'/&amp'
#                     webbrowser.get(chrome_path).open(url)
#                     break
#                 elif 'for' in query:
#                     url='https://google.nl/maps/place/'+query[query.find('for')+4:]+'/&amp'
#                     webbrowser.get(chrome_path).open(url)
#                     break
#             elif there_exists(["what is my exact location","What is my location","my current location","exact current location"],query):
#                 url = "https://www.google.com/maps/search/Where+am+I+?/"
#                 webbrowser.get().open(url)
#                 SR.speak("Showing your current location on google maps...")
#                 break
#             elif there_exists(["where am i"],query):
#                 Ip_info = requests.get('https://api.ipdata.co?api-key=test').json()
#                 loc = Ip_info['region']
#                 SR.speak(f"You must be somewhere in {loc}")

#             #who is searcing mode
#             elif there_exists(['who is','who the heck is','who the hell is','who is this'],query):
#                 query=query.replace("wikipedia","")
#                 results=wikipedia.summary(query,sentences=1)
#                 SR.speak("According to wikipdedia:  ")
#                 SR.speak(results)

#             #play music
#             elif there_exists(['play music','play some music for me','like to listen some music'],query):
#                 SR.speak("Playing musics")
#                 play_music()
#                 break

#             # top 5 news
#             elif there_exists(['top 5 news','top five news','listen some news','news of today'],query):
#                 news=Annex.News(scrollable_text)
#                 news.show()

#             #whatsapp message
#             elif there_exists(['open whatsapp messeaging','send a whatsapp message','send whatsapp message','please send a whatsapp message'],query):
#                 whatsapp=Annex.WhatsApp(scrollable_text)
#                 whatsapp.send()
#                 del whatsapp
#             #what is meant by
#             elif there_exists(['what is meant by','what is mean by'],query):
#                 results=wikipedia.summary(query,sentences=2)
#                 SR.speak("According to wikipedia:\n")
#                 SR.speak(results)
#            #opening file
#             elif there_exists(['open file','open command list'],query):
#                 SR.speak("Opening file")
#                 os.startfile("Commands List.txt")
#             #taking photo
#             elif there_exists(['take a photo','take a selfie','take my photo','take photo','take selfie','one photo please','click a photo'],query):
#                 takephoto=Annex.camera()
#                 Location=takephoto.takePhoto()
#                 os.startfile(Location)
#                 del takephoto
#                 SR.speak("Captured picture is stored in Camera folder.")

#             #bluetooth file sharing
#             elif there_exists(['send some files through bluetooth','send file through bluetooth','bluetooth sharing','bluetooth file sharing','open bluetooth'],query):
#                 SR.speak("Opening bluetooth...")
#                 os.startfile(r"C:\Windows\System32\fsquirt.exe")
#                 break

#             #play game
#             elif there_exists(['would like to play some games','play some games','would like to play some game','want to play some games','want to play game','want to play games','play games','open games','play game','open game'],query):
#                 SR.speak("We have 2 games right now.\n")
#                 SR.updating_ST_No_newline('1.')
#                 SR.speak("Stone Paper Scissor")
#                 SR.updating_ST_No_newline('2.')
#                 SR.speak("Snake")
#                 SR.speak("\nTell us your choice:")
#                 while(True):
#                     query=SR.takeCommand().lower()
#                     if ('stone' in query) or ('paper' in query):
#                         SR.speak("Opening stone paper scissor...")
#                         sps=Annex.StonePaperScissor()
#                         sps.start(scrollable_text)
#                         break
#                     elif ('snake' in query):
#                         SR.speak("Opening snake game...")
#                         import Snake
#                         Snake.start()
#                         break
#                     else:
#                         SR.speak("It did not match the option that we have. \nPlease say it again.")

#             #makig note
#             elif there_exists(['make a note','take note','take a note','note it down','make note','remember this as note','open notepad and write'],query):
#                 SR.speak("What would you like to write down?")
#                 data=SR.takeCommand()
#                 n=Annex.note()
#                 n.Note(data)
#                 SR.speak("I have a made a note of that.")
#                 break

#             #flipping coin
#             elif there_exists(["toss a coin","flip a coin","toss"],query):
#                 moves=["head", "tails"]
#                 cmove=random.choice(moves)
#                 playsound.playsound('quarter spin flac.mp3')
#                 SR.speak("It's " + cmove)

#             #time and date
#             elif there_exists(['the time'],query):
#                 strTime =datetime.datetime.now().strftime("%H:%M:%S")
#                 SR.speak(f"Sir, the time is {strTime}")
#             elif there_exists(['the date'],query):
#                 strDay=datetime.date.today().strftime("%B %d, %Y")
#                 SR.speak(f"Today is {strDay}")
#             elif there_exists(['what day it is','what day is today','which day is today',"today's day name please"],query):
#                 SR.speak(f"Today is {datetime.datetime.now().strftime('%A')}")
#             elif there_exists(['Thanks','Thank you','I appreciate you','Thanks for helping']):
#                 SR.speak("You're welcome!")
#                 break
#             #opening software applications
#             elif there_exists(['open chrome'],query):
#                 SR.speak("Opening chrome")
#                 os.startfile(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
#                 break
#             elif there_exists(['open notepad plus plus','open notepad++','open notepad ++'],query):
#                 SR.speak('Opening notepad++')
#                 os.startfile(r'C:\Program Files\Notepad++\notepad++.exe')
#                 break
#             elif there_exists(['open notepad','start notepad'],query):
#                 SR.speak('Opening notepad')
#                 os.startfile(r'C:\Windows\notepad.exe')
#                 break
#             elif there_exists(['open ms paint','open mspaint','open microsoft paint','start microsoft paint','start ms paint'],query):
#                 SR.speak("Opening Microsoft paint....")
#                 os.startfile('C:\Windows\System32\mspaint.exe')
#                 break
#             elif there_exists(['show me performance of my system','open performance monitor','performance monitor','performance of my computer','performance of this computer'],query):
#                 os.startfile("C:\Windows\System32\perfmon.exe")
#                 break
#             elif there_exists(['open snipping tool','snipping tool','start snipping tool'],query):
#                 SR.speak("Opening snipping tool....")
#                 os.startfile("C:\Windows\System32\SnippingTool.exe")
#                 break
#             elif there_exists(['open code','open visual studio ','open vs code'],query):
#                 SR.speak("Opeining vs code")
#                 codepath=r"C:\Users\Vishal\AppData\Local\Programs\Microsoft VS Code\Code.exe"
#                 os.startfile(codepath)
#                 break
#             elif there_exists(['open file manager','file manager','open my computer','my computer','open file explorer','file explorer','open this pc','this pc'],query):
#                 SR.speak("Opening File Explorer")
#                 os.startfile("C:\Windows\explorer.exe")
#                 break
#             elif there_exists(['powershell'],query):
#                 SR.speak("Opening powershell")
#                 os.startfile(r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe')
#                 break
#             elif there_exists(['cmd','command prompt','command prom','commandpromt',],query):
#                 SR.speak("Opening command prompt")
#                 os.startfile(r'C:\Windows\System32\cmd.exe')
#                 break
#             elif there_exists(['open whatsapp'],query):
#                 SR.speak("Opening whatsApp")
#                 os.startfile(r'C:\Users\Vishal\AppData\Local\WhatsApp\WhatsApp.exe')
#                 break
#             elif there_exists(['open settings','open control panel','open this computer setting Window','open computer setting Window'   ,'open computer settings','open setting','show me settings','open my computer settings'],query):
#                 SR.speak("Opening settings...")
#                 os.startfile('C:\Windows\System32\control.exe')
#                 break
#             elif there_exists(['open your setting','open your settings','open settiing window','show me setting window','open voice assistant settings'],query):
#                 SR.speak("Opening my Setting window..")
#                 sett_wind=Annex.SettingWindow()
#                 sett_wind.settingWindow(root)
#                 break
#             elif there_exists(['open vlc','vlc media player','vlc player'],query):
#                 SR.speak("Opening VLC media player")
#                 os.startfile(r"C:\Program Files\VideoLAN\VLC\vlc.exe")
#                 break

#             #password generator
#             elif there_exists(['suggest me a password','password suggestion','i want a password'],query):
#                 m3=Annex.PasswordGenerator()
#                 m3.givePSWD(scrollable_text)
#                 del m3
#             #screeshot
#             elif there_exists(['take screenshot','take a screenshot','screenshot please','capture my screen'],query):
#                 SR.speak("Taking screenshot")
#                 SS=Annex.screenshot()
#                 SS.takeSS()
#                 SR.speak('Captured screenshot is saved in Screenshots folder.')
#                 del SS

#             #voice recorder
#             elif there_exists(['record my voice','start voice recorder','voice recorder'],query):
#                 VR=Annex.VoiceRecorer()
#                 VR.Record(scrollable_text)
#                 del VR

#             #text to speech conversion
#             elif there_exists(['text to speech','convert my notes to voice'],query):
#                 SR.speak("Opening Text to Speech mode")
#                 TS=Annex.TextSpeech()
#                 del TS

#             #weather report
#             elif there_exists(['weather report','temperature'],query):
#                 Weather=Annex.Weather()
#                 Weather.show(scrollable_text)

#             #shutting down system
#             elif there_exists(['exit','quit','shutdown','shut up','goodbye','shut down'],query):
#                 SR.speak("shutting down")
#                 sys.exit()

#             elif there_exists(['none'],query):
#                 pass
#             elif there_exists(['stop the flow','stop the execution','halt','halt the process','stop the process','stop listening','stop the listening'],query):
#                 SR.speak("Listening halted.")
#                 break
#             #it will give online results for the query
#             elif there_exists(['search something for me','to do a little search','search mode','i want to search something'],query):
#                 SR.speak('What you want me to search for?')
#                 query=SR.takeCommand()
#                 SR.speak(f"Showing results for {query}")
#                 try:
#                     res=app.query(query)
#                     SR.speak(next(res.results).text)
#                 except:
#                     print("Sorry, but there is a little problem while fetching the result.")

#             #what is the capital
#             elif there_exists(['what is the capital of','capital of','capital city of'],query):
#                 try:
#                     res=app.query(query)
#                     SR.speak(next(res.results).text)
#                 except:
#                     print("Sorry, but there is a little problem while fetching the result.")

#             elif there_exists(['temperature'],query):
#                 try:
#                     res=app.query(query)
#                     SR.speak(next(res.results).text)
#                 except:
#                     print("Internet Connection Error")
#             elif there_exists(['+','-','*','x','/','plus','add','minus','subtract','divide','multiply','divided','multiplied'],query):
#                 try:
#                     res=app.query(query)
#                     SR.speak(next(res.results).text)
#                 except:
#                     print("Internet Connection Error")

#             else:
#                 SR.speak("Sorry it did not match with any commands that i'm registered with. Please say it again.")
#     except Exception as e:
#         pass