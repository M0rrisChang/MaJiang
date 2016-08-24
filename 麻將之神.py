# encoding: utf-8
from Tkinter import *

class MaJiang(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        self.ExistedPlayerCount = 0
        self.gamePlayed = 0
        self.playerMoney = [0, 0, 0, 0]
        self.loseCount = [0, 0, 0, 0]
        self.winCount = [0, 0, 0, 0]
        self.lastWinner = self.lastLoser = ""
    #    master.minsize(width=600, height=100)
    #    master.maxsize(width=600, height=100)

    def createWidgets(self):

        self.playerText = Label(self)
        self.playerText["text"] = "麻將鬥士一號："
        self.playerText.grid(row=0, column=0)
        self.playerField = Entry(self)
        self.playerField["width"] = 50
        self.playerField.grid(row=0, column=1, columnspan=6)


        self.playerConfirm = Button(self)
        self.playerConfirm["text"] = "參戰確定！"
        self.playerConfirm.grid(row=1, column=0, columnspan=7)
        self.playerConfirm["command"] = self.playerConfirmMethod
#        self.playerConfirm["command"] = lambda: self.playerConfirmMethod(self.ExistedPlayerCount)

        #press enter instead of click button
        self.playerField.bind('<Return>', lambda _: self.playerConfirmMethod())


        self.displayText = Label(self)
        self.displayText["text"] = "參賽者一號"
        self.displayText.grid(row=3, column=0, columnspan=7)





    #def playerConfirmMethod(self, ExistedPlayerCount):
    def playerConfirmMethod(self):
        #self.displayText["text"] = "賺大錢！"
        self.userinput = self.playerField.get()
        if self.userinput == "":
            self.displayText["text"] = "No input string!!"
        self.ExistedPlayerCount += 1
        self.playerField.delete(0, 'end')
        if self.ExistedPlayerCount == 1:
            self.player1 = self.userinput
            self.displayText["text"] = "參賽者二號"
            self.playerText["text"] = "麻將鬥士二號："
        elif self.ExistedPlayerCount == 2:
            self.player2 = self.userinput
            self.displayText["text"] = "參賽者三號"
            self.playerText["text"] = "麻將鬥士三號："
        elif self.ExistedPlayerCount == 3:
            self.player3 = self.userinput
            self.displayText["text"] = "參賽者四號"
            self.playerText["text"] = "麻將鬥士四號："
        elif self.ExistedPlayerCount > 3:
            self.player4 = self.userinput
            self.playerText.destroy()
            self.playerField.destroy()
            self.playerConfirm.destroy()
            self.gamingMethod()



    def gamingMethod(self):
        self.displayText["text"] = "決鬥吧"


        self.playerText1 = Label(self)
        self.playerText1["text"] = self.player1 #get player name
        self.playerText1.grid(row=0, column=0)
        self.playerField1 = Entry(self)
        self.playerField1["width"] = 6
        self.playerField1.grid(row=1, column=0)

        self.playerText2 = Label(self)
        self.playerText2["text"] = self.player2 #get player name
        self.playerText2.grid(row=0, column=1)
        self.playerField2 = Entry(self)
        self.playerField2["width"] = 6
        self.playerField2.grid(row=1, column=1)

        self.playerText3 = Label(self)
        self.playerText3["text"] = self.player3 #get player name
        self.playerText3.grid(row=0, column=2)
        self.playerField3 = Entry(self)
        self.playerField3["width"] = 6
        self.playerField3.grid(row=1, column=2)

        self.playerText4 = Label(self)
        self.playerText4["text"] = self.player4 #get player name
        self.playerText4.grid(row=0, column=3)
        self.playerField4 = Entry(self)
        self.playerField4["width"] = 6
        self.playerField4.grid(row=1, column=3)


        self.cash = Button(self)
        self.cash["text"] = "貪財貪財"
        self.cash.grid(row=2, column=0, columnspan=4)
        self.cash["command"] =  self.countMethod
        self.playerField4.bind('<Return>', lambda _: self.countMethod())

        self.end = Button(self)
        self.end["text"] = "結束了"
        self.end.grid(row=4, column=0, columnspan=4)
        self.end["command"] =  self.endMethod
        self.displayText.grid(row=3, column=0, columnspan=4)


        # TODO: autoCompletion
        '''
        while self.playerField1.get() == "" or self.playerField2.get() == "" or self.playerField3.get() == "" or self.playerField4.get() == "":
            if self.playerField1.get() != "" and self.playerField2.get() != "" and self.playerField3.get() != "":
                #1 2 3打ㄌ
                self.playerField4 = str(int(self.playerField1.get()) + int(self.playerField2.get()) + int(self.playerField3.get()))
            elif self.playerField1.get() != "" and self.playerField2.get() != "" and self.playerField4.get() != "":
                #1 2 4打ㄌ
                self.playerField3 = str(int(self.playerField1.get()) + int(self.playerField2.get()) + int(self.playerField4.get()))
            elif self.playerField1.get() != "" and self.playerField3.get() != "" and self.playerField4.get() != "":
                #1 3 4
                self.playerField2 = str(int(self.playerField1.get()) + int(self.playerField3.get()) + int(self.playerField4.get()))
            elif self.playerField2.get() != "" and self.playerField3.get() != "" and self.playerField4.get() != "":
                #2 3 4
                self.playerField1 = str(int(self.playerField2.get()) + int(self.playerField3.get()) + int(self.playerField4.get()))
        '''





    def countMethod(self):
        if int(self.playerField1.get()) + int(self.playerField2.get()) + int(self.playerField3.get()) + int(self.playerField4.get()) == 0:
            self.gamePlayed += 1
            self.displayText["text"] = "已經大戰 " + str(self.gamePlayed) + " 回合！"
            self.playerMoney[0] += int(self.playerField1.get())
            self.playerMoney[1] += int(self.playerField2.get())
            self.playerMoney[2] += int(self.playerField3.get())
            self.playerMoney[3] += int(self.playerField4.get())
            if int(self.playerField1.get()) > 0:
                currentWinner = self.player1
                self.winCount[0] += 1
            elif int(self.playerField1.get()) < 0:
                currentLoser = self.player1
                self.loseCount[0] += 1
            if int(self.playerField2.get()) > 0:
                currentWinner = self.player2
                self.winCount[1] += 1
            elif int(self.playerField2.get()) < 0:
                currentLoser = self.player2
                self.loseCount[1] += 1
            if int(self.playerField3.get()) > 0:
                currentWinner = self.player3
                self.winCount[2] += 1
            elif int(self.playerField3.get()) < 0:
                currentLoser = self.player3
                self.loseCount[2] += 1
            if int(self.playerField4.get()) > 0:
                currentWinner = self.player4
                self.winCount[3] += 1
            elif int(self.playerField4.get()) < 0:
                currentLoser = self.player4
                self.loseCount[3] += 1

            self.playerField1.delete(0, 'end')
            self.playerField2.delete(0, 'end')
            self.playerField3.delete(0, 'end')
            self.playerField4.delete(0, 'end')

            if currentWinner == self.lastWinner:
                print "Winner is " + currentWinner
                print "連莊！"
            else:
                print "世代交替！" + self.lastWinner + ">" + currentWinner
                self.lastWinner = currentWinner


        else:
            self.displayText["text"] = "麻將是零和賽局唷！"



    def endMethod(self):
        self.cash.destroy()
        self.end.destroy()
        self.displayText.destroy()
        self.playerField1.destroy()
        self.playerField2.destroy()
        self.playerField3.destroy()
        self.playerField4.destroy()

        self.moneyText1 = Label(self)
        self.moneyText1["text"] = str(self.playerMoney[0])
        self.moneyText1.grid(row=1, column=0)

        self.moneyText2 = Label(self)
        self.moneyText2["text"] = str(self.playerMoney[1])
        self.moneyText2.grid(row=1, column=1)

        self.moneyText3 = Label(self)
        self.moneyText3["text"] = str(self.playerMoney[2])
        self.moneyText3.grid(row=1, column=2)

        self.moneyText4 = Label(self)
        self.moneyText4["text"] = str(self.playerMoney[3])
        self.moneyText4.grid(row=1, column=3)


        print self.playerMoney, self.winCount, self.loseCount
        self.newGame = Button(self)
        self.newGame["text"] = "繼續再戰！"
        self.newGame["command"] = self.__init__
        self.newGame.grid(row=2, column=0, columnspan=4)


if __name__ == '__main__':
    root = Tk()
    root.wm_title("麻將之神")
    app = MaJiang(master=root)
    app.mainloop()
