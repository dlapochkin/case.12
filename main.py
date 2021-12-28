import os
import tkinter
from PIL import ImageTk, Image


def parameters():
    """
    The function sets password and account parameters.
    """
    print('Для работы программы требуется ввести следующие параметры:')
    password = isPassword(input('PIN-код    '))
    account = isAccount(input('Баланс карты    $'))
    return password, int(account)


def isPassword(password):
    """
    The function checks whether a password string meets a requirements.
    password: str, password
    """
    if len(password) == 4:
        valid = True
        for i in range(4):
            if password[i] not in '0123456789':
                valid = False
        if valid:
            return password
    print('PIN-код должен состоять из четырех цифр. Пожалуйста, повторите попытку.')
    password = input('PIN-код    ')
    return isPassword(password)


def isAccount(account):
    """
    The function checks whether a account string meets a requirements.
    account: str, account
    """
    if 1 <= len(account) <= 5:
        valid = True
        for i in range(len(account)):
            if account[i] not in '0123456789':
                valid = False
        if valid and int(account) > 0:
            return account
    print('Баланс должен быть больше нуля и содержать лишь цифры. Пожалуйста, повторите попытку.')
    account = input('Баланс карты    $')
    return isAccount(account)


def isNumber(value):
    """
    The function checks whether value string is number.
    value: str, value
    """
    for i in range(len(value)):
        if value[i] not in '0123456789':
            return False
    if str(int(value)) != value:
        return False
    return True


def beginningPage():
    """
    The function represents an initial state of ATM at launch
    """
    inquiry.set('')
    buttonUpper.configure(state='disabled')
    buttonLower.configure(state='disabled')
    moneyReturnerObj.configure(state='disabled')
    moneyReceiverObj.configure(state='disabled')
    textFirst.grid_forget()
    textSecond.grid_forget()
    passwordEntry.grid_forget()
    optionFirst.grid_forget()
    optionSecond.grid_forget()
    textFirst.configure(text='Вставьте карту')
    textFirst.grid(row=4, column=2, columnspan=8, sticky='N')


def passwordPage():
    """
    The function represents the page with password entry.
    """
    inquiry.set('')
    passwordEntry.configure(show='*')
    textFirst.grid_forget()
    textFirst.configure(text='Введите PIN-код:')
    textFirst.grid(row=3, column=2, columnspan=8, sticky='S')
    passwordEntry.grid(row=4, column=2, columnspan=8)


def choicePage():
    """
    The function represents the page with option choice.
    """
    global account
    cardReceiverObj.configure(state='normal')
    moneyReturnerObj.configure(state='disabled')
    moneyReceiverObj.configure(state='disabled')
    inquiry.set('')
    passwordEntry.grid_forget()
    textFirst.grid_forget()
    textFirst.configure(text='Баланс\n$'+str(account))
    textFirst.grid(row=3, column=2, columnspan=8, rowspan=3, sticky='W')
    optionFirst.grid(row=3, column=4, columnspan=5, sticky='SE')
    optionSecond.grid(row=4, column=4, columnspan=5, sticky='SE')
    buttonUpper.configure(state='normal')
    buttonLower.configure(state='normal')


def cashWithdrawalPage():
    """
    The function represents the cash withdrawal page after choice was made.
    """
    global inquiry, choiceIs
    choiceIs = 'cashWithdrawalPage'
    buttonUpper.configure(state='disabled')
    buttonLower.configure(state='disabled')
    inquiry.set('')
    textFirst.grid_forget()
    textFirst.configure(text='Баланс\n$'+str(account))
    textFirst.grid(row=3, column=2, columnspan=8, rowspan=3, sticky='W')
    optionFirst.grid_forget()
    optionSecond.grid_forget()
    textSecond.grid(row=3, column=4, rowspan=2, columnspan=5, sticky='E')
    passwordEntry.configure(show='')
    passwordEntry.grid(row=4, column=4, columnspan=6, sticky='S')


