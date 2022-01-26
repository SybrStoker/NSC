#practice_work.py
#created by Dan, isp-11
#It translates numbers from one numeral system to another

#************************************************************************************#
#WARNING! READ ME PLEASE                                                             #
#THIS PROGRAM WILL WORK ONLY ON PYHON 3.10 V, IF YOUR PY V IS BELOW THAT PLS UPDATE  #
#COUSE I'VE USED NEW FUN IN THIS UPDATE MATCH(SWITCH FOR FOLK)                       #
#WARNING! READ ME PLEASE                                                             #
#************************************************************************************#
from prettytable import PrettyTable
__version__ = '6.7' #needed to be tested and finished

class MaxInputError(Exception):
    '''Tell to user that he wrote a so big number to get over with'''
    def __init__(self, length, maxValue):
        Exception.__init__(self)
        self.length = length
        self.maxValue = maxValue

class EmptyInputError(Exception):
    '''Tell to user that he wrote nothing or it's too small '''
    def __init__(self, length):
        Exception.__init__(self)
        self.length = length

class en:
    '''Gives English replies '''
    def info(self):
        return '''
        Programm translates numbers from one numeral system to another
        Enter number of wished choice to make the right desision.
        1.Translate number from another numeral sys to 10 NS
        *At first enter num in another NS, then NS of that num*
        2.Translate number from 10 numeral sys to another
        *At firs enter num in 10 NS, then NS of sought num*
        3.Do any operation with NS, such as plus, minus, devision, multiply.
        4.Table with step
        *Enter first number, then the system of it. We'll pluss step which you enter to the first num
        untill some number you will enter too in the same NS as first number.*
        5.Exit
        '''

    def info2(self):
        return "Enter the number which y'd like to translate:"

    def info3(self):
        return "Value of expression is "

    def enter(self):
        return "Enter here --> "

    def typeSys(self):
        return "Enter the type of numeral system:"

    def error(self):
        return "Wrong number"

    def zeroE(self):
        return "You can't use zero"

    def finished(self):
        return "Press Enter to finish"

    def operatorChoice(self):
        return "Enter the operator to act(+|-|/|*)"

    def wrongSys(self):
        return "You have enterd the wrong NS, cause one of your numbers is bigger than your NS"

    def sysOutput(self):
        return "Enter the NS which the result must be in"

    def addNS(self):
        return """Add as many numeral system as you need.
                  (you must add at least 1)"""

    def addMore(self):
        return "To add more, just write '+'. But if you wanna finish pess any key"

    def limit(self):
        return "Enter the number as the end point of reaching the result"

    def firstNumber(self):
        return "Enter a first number"

    def secondNumber(self):
        return "Enter a second number"

    def step(self):
        return "Enter a step(number is in 10 numeral system)"
class ru:
    '''Gives Russian replies'''
    def info(self):
        return '''
        Программа переводит цифры из одной системы счисления в другую
        Введите желаемое число вашего выбора, чтобы сделать правильное решение.
        1.Перевести число из одной системы исчисления в десятичную
        *Сначала вводим число в другой СИ, а потом его СИ*
        2.Перевести число из десятичной системы исчисления в другую
        *Сначала вводим число в 10  СИ, а потом СИ искомого числа*
        3.Делать любые операции с СИ, такие как +,-,*,/.
        4.Построение таблицы с шагом
        *Введите первое число, тогда систему этого числа. Мы прибавим шаг, который
        вы введете к первому числу, до введенного предела в той же СИ, как и первое число.*
        3.Выход
        '''

    def info2(self):
        return "Напишите какое число вы бы хотели перевести:"

    def info3(self):
        return "Значение выражения - "

    def enter(self):
        return "Напишите тут --> "

    def typeSys(self):
        return "Напишите тип системы счисления:"

    def error(self):
        return "Непривильное число"

    def zeroE(self):
        return "Вы не можете использовать 0"

    def finished(self):
        return "Нажмите Enter, чтобы выйти"

    def operatorChoice(self):
        return "Введите оператор, чтобы начать действие(+|-|/|*)"

    def wrongSys(self):
        return "Вы ввели неправильное число, т.к. оно больше СИ"

    def sysOutput(self):
        return "Введите СИ в которой должен быть ответ"

    def addNS(self):
        return """Add as many numeral system as you need.
                  (you must add at least 1)"""

    def addMore(self):
        return "To add more, just write '+'. But if you wanna finish pess any key"

    def limit(self):
        return "Введите число до которого нужно считать."

    def firstNumber(self):
        return "Введите первое число"

    def secondNumber(self):
        return "Введите второе число"

    def step(self):
        return "Введите шаг(чмсло в 10 СИ)"

