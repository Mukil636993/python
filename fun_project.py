#empty strings
to_store_positive=0
to_store_negative=0
#character love level for you
yoimiya=0
yuki=0
money=0
#start of the story
print('\nwelcome to my game 🎉🎉😊 choices matters in the game, so choose it wisely \n'.title())
print("In this game you're the protogonist of the game,you go the highschool and met three  girls so what will you do, that's the premise of the game so what will you do as the protogonist of the game?\n")
#name from player
player_name=input('enter your name:')
#protogonist life
story_line=['I am '+player_name,'i am 16 years old','you thinking how i can speak to you like this because am the developer i can do anything','enough chit chat','Do you even know that you\'re late to school wake up you idiot','now the first choice gonna appear and the author and developer of the game gonna leave you','so good luck with the game']
print('\nThe story now begins')
input('\npress enter to continue the story enjoy!!!😘')
#for loop to loop through the story
for story in story_line:
  print(story)
  input()
#first choice of the game
#put the choices in loop in case of wrong input
mistake=True
while mistake:
  player_choice=input(' for get ready for the school press "y" \n for not go to school press "n"\n')
  if player_choice.lower()=="y":
    print('you\'re ready for the school\n')
    to_store_positive+=1
    mistake=False
    #on the way to school story
    bus_stop_story=['since you\'re late to school you started running','there is a turn in the way to the bus stop','when you try turn to the side of the road ','you bumbed into a girl']
    for bus in bus_stop_story:
     print(bus)
     input()
    #puting tuple values in list
    char_bus_dialogues=[
    ('yoimiya','owch '),
    (player_name,'ouch it hurts'),
    ('yoimiya','DON\'T YOU HAVE EYES OWWW WHY ARE RUSHING LIKE THAT')
    ]
    for character,line in char_bus_dialogues:
      print(f'{character}: {line}')
      input()
    character_pos_dialogue=[
      (player_name,'am really really sorry am just late to school'),
      ('yoimiya','atleast you\'re asking sorry i appreciate that,don\'t run around like this it dangerous'),
      (player_name,'yeah i won\'t am really sorry yoimiya'),
      ('yoimiya','its okay and wait a minute how do you know my name'),
      (player_name,'we are in same class ,its not your fault that you don\'t know me most of classmates don\'t know me because am always silent'),
      ('yoimiya','ohh you\'re '+player_name+' always sitting in the last bench and talk to no one now i remember'),
      (player_name,'let me introduce myself am '+player_name+''),
      ('yoimiya','hey idiot its not the time for the!!!!! we both gonna be late'),
      (player_name,'oh shit you\'re right runnnn'),
      ('','Both of them hurry to the school while smiling because of what happened earlier')
    ]
    character_neg_dialogue=[
      ('','you just walked away'),
      ('','i know this girl don\'t i she is from my same class her name is yoimiya ig'),
      ('','i just walked away without saying anything'),
      ('','its not the time to think about lets leave i am late to class')
    ]
    character_pos_dialogue1=[
    (player_name,'Finally we arrived at the school'),
    ('yoimiya','we still late you idiot, but arriving to school with someone is actually fun eventhough we are late'),
    (player_name,'glad you think like that its fun'),
    ('yoimiya','eventhough it\'s the first time we are meeting you\'re are funny lets talk some other time bye '+player_name),
    (player_name,'bye yoimiya'),
    (':','I just go to my usual place to sit')
    ]
    mistake1=True
    while mistake1:
      #player choice 2
      player_choice_2=input('To say sorry press "y"\nTo just walkaway without sorry press"n"\n')
      if player_choice_2.lower()=='y':
        yoimiya+=1
        to_store_positive+=1
        for character,line in character_pos_dialogue:
          print(f'{character}:{line}')
          input()
        for character,line in(character_pos_dialogue1):
         print(f"{character}: {line}")
         input()
         mistake1=False
      elif player_choice_2.lower()=='n':
        yoimiya-=1
        to_store_negative+=1
        for character,line in character_neg_dialogue:
          print(f'{character}: {line}')
          input()
          mistake1=False
        character_neg_dialogue1=[
        (':','finally i reached class '),
        (':','there is a girl standing there at the front of the classroom'),
        (':','i think she is also late to the class'),
        (':','when get closer its the girl i bumbed in the morning'),
        (':','i did\'nt even say sorry earlier hope she is not mad'),
        ('yoimiya','hmphh '),
        (':','she definetly mad'),
        (':','i just go to my usual place to sit')
        ] 
        for character,line in character_neg_dialogue1:
          print(f"{character}: {line}")
          input()
          mistake1=False
      else:
        print('you put the wrong input you fucking retard put the input carefully because of you guys, like i have code a seperate line of code for this, now put the input correctly')
        continue
      #after meeting yoimiya and not interating with her
      common_story_for_school=[
        (':','I placed my bag on the bench and pacing out in the windows'),
        (':','The birds where chirping while i pacing out'),
        (':','There is no one i can talk with in the class'),
        (':','teacher arrived in class'),
        (':','first period was my worst subject because its maths'),
        (':','i hate maths to the every single fiber in my body'),
        (':','still i have to listen to this lecture becoz i have to pass so there is no otherway'),
        ('maths_teacher','today we gonna cover trigonomatry first chapter'),
        (':','hahh💨 worst topic in maths'),
        (':','since there is no other way to pass the exam so lisened to the whole lucture'),
        (':','she finally finished her lecture and left the class'),
        (':','finally finished'),
        (':','After the class finished i decide to go to the restroom'),
        (':','when i get closer to restroom i heard some noise in restroom'),
        (':','there is locker beside the restroom'),
        (':','i heard crying souds in the locker!!!!! its afternoon everyone busy with lunch and playing so there is no one near'),
        (':','i gently get closer to the locker'),
        (':','is someone inside? hello...'),
        (':','the weeping sound was stopped and also the locker was locked outside'),
        (':','am gonna call the teacher if no one answers in 5 sec'),
        (':','5'),
        (':','4'),
        (':','3'),
        (':','2'),
        (':','1'),
        ('a girl voice?','doonn\'t call.. the teacher plzzz...'),
        (':','her voice soo slow and trembling i can feel that'),
        (player_name,'wait let me get you out first and explain what happened'),
        (':','she is trembling when i open the locker she looked at me with a dead expression on her face'),
        (':','when i saw that look on her face it reminds of me when i am in my middle school'),
        (':','she is crammed inside the locker while wiping the tears off of her face'),
        (':','i gently grabbed her and she is drenched in water and sweat she is hyperventing'),
        (':','she has no strenth in her legs to stand up'),
        (':','so i lift her up and take her to the infirmary in the school'),
        (':','but there is no one at the infirmary,she has barely have any conciounous'),
        (':','I placed her in the bed and wiping of her sweats'),
        (':','she has fever too so i know some medicine that can help her'),
        (':','I started searching inside the medicine cabinet')
        ]
      for character,line in common_story_for_school:
        print(f'{character}: {line}')  
        input()
      #searching for the medicine using list or tuple
      medicine=("colobal",'citrizen','no cold','riblovin','metrogyl')
      print(medicine)
      print('')
      print('these are the medicine i can see i have to pick the right one for her')
      print('')
      print('if you want to give her colbal enter 1\nif citrizen enter 2\nif no cold enter 3\nif riboflovin enter 4\nif metrogyl enter 5')
      print('')
      mistake2=True
      while mistake2:
        player_medicine_choice=input("pick the right tablet for her>")
        if player_medicine_choice=='1':
         print('\nits the right tablet for fever,lets give it to her')
         mistake2=False
        else:
          print('it\'s a wrong medicine pick the correct one!!')
          continue
      #after choosed the right medicine
      in_the_infirmary_story=[
        (':','I take a glass of water and bring it to her'),
        (':','she barely has any conciounous'),
        (':','i waked her up by splashing little bit of water on her face'),
        (':','she woke up after some couple of seconds'),
        ('???','where am i ahh... my head hurts'),
        (player_name,'you\'re in the infirmary i carried you here'),
        ('???','who are you? and caa...rr..ied me.... i remember nowww i was in the locker'),
        ('???','those girls bullied me and poured some water on me and locked me there'),
        ('???','"sob...." "sob...."'),
        (player_name,'don\'t cry everything okay now don\'t worry'),
        ('???','no its not, they will hurt me tommorow and next day and NEXT DAYY AND NEXT DAY AND AND AND AND AND i dont know what to do "sob....." '),
        (player_name,'calmdown first breath slowly and let out slowly now here take this tablet it will help to reduce your fever'),
        ('???','th..ank youuu for carried me here and taking care of me'),
        (player_name,'i can\'t ignore a girl who is in trouble and am ' +player_name+' from "A" class'),
        ('???','am yuki from "B" class'),
        (player_name,'so what happened in the interval can you tell me about it'),
        ('yuki','there are three girls in my class and the one called "karen" is the leader of the two,karen likes a boy from my class ,his name is yoshida but he likes me so she got jelous and doing terrible things to me "'),
        ('yuki','but i have no intrest in him , i even told her that but they continued to bully'),
        ('yuki','i don\'t even know what to do anymore'),
        (player_name,'so thats what happened')
      ]
      char_pos_dialogue2=[
        (player_name,'don\'t worry am here for you,don\'t ever feel alone'),
        (player_name,'if anything happens tell me about it, i can help with that okay'),
        (player_name,'i will handle them when the time comes'),
        (':','pats her head'),
        ('yuki','is it okay to belive you ,is it okay to having a hope'),
        (player_name,'yeah you can , just belive in me everything will get better'),
        (':','she started to cry on my shoulder')
      ]
      char_neg_dialogue2=[
        (':','i decided to stay silent becoz i don\'t want to get trouble with them'),
        (':','she cried for like 10 mins and i didnt say anything to her'),
        (':','there is a part of me still feels guilty for what i did'),
        (player_name,'i will try to do something about the bullies so don\'t worry '),
        ('yuki','thank you')
      ]
      #common story
      for character,line in in_the_infirmary_story:
        print(f'{character}: {line}')
        input()
      #player choice 3 console yuki
      mistake3=True
      while mistake3:
        player_choice_3=input('IF YOU WANT TO CONSOLE HER PRESS "y"\nTO STAY SILENT AND DON\'T WANT TO CONSOLE HER PRESS "n">')
        if player_choice_3.lower()=='y':
          yuki+=1
          for character,line in char_pos_dialogue2:
            print(f'{character}: {line}')
            input()
            mistake3=False
        elif player_choice_3.lower()=='n':
          yuki-=1
          for character,line in char_neg_dialogue2:
            print(f'{character}: {line}')
            input()
            mistake3=False
        else:
          print('you put the wrong input')
          continue
      #after consoling
      after_the_console=[
        (':','we both left the infirmary and headed toward our class'),
        (player_name,'if anything happens tell me okay'),
        ('yuki','i will thank you for the help'),
        (':','hope she will be okay'),
        (':','we go to our seperate class'),
        (':','its bilogy class my fav one'),
        (':','time passed class ends'),
        (':','i headed toward home'),
        (':','i have little sister at home her name is hotaru '),
        (':','she is an elementary school student'),
        (':','our parents died in a car accident a year ago,we lost everything on that day'),
        (':','on that day onwards she is the only family i have'),
        ('','after that , am the one taking care of everything'),
        (player_name,'i am home hotaru'),
        ('hotaru','welcome home brother'),
        ('hotaru','i prepared dinner for you'),
        (player_name,'reallyy can\'t wait to taste it thank you hotaru'),
        ('hotaru','hehe'),
        (':','i finished dinner with hotaru'),
        (':',"what will i do now")
        ]