def refillPage():
    """
    The function represents the refill page after choice was made.
    """
    global inquiry, choiceIs
    choiceIs = 'refillPage'
    buttonUpper.configure(state='disabled')
    buttonLower.configure(state='disabled')
    inquiry.set('')
    textFirst.grid_forget()
    textFirst.configure(text='Баланс\n$'+str(account))
    textFirst.grid(row=3, column=2, columnspan=8, rowspan=3, sticky='W')
    optionFirst.grid_forget()
    optionSecond.grid_forget()
    textSecond.grid(row=3, column=4, rowspan=2, columnspan=5, sticky='E')
    passwordEntry.configure(show='')
    passwordEntry.grid(row=4, column=4, columnspan=6, sticky='S')
        


def oneClick():
    """
    The function changes input field value.
    """
    inquiry.set(inquiry.get()+'1')


def twoClick():
    """
    The function changes input field value.
    """
    inquiry.set(inquiry.get()+'2')


def threeClick():
    """
    The function changes input field value.
    """
    inquiry.set(inquiry.get()+'3')


def fourClick():
    """
    The function changes input field value.
    """
    inquiry.set(inquiry.get()+'4')


def fiveClick():
    """
    The function changes input field value.
    """
    inquiry.set(str(inquiry.get())+'5')


def sixClick():
    """
    The function changes input field value.
    """
    inquiry.set(str(inquiry.get())+'6')


def sevenClick():
    """
    The function changes input field value.
    """
    inquiry.set(str(inquiry.get())+'7')


def eightClick():
    """
    The function changes input field value.
    """
    inquiry.set(str(inquiry.get())+'8')


def nineClick():
    """
    The function changes input field value.
    """
    inquiry.set(str(inquiry.get())+'9')


def zeroClick():
    """
    The function changes input field value.
    """
    inquiry.set(str(inquiry.get())+'0')


def clearClick():
    """
    The function changes input field value.
    """
    inquiry.set(inquiry.get()[:-1])


def okEntry():
    """
    The function checks input field value and addressing to page if the value is coorect.
    """
    global password, account, choiceIs
    textFirst.grid_forget()
    passwordEntry.grid_forget()
    textSecond.grid_forget()
    if choiceIs:
        if isNumber(inquiry.get()):
            if choiceIs == 'cashWithdrawalPage':
                choiceIs = None
                if int(inquiry.get()) <= account:
                    account -= int(inquiry.get())
                    choiceIs = None
                    cardReceiverObj.configure(state='disabled')
                    moneyReturnerObj.configure(state='normal')
                    textFirst.configure(text='Произошло списание\n$'+inquiry.get()+'\nВозьмите наличные')
                    textFirst.grid(row=3, column=2, columnspan=8, rowspan=3)
                else:
                    textFirst.configure(text='На балансе\nнедостаточно средств')
                    textFirst.grid(row=3, column=2, columnspan=8, rowspan=2)
                    root.after(3000, cashWithdrawalPage)
            else:
                if int(inquiry.get()) <= 1000:
                    choiceIs = False
                    moneyReceiverObj.configure(state='normal')
                    textFirst.configure(text='Для продолжения\nвведите $'+inquiry.get())
                    textFirst.grid(row=3, column=2, columnspan=8, rowspan=3)
                else:
                    textFirst.configure(text='Возможно внести\nне более, чем\n$1000 за транзакцию')
                    textFirst.grid(row=3, column=2, columnspan=8, rowspan=3)
                    root.after(3000, refillPage)
        else:
            textFirst.configure(text='Введено некорректное\nзначение')
            textFirst.grid(row=3, column=2, columnspan=8, rowspan=2)
            root.after(3000, cashWithdrawalPage)
    else:
        if password == inquiry.get():
            choicePage()
        else:
            textFirst.configure(text='Введен неверный\nPIN-код')
            textFirst.grid(row=3, column=2, columnspan=8, rowspan=2)
            root.after(3000, passwordPage)