class examination:
    '''Exam how did user write the needed answer'''
    acceptedLettersInUppercase = ('A', 'B', 'C', 'D', 'E', 'F')
    acceptedLettersInLowercase = ('a', 'b', 'c', 'd', 'e', 'f')
    acceptedLetters = ('A', 'B', 'C', 'D', 'E', 'F',\
                       'a', 'b', 'c', 'd', 'e', 'f')

    ALLC = ('a', 'b', 'c', 'd', 'e', 'f') #acceptedLettersLowercase

    acceptedNumbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

    acceptedSigns   = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',\
                       'A', 'B', 'C', 'D', 'E', 'F',\
                       'a', 'b', 'c', 'd', 'e', 'f')

    temp = 0      #this is here to give some value from class to the main block
    successes = 0 #counter of successes iterations
    ctr = 0       #counter of all iterations
    listEx = []   #to every method could use it(listExamination)

    def zeroMethod(self, s):
        '''Split up the string to make work more easiest

            Actually this method need to make listEx empty when one of iterations was fialed as well'''
        examination.listEx = []

        #examination.listEx.append(list(s))
        for i in range(0, len(s)):
            examination.listEx.append(s[i])

    def checkMistakes(self, position):
        '''Find accepted  signs in the user's input to put down ability of making mistakes'''
        examination.ctr +=1
        value = examination.listEx[position]

        if value in examination.acceptedSigns:
            examination.successes += 1

            #if user wrote 16 NS translate it to normal numbers
            if value in examination.acceptedLetters:

                #lowercase
                if value in examination.ALLC:
                    examination.listEx.insert(examination.listEx.index(value), self.translate(value.upper()))
                    examination.listEx.pop(examination.listEx.index(value))

                #uppercase
                else:
                    examination.listEx.insert(examination.listEx.index(value), self.translate(value))
                    examination.listEx.pop(examination.listEx.index(value))

        else:
            print(value, "is not the accepted part")

    def successesFun(self):
        '''check out did make user any mistakes'''
        if examination.ctr == examination.successes:
            return 0
        else:
            examination.ctr = 0
            examination.successes = 0

    def translate(self, letter):
        '''Translate letter from 16 num sys to numbers

        We have trouble with 16 numeral system couse A or F aren't numbers
        therefore we need to translate it to the normal integer number.'''

        #we're trying to face our inputed letter with the array where all characters on their own places
        #and with every time it will take the exactly needed number A = 10, B = 11...
        ctr = 9
        for i in examination.acceptedLettersInUppercase:
            ctr += 1
            if letter == i:
                break
        return ctr

    def translateBack(self, num):
        '''Translate numbers to 16 NS when num is more than 9 and up to 15

        We have trouble with 16 numeral system couse A or F aren't numbers
        therefore we need to translate numbers to letter for user'''

        # we're trying to face our inputed number with the array where all characters on their own places
        # and with every time it will take the exactly needed number 10 = A, 11 = B...
        ctr = 9
        for i in examination.acceptedLettersInUppercase:
            ctr += 1
            if num == ctr:
                break
        return i

    def testInput(self, typeInput = 0):
        '''exam how had user entered some value'''
        try:
            if typeInput == 0:
                integerN = False
                examination.temp = input()

                if len(examination.temp) > 2147483647:
                    raise MaxInputError (len(examination.temp), 2147483647)

                elif len(examination.temp) == ' ' or len(examination.temp) == '\n' or len(examination.temp) == 0:
                    raise EmptyInputError(0)

            elif typeInput == 1:
                integerN = True
                examination.temp = int(input())

                if examination.temp > 2147483647:
                    raise MaxInputError (examination.temp, 2147483647)

                if examination.temp == ' ' or examination.temp == '\n':
                    raise EmptyInputError(0)

        except ValueError:
            print(lan.error())
            if integerN == False:
                self.testInput()
            else:
                self.testInput(typeInput == 1)

        except EOFError:
            print("What the... alright, alright. BUT WHY DUDE? WHY DID YOU THAT? ")
            print("Зачем? Просто зачем? ")
            self.testInput()

        except MaxInputError as MIE:
            print(f"You wrote {MIE.length} symbols, it's beyond the limit - {MIE.maxValue}")
            print(f"Ты написал {MIE.length} сиволов, это превышает лимит  - {MIE.maxValue}")
            self.testInput()

        except EmptyInputError as EIE:
            print(f"Hey, you wrote nothing, it's {EIE.length} symbols. You gotta write 1 or more symbols")
            print(f"Эм, ты ничего не написал, тут {EIE.length} символов. Ты должен написать 1 или больше.")
            self.testInput()