def show_scene(scene):
    for character,line in scene:
      print(f'{character}: {line}')
      input()
def start():
  show_scene(after_the_console)
  print('money is important in this game so earn when you have choices\n'.title())
  choice_4()

#playerchoice4 go to work and earn money
def choice_4():
 while True:
  player_choice4=input('IF YOU WANT TO GO TO WORK PRESS "y"\n IF YOU WANT TO SLEEP PRESS "n"')
  if player_choice4.lower()=='y':
    print('you earned $500 in the work\n')
    print('after the work you return to home and slept well')
    print('')
    global money
    money+=500
    break
  elif player_choice4.lower()=='n':
    print('you decided to sleep it will affect the future progress')
    break
  else:
    print('invalid input')
start()
print('everyday $100 deducted from your account for rent')
print('')
money-=100
print('')
print('DAY-2'.center(20,'*'))
print('REMAINING MONEY:'+str(money))
story_line_day_2=[
  (player_name,'hahhh another morning'),
  (':','some morining i will think that why am waking up in the morning , like why i existing and what the purpose me existing in the world'),
  (':','enough of my thoughts i have get ready for the school'),
  (':''today i wake up early in the morning'),
  (':''i start to cooking for my sister'),
  (':','today\'s dish is omurice her fav '),
  (':','little bit of this and little bit of that'),
  (':','omurice is ready!!!!🍝'),
  (player_name,'hotaru!!!! wake up !!!! breakfast is ready come and eat'),
  (player_name,'HOTARRRRUUU!!!!!!'),
  ('hotaru','don\'t shout am comming'),
  (player_name,'here eat while its hot'),
  ('hotaru','lets dig it in !!!!!!'),
  (':','while she is eating ,i decide to ready of the school'),
  (':','brushed ,bathed,fit check,everything is perfect'),
  (':','hotaru also ready to depart to school'),
  (player_name,'bye hotaru go to school safely'),
  (':','van picked her up'),
  (":",'am also on my way to the school sameway as tommorow'),
  (":",'in the bus stop yoimiya is there')
]
show_scene(story_line_day_2)