def cardInsert():
    """
    The function represents card insert animation.
    """
    global cardIn, cardFrame
    if cardIn:
        if cardFrame > 1:
            cardFrame -= 1
            background = ImageTk.PhotoImage(Image.open(os.path.abspath('assets\\CardFrame'+str(cardFrame)+'.png')))
            backgroundObj.configure(image=background)
            backgroundObj.image = background
            root.after(70, cardInsert)
        else:
            background = ImageTk.PhotoImage(Image.open(os.path.abspath('assets\\background.png')))
            backgroundObj.configure(image=background)
            backgroundObj.image = background
            cardIn = False
            beginningPage()
    else:
        if cardFrame < 10:
            cardFrame += 1
            background = ImageTk.PhotoImage(Image.open(os.path.abspath('assets\\CardFrame'+str(cardFrame)+'.png')))
            backgroundObj.configure(image=background)
            backgroundObj.image = background
            root.after(70, cardInsert)
        else:
            background = ImageTk.PhotoImage(Image.open(os.path.abspath('assets\\background.png')))
            backgroundObj.configure(image=background)
            backgroundObj.image = background
            cardIn = True
            passwordPage()


def moneyOut():
    """
    The function represents money withdrawal animation.
    """
    global moneyOutFrame
    if moneyOutFrame < 7:
        moneyOutFrame += 1
        background = ImageTk.PhotoImage(Image.open(os.path.abspath('assets\\MoneyOutFrame'+str(moneyOutFrame)+'.png')))
        backgroundObj.configure(image=background)
        backgroundObj.image = background
        root.after(70, moneyOut)
    else:
        background = ImageTk.PhotoImage(Image.open(os.path.abspath('assets\\background.png')))
        backgroundObj.configure(image=background)
        backgroundObj.image = background
        moneyOutFrame = 0
        choicePage()


def moneyIn():
    """
    The function represents money input animation.
    """
    global moneyInFrame, account
    cardReceiverObj.configure(state='disabled')
    if moneyInFrame < 13:
        moneyInFrame += 1
        background = ImageTk.PhotoImage(Image.open(os.path.abspath('assets\\MoneyInFrame'+str(moneyInFrame)+'.png')))
        backgroundObj.configure(image=background)
        backgroundObj.image = background
        root.after(70, moneyIn)
    else:
        account += int(inquiry.get())
        background = ImageTk.PhotoImage(Image.open(os.path.abspath('assets\\background.png')))
        backgroundObj.configure(image=background)
        backgroundObj.image = background
        moneyInFrame = 0
        cardReceiverObj.configure(state='normal')
        choicePage()


password, account = parameters()
cardIn = False
choiceIs = None
cardFrame = 0
moneyOutFrame = 0
moneyInFrame = 0

root = tkinter.Tk()
root.title('ATM')

inquiry = tkinter.StringVar()

# Icons block
background = ImageTk.PhotoImage(Image.open(os.path.abspath('assets\\background.png')))
screen = ImageTk.PhotoImage(Image.open(os.path.abspath('assets\\screen.png')))
button = ImageTk.PhotoImage(Image.open(os.path.abspath('assets\\button.png')))
cardReceiver = ImageTk.PhotoImage(Image.open(os.path.abspath('assets\\cardReceiver.png')))
moneyReceiver = ImageTk.PhotoImage(Image.open(os.path.abspath('assets\\moneyReceiver.png')))
moneyReturner = ImageTk.PhotoImage(Image.open(os.path.abspath('assets\\moneyReturner.png')))
one = ImageTk.PhotoImage(Image.open(os.path.abspath('assets\\one.png')))
two = ImageTk.PhotoImage(Image.open(os.path.abspath('assets\\two.png')))
three = ImageTk.PhotoImage(Image.open(os.path.abspath('assets\\three.png')))
four = ImageTk.PhotoImage(Image.open(os.path.abspath('assets\\four.png')))
five = ImageTk.PhotoImage(Image.open(os.path.abspath('assets\\five.png')))
six = ImageTk.PhotoImage(Image.open(os.path.abspath('assets\\six.png')))
seven = ImageTk.PhotoImage(Image.open(os.path.abspath('assets\\seven.png')))
eight = ImageTk.PhotoImage(Image.open(os.path.abspath('assets\\eight.png')))
nine = ImageTk.PhotoImage(Image.open(os.path.abspath('assets\\nine.png')))
zero = ImageTk.PhotoImage(Image.open(os.path.abspath('assets\\zero.png')))
ok = ImageTk.PhotoImage(Image.open(os.path.abspath('assets\\ok.png')))
clear = ImageTk.PhotoImage(Image.open(os.path.abspath('assets\\clear.png')))