try1 = examination()
def cleaner():
    """safety input a number as a string after that translate it to the numbers

    Needed to use NS above 9, like 16 NS"""

    global number

    #trying find any mistake a user could do#
    while True:
        try1.testInput()
        s = examination.temp

        try1.zeroMethod(s)#give the string to the class to have an ability making some mistakes
        for i in range(0, len(s)):
            #exam every character of string to find mistakes
            try1.checkMistakes(i)

        if try1.successesFun() == 0:
            #if here is no mistakes then we go out the cycle
            number = examination.listEx
            break

def sysemValue():
    """enter the NS"""

    global system
    while True:
        try1.testInput(typeInput = 1)
        system = examination.temp

        #exam sys for 0#
        #we can't have the 0 NS
        if system == 0:
            print(lan.zeroE())
            continue
        else:
            break


def NStoTen(number, system):
    """translate the list of numbers from any NS to 10 NS"""

    global totalT

    number.reverse()
    totalT = 0
    for i in range (0, len(number)):
        temp  = pow(system, i) * int(number[i])
        totalT += temp

def tenToNS(number,system):
    global list2
    #translation#

    list2 = []
    whileBlock = False
    while number >= system:
        whileBlock = True
        list2.append(int(number % system))
        number /= system

        if number < system:
            list2.append(int(number % system))

    if whileBlock == False:
        #say that num is less than NS
        if number >= 10 and number < 16 and\
           system > 10 and system <= 16:
           list2.append(try1.translateBack(number))

    #exam list for 16 NS parts#
    list2.reverse()

    if system >= 10:
        num16 = (10, 11, 12, 13, 14, 15)
        for i in num16:
            for j in range(0, len(list2)):
                if list2[j] == i:
                    list2.insert(list2.index(list2[j]), try1.translateBack(list2[j]))
                    list2.pop(list2.index(list2[j + 1]))

def fullWork(have = 0):
    """take the number in any NS and then exam and translate to 10 NS"""
    global number
    global system

    while True:
        cleaner()

        #to except situation where we've known which system we'd need
        if have == 0:
            print(lan.typeSys())
            sysemValue()
        else:
            system = have

        mistake = False
        for i in number:
            if int(i) >= system:
                print(lan.wrongSys())
                mistake = True
                break
        if mistake == True:
            continue
        else:
            NStoTen(number,system)
            break

class operations():
    valueButList = []

    def sum(self, number1, number2):
        global system
        global list2

        value = number1 + number2

        #prepear for output
        print(lan.sysOutput())
        sysemValue()
        tenToNS(value, system)

        operations.valueButList = list2

    def minus(self, number1, number2):
        global system
        global list2

        value = number1 - number2

        #prepear for output
        print(lan.sysOutput())
        sysemValue()
        tenToNS(value, system)

        operations.valueButList = list2

    def multiply(self, number1, number2):
        global system
        global list2

        value = number1 * number2

        #prepear for output
        print(lan.sysOutput())
        sysemValue()
        tenToNS(value, system)

        operations.valueButList = list2

    def devision(self, number1, number2):
        global system
        global list2

        value = number1 / number2

        #prepear for output
        print(lan.sysOutput())
        sysemValue()
        tenToNS(value, system)

        operations.valueButList = list2
act = operations()
#***
#CHOOSE LANGUAGE
#***
print('''
Sup,you gotta choose the language to keep on running.(en)
Just enter en

Привет, выбери нужный тебе язык.(ru)
Просто введи ru
''')

