import random

questions=['Which god is also known as ‘Gauri Nandan’?',
           'What does not grow on tree according to a popular Hindi saying?',
           'Which city is known as Pink City in India?',
           "Who wrote India's National Anthem?",
           'How many major religions are there in India?',
           'When is the National Hindi Diwas celebrated?',
           'What is the name of the game developer ?',
           'How many states are there in India?',
           'Where in India Gate located?',
           'Who wrote Vande Mataram?',
           'Which one of the following places is famous for the Great Vishnu Temple?',
           'Which Indian monument was originally built as a victory tower to commemorate the defeat of the Khan of Khambhat?',
           "Who among the following was killed during 'Operation Bluestar' of 1984?",
           'Which former Indian President died as a result of a road accident?',
           'Who is the founder of the political party Dravida Munnetra Kazhagam (DMK)?',
           'Who was the first Indian woman to win a medal in the Olympics?']
options=[['A.Agni','B.Indra','C.Hanuman','D.Ganesha'],
         ['A.Money','B.Flowers','C.Leaves','D.Fruits'],
         ['A.Banglore','B.Maysore','C.Jaipur','D.Kochi'],
         ['A.Rabindranath Tagore','B.Lal Bahadur Shastri','C.Chetan Bhagat','D.RK Narayan'],
         ['A.6','B.7','C.8','D.9'],
         ['A.13 September','B.14 September','C.14 July','D.15 August'],
         ['A.Adarsh','B.Aakarsh','C.Aakash','D.Akash'],
         ['A.28','B.29','C.31','D.31'],
         ['A.Agra','B.Punjab','C.Mumbai','D.New Delhi'],
         ['A.Sarat Chandra Chattopadhyay','B.Rabindranath Tagore','C.Bankim Chandra Chatterjee','D.Ishwar Chandra Vidyasagar'],
         ['A.Bordubar, Indonesia','B.Bamiyan, Afghanistan','C.Panja Sahib, Pakistan','D.Ankorvat, Cambodia'],
         ['A.Qutub Minar','B.India Gate','C.Charminar','D.Vijay Stambha'],
         ['A.Baba Santa Singh','B.Haji Mastan','C.Jarnail Singh Bhindrawale','D.Homi Jehangir Bhabha'],
         ['A.Rajendra Prasad','B.Faqruddin Ali Ahmed','C.Giani Zail Singh','D.R.Venkatraman'],
         ['A.C.N. Annadurai','B.M. Karunanidhi','C.M.G. Ramachandran','D.Jayalalitha'],
         ['A.P.T. Usha','B.Kunjarani Devi','C.Bachendri Pal','D.Karnam Maleshwari']]
options50=[['A.Agni','B.','C.','D.Ganesha'],
         ['A.Money','B.','C.Leaves','D.'],
         ['A.','B.Maysore','C.Jaipur','D.'],
         ['A.Rabindranath Tagore','B.','C.Chetan Bhagat','D.'],
         ['A.6','B.7','C.','D.'],
         ['A.','B.14 September','C.','D.15 August'],
         ['A.','B.Aakarsh','C.Aakash','D.'],
         ['A.28','B.','C.','D.31'],
         ['A.','B.','C.Mumbai','D.New Delhi'],
         ['A.','B.Rabindranath Tagore','C.Bankim Chandra Chatterjee','D.'],
         ['A.Bordubar, Indonesia','B.','C.','D.Ankorvat, Cambodia'],
         ['A.','B.India Gate','C.','D.Vijay Stambha'],
         ['A.Baba Santa Singh','B.','C.Jarnail Singh Bhindrawale','D.'],
         ['A.Rajendra Prasad','B.','C.Giani Zail Singh','D.'],
         ['A.C.N. Annadurai','B.','C.','D.Jayalalitha'],
         ['A.','B.','C.Bachendri Pal','D.Karnam Maleshwari']]
answers=['D','A','C','A','A','B','B','A','D','C','D','D','C','C','A','D']
money=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
lifeline=['a.50:50','b.flip the question']

combined=list(zip(questions,options,options50,answers))
random.shuffle(combined)
questions,options,options50,answers=zip(*combined)
questions=list(questions)
options=list(options)
options50=list(options50)
answers=list(answers)

def Answer():
    print()
    answer=input('Enter your option or enter 0 to take a lifeline or enter "quit" to end the game.').upper()
    if answer==answers[i]:
        print('Your answer is correct.')
        print('Your current prize money :',money[i])
        print()
    elif answer=='QUIT':
        if i==0:
            print('Your winning prize money :',0)
        else:
            print('Your winning prize money :',money[i-1])
        return 0
    elif answer=='0':
        return 'L'
    else:
        print('Your answer is wrong.')
        if i in range(5):
            print('Your winning prize money :',0)
        elif i in range(5,10):
            print('Your winning prize money :',10000)
        elif i in range(10,15):
            print('Your winning prize money :',320000)
        return 0

def Lifeline():
    print()
    if len(lifeline)==2:
        print('You have 2 lifelines.')
        for k in lifeline:
            print(f'{k}')
        l1=input('Enter a or b to choose a lifeline from above :').lower()
        if l1=='a':
            f=fifty()
            if f==0:
                return 'break'
            elif f=='L':
                return 'l2'
        elif l1=='b':
            print()
            lifeline.pop(1)
            return 'continue'
    elif len(lifeline)==1:
        print('Since you are left with only one lifeline we will use it.')
        if 'a.50:50' in lifeline:
            f1=fifty()
            if f1==0:
                return 'break'
            elif f1=='L':
                return 'l2'
        elif 'b.flip the question' in lifeline:
            return 'continue'
    elif len(lifeline)==0:
        print('No lifeline remaining.')
        return 'nlr'

def fifty():
    lifeline.pop(0)
    print(f'{questions[i]}')
    for m in options50[i]:
        print(f'{m}')
    a1=Answer()
    return a1

i=0
while i<15:
    x=0
    print(f'{questions[i]}')
    for j in options[i]:
        print(f'{j}')
    a=Answer()
    if a==0:
        break
    elif a=='L':
        while True:
            l=Lifeline()
            if l=='nlr':
                i-=1
                break
            elif l=='break':
                x=1
                break
            elif l=='continue':
                break
    if x==1:
        break
    i+=1