# Objects block
backgroundObj = tkinter.Label(root, image=background)
screenObj = tkinter.Label(root, image=screen)
buttonUpper = tkinter.Button(root, bg='#ffe082', image=button, command=cashWithdrawalPage)
buttonLower = tkinter.Button(root, bg='#ffe082', image=button, command=refillPage)
cardReceiverObj = tkinter.Button(root, bg='#ffe082', image=cardReceiver, command=cardInsert)
moneyReceiverObj = tkinter.Button(root, bg='#ffe082', image=moneyReceiver, command=moneyIn)
moneyReturnerObj = tkinter.Button(root, bg='#c5e1a5', image=moneyReturner, command=moneyOut)
oneBtn = tkinter.Button(root, bg='#e8f5e9', image=one, command=oneClick)
twoBtn = tkinter.Button(root, bg='#e8f5e9', image=two, command=twoClick)
threeBtn = tkinter.Button(root, bg='#e8f5e9', image=three, command=threeClick)
fourBtn = tkinter.Button(root, bg='#e8f5e9', image=four, command=fourClick)
fiveBtn = tkinter.Button(root, bg='#e8f5e9', image=five, command=fiveClick)
sixBtn = tkinter.Button(root, bg='#e8f5e9', image=six, command=sixClick)
sevenBtn = tkinter.Button(root, bg='#e8f5e9', image=seven, command=sevenClick)
eightBtn = tkinter.Button(root, bg='#e8f5e9', image=eight, command=eightClick)
nineBtn = tkinter.Button(root, bg='#e8f5e9', image=nine, command=nineClick)
zeroBtn = tkinter.Button(root, bg='#e8f5e9', image=zero, command=zeroClick)
okBtn = tkinter.Button(root, bg='#e8f5e9', image=ok, command=okEntry)
clearBtn = tkinter.Button(root, bg='#e8f5e9', image=clear, command=clearClick)
textFirst = tkinter.Label(root, font=('Arial', 19), text='Вставьте карту', bg='#e8f5e9')
textSecond = tkinter.Label(root, font=('Arial', 16), text='Введите нужную\nсумму:', bg='#e8f5e9')
optionFirst = tkinter.Label(root, font=('Arial', 16), text='Снять наличные', bg='#e8f5e9')
optionSecond = tkinter.Label(root, font=('Arial', 16), text='Пополнить счет', bg='#e8f5e9')
passwordEntry = tkinter.Entry(root, show='*', textvariable=inquiry)

# Pre-grids
backgroundObj.grid(row=0, column=0, rowspan=20, columnspan=14)
screenObj.grid(row=3, column=15, rowspan=14, columnspan=14)
buttonUpper.grid(row=3, column=10, columnspan=3, sticky='S')
buttonLower.grid(row=4, column=10, columnspan=3, sticky='S')
cardReceiverObj.grid(row=7, column=8, rowspan=2, columnspan=5, sticky='W')
moneyReceiverObj.grid(row=7, column=2, rowspan=2, columnspan=5, sticky='W')
moneyReturnerObj.grid(row=13, column=2, rowspan=2, columnspan=8, sticky='E')
oneBtn.grid(row=6, column=17, rowspan=2, columnspan=2)
twoBtn.grid(row=6, column=19, rowspan=2, columnspan=2)
threeBtn.grid(row=6, column=21, rowspan=2, columnspan=2)
fourBtn.grid(row=8, column=17, rowspan=2, columnspan=2)
fiveBtn.grid(row=8, column=19, rowspan=2, columnspan=2)
sixBtn.grid(row=8, column=21, rowspan=2, columnspan=2)
sevenBtn.grid(row=10, column=17, rowspan=2, columnspan=2)
eightBtn.grid(row=10, column=19, rowspan=2, columnspan=2)
nineBtn.grid(row=10, column=21, rowspan=2, columnspan=2)
zeroBtn.grid(row=10, column=25, rowspan=2, columnspan=2)
okBtn.grid(row=6, column=25, rowspan=2, columnspan=2)
clearBtn.grid(row=8, column=25, rowspan=2, columnspan=2)

beginningPage()
root.mainloop()