while True:
    #test input#
    tempObject = examination()
    tempObject.testInput()
    language = examination.temp

    #set up the language settings#
    #it doesn't matter which one user will pick
    #couse we'll set the same object's name and method for every of 'em
    match language:
        case ('en'|'EN'|'En'|'eN'):
            lanEn = en()
            lan = lanEn
            break

        case ('ru'|'RU'|'Ru'|'rU'):
            lanRu = ru()
            lan = lanRu
            break

        case _:
            print("Oops!")

#***
#THE MAIN BLOCK
#***
while True:
    print(lan.info())
    #we have the second one cause we need to see info again

    while True:
        #test input#
        tempObject.testInput(typeInput = 1)
        key = examination.temp

        match key:

            #***
            #TRANSLATION FROM NS TO 10 NS
            #***
            case 1:
                #enter number#
                print(lan.info2())

                #trying find any mistake a user could do#
                cleaner()
                n1 = number

                #enter sys variable#
                print(lan.typeSys())
                sysemValue()
                sys = system

                #translation#
                NStoTen(n1, sys)

                #output#
                print(lan.info3(), totalT)

                #print(lan.finished())
                input(lan.finished())
                break

            #***
            #TRANSLATION FROM 10 NS TO ANOTHER NS
            #***
            case 2:
                #get number in 10 NS#
                print(lan.info2())
                try1.testInput(typeInput = 1)
                n1 = examination.temp

                #get numeral system#
                print(lan.typeSys())
                sysemValue()
                sys = system

                tenToNS(n1,sys)

                #output#
                print(lan.info3(), end="")
                for i in list2:
                    print(i, end="")
                print("\n")

                #clean data#
                input(lan.finished())
                break

            case 3:
                # enter first number#
                print(lan.firstNumber())
                fullWork()
                num1 = totalT


                # second number with the exam#
                print(lan.secondNumber())
                cleaner()
                num2 = number

                #enter sys variable for sec num
                print(lan.typeSys())
                try1.testInput(typeInput = 1)
                sys2 = examination.temp

                #translate the num to 10 NS
                NStoTen(number, sys2)
                num2 = totalT
                print(num2)
                type(num2)

                #chosing operators#
                while True:
                    print(lan.operatorChoice())
                    try1.testInput()
                    operatorChoice = examination.temp

                    match operatorChoice:
                        case '+':
                            act.sum(num1, num2)

                            #output#
                            print(lan.info3(), end="")
                            for i in operations.valueButList:
                                print(i, end="")
                            print("\n")
                            input(lan.finished())

                            break

                        case '-':
                            act.minus(num1, num2)

                            #output#
                            print(lan.info3(), end="")
                            for i in operations.valueButList:
                                print(i, end="")
                            print("\n")
                            input(lan.finished())

                            break

                        case '/':
                            act.devision(num1, num2)

                            #output#
                            print(lan.info3(), end="")
                            for i in operations.valueButList:
                                print(i, end="")
                            print("\n")
                            input(lan.finished())

                            break

                        case '*':
                            act.multiply(num1, num2)

                            #output#
                            print(lan.info3(), end="")
                            for i in operations.valueButList:
                                print(i, end="")
                            print("\n")
                            input(lan.finished())

                            break

                        case _:
                            print(lan.error())
                break
            case 4:
                #first number
                print(lan.firstNumber())
                fullWork()
                n1 = totalT
                sys = system

                #step#
                print(lan.step())
                fullWork(have = 10)
                step = totalT

                #limit of wolking forward#
                print(lan.limit())
                fullWork(have = sys)
                limit = totalT

                #action#
                table = PrettyTable()
                table.field_names = ["2", "8", "10", "16"]
                r1 = []
                sysList = (2,8,10,16)

                #output the started data
                for i in sysList:
                    #print('system', i)
                    tenToNS(n1,i)
                    string = []

                    for j in range(len(list2)):
                        s = str(list2[j])
                        #print("s is", s)
                        string.append(s)
                    r1.append(''.join(string))
                table.add_row(r1)

                #steping
                while n1 < limit - step:
                    r1 = []
                    n1 += step

                    for i in sysList:
                        tenToNS(n1,i)
                        string = []

                        for j in range(len(list2)):
                            s = str(list2[j])
                            string.append(s)
                        r1.append(''.join(string))
                    table.add_row(r1)


                print(table)
                input(lan.finished())
                break
            # ***
            # EXIT BLOCK
            # ***
            case  5:
                exit()

            case _:
                #if not found any able action
                print(lan.error())
