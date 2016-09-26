# encoding: utf-8
from Tkinter import *
import time
class MaJiang(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        self.ExistedPlayerCount = 0
        self.gamePlayed = 0
        self.playerMoney = [0, 0, 0, 0]
        self.player = ["", "", "", ""]
        self.playerTai = [0, 0, 0, 0]
        self.playerDee = [0, 0, 0, 0]
        self.loseCount = [0, 0, 0, 0]
        self.winCount = [0, 0, 0, 0]
        self.masturbateCount = [0, 0, 0, 0]
        self.playerLianZhuang = [0, 0, 0, 0]
        self.playerMaxComboWin = [0, 0, 0, 0]
        self.playerMaxComboLose = [0, 0, 0, 0]
        self.lastWinner = self.tmpComboWin = self.lastLoser = self.tmpComboLose = 0
        self.chuanTable = ['東', '南', '西', '北', '中', '發', '白']
        self.zhuangJiaTaiTable = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29] #沒設上界，目前最高連14
        # TODO: 現在是第幾圈  決定莊家 莊家台直接算 連勝
        self.chuanIndex = 0
        self.lastWinner = self.lastLoser = ""
        self.player1MoneyText = Label(self) # For
        self.player2MoneyText = Label(self) # littleEndMethod
        self.player3MoneyText = Label(self) # displaying
        self.player4MoneyText = Label(self) # money
        self.MaxLianZuangCount = self.LianZhuangCount = self.MaxLianZuangPlayer = 0
    #    master.minsize(width=600, height=100)
    #    master.maxsize(width=600, height=100)
        self.filename = str(time.strftime("%Y")) + str(time.strftime("%m")) + str(time.strftime("%d"))
        #TODO filename check
        self.calledByHooPaiMethod = False
        self.calledByZMorFPMethod = False
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
        self.displayText["text"] = "東風位"
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
            self.player[0] = self.userinput
            self.ZhuangJia = 0 #for TaiMode
            self.displayText["text"] = "南風位"
            self.playerText["text"] = "麻將鬥士二號："
        elif self.ExistedPlayerCount == 2:
            self.player[1] = self.userinput
            self.displayText["text"] = "西風位"
            self.playerText["text"] = "麻將鬥士三號："
        elif self.ExistedPlayerCount == 3:
            self.player[2] = self.userinput
            self.displayText["text"] = "北風位"
            self.playerText["text"] = "麻將鬥士四號："
        elif self.ExistedPlayerCount > 3:
            self.player[3] = self.userinput
            self.playerText.destroy()
            self.playerField.destroy()
            self.playerConfirm.destroy()
            self.preGamingMethod()



    def preGamingMethod(self):
        self.displayText.destroy()
        self.modeText = Label(self)
        self.modeText["text"] = "模式選擇"
        self.modeText.grid(row=0, column=0, columnspan=2)

        self.TaiMode = Button(self)
        self.TaiMode["text"] = "用台算"
        self.TaiMode.grid(row=1, column=0)
        self.TaiMode["command"] = self.preTaiModeMethod

        self.MoneyMode = Button(self)
        self.MoneyMode["text"] = "用錢算"
        self.MoneyMode.grid(row=1, column=1)
        self.MoneyMode["command"] = self.MoneyModeMethod


    def preTaiModeMethod(self):
        print 'preTaiModeMethod'
        self.modeText.destroy()
        self.TaiMode.destroy()
        self.MoneyMode.destroy()

        f = open(self.filename, 'w')
        f.write(self.player[0] + ' ' + self.player[1] + ' ' + self.player[2] + ' ' + self.player[3] + '\n')
        f.close()

        self.DeeText = Label(self)
        self.DeeText["text"] = "一底幾元："
        self.DeeText.grid(row=0, column=0)
        self.DeeField = Entry(self)
        self.DeeField["width"] = 10
        self.DeeField.grid(row=0, column=1, columnspan=7)

        self.TaiText = Label(self)
        self.TaiText["text"] = "一台幾元："
        self.TaiText.grid(row=1, column=0)
        self.TaiField = Entry(self)
        self.TaiField["width"] = 10
        self.TaiField.grid(row=1, column=1, columnspan=7)
        self.TaiField.bind('<Return>', lambda _: self.TaiModeMethod())

        self.confirmButton = Button(self)
        self.confirmButton["text"] = "就打這麼大吧！"
        self.confirmButton.grid(row=2, column=0, columnspan=8)
        self.confirmButton["command"] = self.TaiModeMethod

    def TaiModeMethod(self):
        print 'TaiModeMethod'
        if self.TaiField.get().isdigit() and self.DeeField.get().isdigit():
            self.Tai = int(self.TaiField.get())
            self.Dee = int(self.DeeField.get())
            self.TaiText.destroy()
            self.TaiField.destroy()
            self.DeeText.destroy()
            self.DeeField.destroy()
            self.confirmButton.destroy()
            self.TaiModeInterfaceMethod()
        else:
            self.displayText = Label(self)
            self.displayText["text"] = "來點數字吧！"
            self.displayText.grid(row=3, column=0, columnspan=8)

    def TaiModeInterfaceMethod(self):
        print 'TaiModeInterfaceMethod'
        if self.calledByHooPaiMethod:
            self.playerButton1.destroy()
            self.playerButton2.destroy()
            self.playerButton3.destroy()
            self.playerButton4.destroy()
            self.littleEndButton.destroy()
            self.realEndButton.destroy()

        self.playerText1 = Label(self)
        self.playerText1["text"] = self.player[0] #get player name
        self.playerText1.grid(row=0, column=0)
        self.playerButton1 = Button(self)
        self.playerButton1["text"] = "胡牌"
        self.playerButton1.grid(row=1, column=0)
        self.playerButton1["command"] = lambda: self.HooPaiMethod(1)

        self.playerText2 = Label(self)
        self.playerText2["text"] = self.player[1] #get player name
        self.playerText2.grid(row=0, column=1)
        self.playerButton2 = Button(self)
        self.playerButton2["text"] = "胡牌"
        self.playerButton2.grid(row=1, column=1)
        self.playerButton2["command"] = lambda: self.HooPaiMethod(2)

        self.playerText3 = Label(self)
        self.playerText3["text"] = self.player[2] #get player name
        self.playerText3.grid(row=0, column=2)
        self.playerButton3 = Button(self)
        self.playerButton3["text"] = "胡牌"
        self.playerButton3.grid(row=1, column=2)
        self.playerButton3["command"] = lambda: self.HooPaiMethod(3)

        self.playerText4 = Label(self)
        self.playerText4["text"] = self.player[3] #get player name
        self.playerText4.grid(row=0, column=3)
        self.playerButton4 = Button(self)
        self.playerButton4["text"] = "胡牌"
        self.playerButton4.grid(row=1, column=3)
        self.playerButton4["command"] = lambda: self.HooPaiMethod(4)

        self.littleEndButton = Button(self)
        self.littleEndButton["text"] = "小結"
        self.littleEndButton.grid(row=2, column=0, columnspan=4)
        self.littleEndButton["command"] = self.littleEndMethod

        self.realEndButton = Button(self)
        self.realEndButton["text"] = "止戰"
        self.realEndButton.grid(row=2, column=3)
        self.realEndButton["command"] = self.realEndMethod

    def HooPaiMethod(self, winner):
        print 'HooPaiMethod'
        #if self.calledByZMorFPMethod:
        #    print 'hi'
        self.player1MoneyText.destroy()
        self.player2MoneyText.destroy()
        self.player3MoneyText.destroy()
        self.player4MoneyText.destroy()
        self.player1MoneyText = Label(self) # For
        self.player2MoneyText = Label(self) # littleEndMethod
        self.player3MoneyText = Label(self) # displaying
        self.player4MoneyText = Label(self) # money

        self.displayText.destroy()
        self.littleEndButton.destroy()
        self.realEndButton.destroy()

        if winner == 1:
            self.winner = 1
            self.playerButton1["text"] = "自摸"
            self.playerButton2["text"] = "放炮"
            self.playerButton3["text"] = "放炮"
            self.playerButton4["text"] = "放炮"
            self.playerButton1["command"] = lambda: self.ZhiMaoMethod(self.player[0])
            self.playerButton2["command"] = lambda: self.FangPaoMethod(2)
            self.playerButton3["command"] = lambda: self.FangPaoMethod(3)
            self.playerButton4["command"] = lambda: self.FangPaoMethod(4)
        elif winner == 2:
            self.winner = 2
            self.playerButton2["text"] = "自摸"
            self.playerButton1["text"] = "放炮"
            self.playerButton3["text"] = "放炮"
            self.playerButton4["text"] = "放炮"
            self.playerButton2["command"] = lambda: self.ZhiMaoMethod(self.player[1])
            self.playerButton1["command"] = lambda: self.FangPaoMethod(1)
            self.playerButton3["command"] = lambda: self.FangPaoMethod(3)
            self.playerButton4["command"] = lambda: self.FangPaoMethod(4)
        elif winner == 3:
            self.winner = 3
            self.playerButton3["text"] = "自摸"
            self.playerButton1["text"] = "放炮"
            self.playerButton2["text"] = "放炮"
            self.playerButton4["text"] = "放炮"
            self.playerButton3["command"] = lambda: self.ZhiMaoMethod(self.player[2])
            self.playerButton1["command"] = lambda: self.FangPaoMethod(1)
            self.playerButton2["command"] = lambda: self.FangPaoMethod(2)
            self.playerButton4["command"] = lambda: self.FangPaoMethod(4)
        elif winner == 4:
            self.winner = 4
            self.playerButton4["text"] = "自摸"
            self.playerButton1["text"] = "放炮"
            self.playerButton2["text"] = "放炮"
            self.playerButton3["text"] = "放炮"
            self.playerButton4["command"] = lambda: self.ZhiMaoMethod(self.player[3])
            self.playerButton1["command"] = lambda: self.FangPaoMethod(1)
            self.playerButton2["command"] = lambda: self.FangPaoMethod(2)
            self.playerButton3["command"] = lambda: self.FangPaoMethod(3)

    '''    self.returnToTaiModeInterfaceButton = Button(self)
        self.returnToTaiModeInterfaceButton["text"] = "返回"
        self.returnToTaiModeInterfaceButton.grid(row=2, column=0, columnspan=4)
        self.returnToTaiModeInterfaceButton["command"] = self.TaiModeInterfaceMethod
        self.calledByHooPaiMethod = True'''

    def ZhiMaoMethod(self, winner):
        print 'ZhiMaoMethod'
        #self.returnToTaiModeInterfaceButton.destroy()

        self.playerButton1["text"] = "牌若"
        self.playerButton2["text"] = "回頭"
        self.playerButton3["text"] = "必有"
        self.playerButton4["text"] = "理由"
        if winner == self.player[self.ZhuangJia]:
            self.JiTaiText = Label(self)
            self.JiTaiText["text"] = "幾台："
            self.JiTaiText.grid(row=2, column=0, columnspan=2)
            self.JiTaiField = Entry(self)
            self.JiTaiField["width"] = 5
            self.JiTaiField.grid(row=2, column=1, columnspan=2)
            self.JiTaiField.bind('<Return>', lambda _: self.TaiMoneyCountMethod(0))
            self.JiTaiButton = Button(self)
            self.JiTaiButton["text"] = "貪財"
            self.JiTaiButton.grid(row=2, column=2, columnspan=2)
            self.JiTaiButton["command"] = lambda: self.TaiMoneyCountMethod(0)
            self.displayText.destroy()
    #        self.HowManyTaiMethod() #user choose
        else:
            self.JiTaiText = Label(self)
            self.JiTaiText["text"] = "非莊家幾台："
            self.JiTaiText.grid(row=2, column=0)
            self.JiTaiField = Entry(self)
            self.JiTaiField["width"] = 5
            self.JiTaiField.grid(row=2, column=1)
            self.JiTaiButton = Button(self)
            self.ZJiTaiText = Label(self)
            self.ZJiTaiText["text"] = "莊家幾台："
            self.ZJiTaiText.grid(row=2, column=2)
            self.ZJiTaiField = Entry(self)
            self.ZJiTaiField["width"] = 5
            self.ZJiTaiField.grid(row=2, column=3)
            self.ZJiTaiField.bind('<Return>', lambda _: self.TaiMoneyCountMethod(1))
            self.JiTaiButton = Button(self)
            self.JiTaiButton["text"] = "貪財"
            self.JiTaiButton.grid(row=3, column=0, columnspan=4)
            self.JiTaiButton["command"] = lambda: self.TaiMoneyCountMethod(1)
            self.displayText.destroy()

        '''self.returnToHooPaiButton = Button(self)
        self.returnToHooPaiButton["text"] = "返回"
        self.returnToHooPaiButton.grid(row=2, column=0, columnspan=4)
        self.returnToHooPaiButton["command"] = lambda: self.HooPaiMethod(winner)
        self.calledByZMorFPMethod = True'''

    #        self.HowManyTaiMethod() #user choose
    def FangPaoMethod(self, loser):
        print 'FangPaoMethod'
    #ss    self.returnToTaiModeInterfaceButton.destroy()

        self.loser = loser
        self.playerButton1["text"] = "牌若"
        self.playerButton2["text"] = "回頭"
        self.playerButton3["text"] = "必有"
        self.playerButton4["text"] = "理由"
        self.JiTaiText = Label(self)
        self.JiTaiText["text"] = "幾台："
        self.JiTaiText.grid(row=2, column=0, columnspan=2)
        self.JiTaiField = Entry(self)
        self.JiTaiField["width"] = 5
        self.JiTaiField.grid(row=2, column=1, columnspan=2)
        self.JiTaiField.bind('<Return>', lambda _: self.TaiMoneyCountMethod(2))
        self.JiTaiButton = Button(self)
        self.JiTaiButton["text"] = "貪財"
        self.JiTaiButton.grid(row=2, column=2, columnspan=2)
        self.JiTaiButton["command"] = lambda: self.TaiMoneyCountMethod(2)

        self.displayText.destroy()

        '''self.returnToHooPaiButton = Button(self)
        self.returnToHooPaiButton["text"] = "返回"
        self.returnToHooPaiButton.grid(row=2, column=0, columnspan=4)
        self.returnToHooPaiButton["command"] = lambda: self.HooPaiMethod(winner)
        self.calledByZMorFPMethod = True'''

    #    self.HowManyTaiMethod() #user choose

    # yet using
    '''
    def HowManyTaiMethod(self):
        self.TaiText1 = Label(self)
        self.TaiText1["text"] = "一台"
        self.TaiText2 = Label(self)
        self.TaiText2["text"] = "二台"
        self.TaiText3 = Label(self)
        self.TaiText3["text"] = "三台"
        self.TaiText4 = Label(self)
        self.TaiText4["text"] = "四台"
        self.TaiText5 = Label(self)
        self.TaiText5["text"] = "五台"
        self.TaiText8 = Label(self)
        self.TaiText8["text"] = "八台"
        self.TaiText16 = Label(self)
        self.TaiText16["text"] = "十六台"
    '''
    def TaiMoneyCountMethod(self, way):
        print 'TaiMoneyCountMethod'
        self.displayText = Label(self)
        if self.JiTaiField.get().isdigit():
            _Tai = int(self.JiTaiField.get())
        else:
            self.displayText["text"] = "來點數字吧！"
            self.displayText.grid(row=4, column=0, columnspan=8)

        if way == 0: #莊家自摸
            tmpTai = self.playerTai[:]
            tmpDee = self.playerDee[:]
            self.playerTai = [money - _Tai for money in self.playerTai]
            self.playerTai[self.winner - 1] += 4 * _Tai
            self.playerDee = [dee - 1 for dee in self.playerDee]
            self.playerDee[self.winner - 1] += 4

            self.loseCount = [c - 1 for c in self.loseCount]
            self.loseCount[self.winner - 1] += 1
            self.winCount[self.winner - 1] += 1
            self.masturbateCount[self.winner - 1] += 1
            self.LianZhuangCount += 1
            if self.LianZhuangCount > self.playerLianZhuang[self.winner - 1]:
                self.playerLianZhuang[self.winner - 1] = self.LianZhuangCount

            #最長連勝
            if self.lastWinner == self.winner:
                self.tmpComboWin += 1
            else:
                self.lastWinner = self.winner
                self.tmpComboWin = 1
            if self.tmpComboWin > self.playerMaxComboWin[self.winner - 1] and self.winner == self.lastWinner:
                self.playerMaxComboWin[self.winner - 1] = self.tmpComboWin

            #最長連敗
        #    self.tmpComboLose += 1
        #    if self.tmpComboLose > self.playerMaxComboLose[self.loser - 1]:
        #        self.playerMaxComboLose[self.loser - 1] = self.tmpComboLose

            f = open(self.filename, 'a')
            print 'win ' + str((self.playerTai[self.winner - 1] - tmpTai[self.winner - 1]) * self.Tai + (self.playerDee[self.winner - 1] - tmpDee[self.winner - 1]) * self.Dee)
            for i in range(0, 4):
                f.write(str((self.playerTai[i] - tmpTai[i]) * self.Tai + (self.playerDee[i] - tmpDee[i]) * self.Dee) + ' ')
            f.write('z\n')
            f.close()
        elif way == 1: #非莊家自摸
            if self.ZJiTaiField.get().isdigit():
                ZTai = int(self.ZJiTaiField.get())
            else:
                self.displayText = Label(self)
                self.displayText["text"] = "來點數字吧！"
                self.displayText.grid(row=4, column=0, columnspan=8)

            # TODO: check 莊家幾台 > 平家台
            #if ZTai < _Tai:
            #    self.displayText["text"] = "莊家要輸比較多錢啦"
            tmpTai = self.playerTai[:]
            tmpDee = self.playerDee[:]
            self.playerTai = [money - _Tai for money in self.playerTai]
            self.playerTai[self.ZhuangJia] -= (ZTai - _Tai)
            self.playerTai[self.winner - 1] += (4 * _Tai + ZTai - _Tai)
            self.playerDee = [dee - 1 for dee in self.playerDee]
            self.playerDee[self.winner - 1] += 4

            self.loseCount = [c - 1 for c in self.loseCount]
            self.loseCount[self.winner - 1] += 1
            self.winCount[self.winner - 1] += 1
            self.masturbateCount[self.winner - 1] += 1

            self.ZJiTaiField.destroy()
            self.ZJiTaiText.destroy()

            self.ZhuangJia = (self.ZhuangJia + 1) % 4
            if self.ZhuangJia == 0:
                self.chuanIndex = (self.chuanIndex + 1) % 4
            self.LianZhuangCount = 0

            #最長連勝
            if self.lastWinner == self.winner:
                self.tmpComboWin += 1
            else:
                self.lastWinner = self.winner
                self.tmpComboWin = 1
            if self.tmpComboWin > self.playerMaxComboWin[self.winner - 1] and self.winner == self.lastWinner:
                self.playerMaxComboWin[self.winner - 1] = self.tmpComboWin

            f = open(self.filename, 'a')
            print 'win ' + str((self.playerTai[self.winner - 1] - tmpTai[self.winner - 1]) * self.Tai + (self.playerDee[self.winner - 1] - tmpDee[self.winner - 1]) * self.Dee)
            for i in range(0, 4):
                f.write(str((self.playerTai[i] - tmpTai[i]) * self.Tai + (self.playerDee[i] - tmpDee[i]) * self.Dee) + ' ')
            f.write('z\n')
            print self.playerTai, tmpTai, self.playerDee, tmpDee
            f.close()

        elif way == 2: #放炮
            tmpTai = self.playerTai[:]
            tmpDee = self.playerDee[:]
            self.playerTai[self.winner - 1] += _Tai
            self.playerDee[self.winner - 1] += 1
            self.playerTai[self.loser - 1] -= _Tai
            self.playerDee[self.loser - 1] -= 1

            self.loseCount[self.loser - 1] -= 1
            self.winCount[self.winner - 1] += 1

            if self.winner - 1 == self.ZhuangJia:
                self.LianZhuangCount += 1
                if self.LianZhuangCount > self.playerLianZhuang[self.winner - 1]:
                    self.playerLianZhuang[self.winner - 1] = self.LianZhuangCount
            else:
                self.ZhuangJia = (self.ZhuangJia + 1) % 4
                if self.ZhuangJia == 0:
                    self.chuanIndex = (self.chuanIndex + 1) % 4
                self.LianZhuangCount = 0

            #最長連勝
            if self.lastWinner == self.winner:
                self.tmpComboWin += 1
            else:
                self.lastWinner = self.winner
                self.tmpComboWin = 1
            if self.tmpComboWin > self.playerMaxComboWin[self.winner - 1] and self.winner == self.lastWinner:
                self.playerMaxComboWin[self.winner - 1] = self.tmpComboWin

            f = open(self.filename, 'a')
            print 'win ' + str(_Tai * self.Tai + self.Dee)
            for i in range(0, 4):
                f.write(str((self.playerTai[i] - tmpTai[i]) * self.Tai + (self.playerDee[i] - tmpDee[i]) * self.Dee) + ' ')
            f.write('p\n')
            print self.playerTai, tmpTai
            f.close()

        # TODO: 秀winner name(非英文會有bug)
        self.displayText["text"] = "又大戰了一場！"
        self.displayText.grid(row=3, column=0, columnspan=4)
        self.JiTaiText.destroy()
        self.JiTaiField.destroy()
        self.JiTaiButton.destroy()
        self.playerButton1.destroy()
        self.playerButton2.destroy()
        self.playerButton3.destroy()
        self.playerButton4.destroy()
        self.TaiModeInterfaceMethod()
        print "莊家：" + self.player[self.ZhuangJia]
        print "連莊：" + str(self.LianZhuangCount)

    def littleEndMethod(self):
        print 'littleEndMethod'
        self.displayText.destroy()
        self.player1MoneyText["text"] = self.Tai * self.playerTai[0] + self.Dee * self.playerDee[0]
        self.player1MoneyText.grid(row=3, column=0)
        self.player2MoneyText["text"] = self.Tai * self.playerTai[1] + self.Dee * self.playerDee[1]
        self.player2MoneyText.grid(row=3, column=1)
        self.player3MoneyText["text"] = self.Tai * self.playerTai[2] + self.Dee * self.playerDee[2]
        self.player3MoneyText.grid(row=3, column=2)
        self.player4MoneyText["text"] = self.Tai * self.playerTai[3] + self.Dee * self.playerDee[3]
        self.player4MoneyText.grid(row=3, column=3)
        #self.TaiModeInterfaceMethod()


    def realEndMethod(self):
        print 'realEndMethod'
        self.playerButton1.destroy()
        self.playerButton2.destroy()
        self.playerButton3.destroy()
        self.playerButton4.destroy()
        self.realEndButton.destroy()
        self.displayText.destroy()
        self.littleEndButton.destroy()

        self.player1MoneyText["text"] = self.Tai * self.playerTai[0] + self.Dee * self.playerDee[0]
        self.player1MoneyText.grid(row=1, column=0)
        self.player2MoneyText["text"] = self.Tai * self.playerTai[1] + self.Dee * self.playerDee[1]
        self.player2MoneyText.grid(row=1, column=1)
        self.player3MoneyText["text"] = self.Tai * self.playerTai[2] + self.Dee * self.playerDee[2]
        self.player3MoneyText.grid(row=1, column=2)
        self.player4MoneyText["text"] = self.Tai * self.playerTai[3] + self.Dee * self.playerDee[3]
        self.player4MoneyText.grid(row=1, column=3)

        self.winCountText = Label(self)
        self.winCountText["text"] = "收了幾次錢"
        self.winCountText.grid(row=2, column=0, columnspan=4)
        self.p1wText = Label(self)
        self.p1wText["text"] = str(self.winCount[0])
        self.p1wText.grid(row=3, column=0)
        self.p2wText = Label(self)
        self.p2wText["text"] = str(self.winCount[1])
        self.p2wText.grid(row=3, column=1)
        self.p3wText = Label(self)
        self.p3wText["text"] = str(self.winCount[2])
        self.p3wText.grid(row=3, column=2)
        self.p4wText = Label(self)
        self.p4wText["text"] = str(self.winCount[3])
        self.p4wText.grid(row=3, column=3)

        self.loseCountText = Label(self)
        self.loseCountText["text"] = "付了幾次錢"
        self.loseCountText.grid(row=4, column=0, columnspan=4)
        self.p1lText = Label(self)
        self.p1lText["text"] = str(self.loseCount[0])
        self.p1lText.grid(row=5, column=0)
        self.p2lText = Label(self)
        self.p2lText["text"] = str(self.loseCount[1])
        self.p2lText.grid(row=5, column=1)
        self.p3lText = Label(self)
        self.p3lText["text"] = str(self.loseCount[2])
        self.p3lText.grid(row=5, column=2)
        self.p4lText = Label(self)
        self.p4lText["text"] = str(self.loseCount[3])
        self.p4lText.grid(row=5, column=3)

        self.masturbateCountText = Label(self)
        self.masturbateCountText["text"] = "自摸次數"
        self.masturbateCountText.grid(row=6, column=0, columnspan=4)
        self.p1mText = Label(self)
        self.p1mText["text"] = str(self.masturbateCount[0])
        self.p1mText.grid(row=7, column=0)
        self.p2mText = Label(self)
        self.p2mText["text"] = str(self.masturbateCount[1])
        self.p2mText.grid(row=7, column=1)
        self.p3mText = Label(self)
        self.p3mText["text"] = str(self.masturbateCount[2])
        self.p3mText.grid(row=7, column=2)
        self.p4mText = Label(self)
        self.p4mText["text"] = str(self.masturbateCount[3])
        self.p4mText.grid(row=7, column=3)


        self.comboWinCountText = Label(self)
        self.comboWinCountText["text"] = "最長連勝"
        self.comboWinCountText.grid(row=8, column=0, columnspan=4)
        self.p1cbwText = Label(self)
        self.p1cbwText["text"] = str(self.playerMaxComboWin[0])
        self.p1cbwText.grid(row=9, column=0)
        self.p2cbwText = Label(self)
        self.p2cbwText["text"] = str(self.playerMaxComboWin[1])
        self.p2cbwText.grid(row=9, column=1)
        self.p3cbwText = Label(self)
        self.p3cbwText["text"] = str(self.playerMaxComboWin[2])
        self.p3cbwText.grid(row=9, column=2)
        self.p4cbwText = Label(self)
        self.p4cbwText["text"] = str(self.playerMaxComboWin[3])
        self.p4cbwText.grid(row=9, column=3)


        self.comboLoseCountText = Label(self)
        self.comboLoseCountText["text"] = "最長連敗"
        self.comboLoseCountText.grid(row=10, column=0, columnspan=4)

        self.comboLianZhuangCountText = Label(self)
        self.comboLianZhuangCountText["text"] = "最長連莊"
        self.comboLianZhuangCountText.grid(row=12, column=0, columnspan=4)
        self.p1lzText = Label(self)
        self.p1lzText["text"] = str(self.playerLianZhuang[0])
        self.p1lzText.grid(row=13, column=0)
        self.p2lzText = Label(self)
        self.p2lzText["text"] = str(self.playerLianZhuang[1])
        self.p2lzText.grid(row=13, column=1)
        self.p3lzText = Label(self)
        self.p3lzText["text"] = str(self.playerLianZhuang[2])
        self.p3lzText.grid(row=13, column=2)
        self.p4lzText = Label(self)
        self.p4lzText["text"] = str(self.playerLianZhuang[3])
        self.p4lzText.grid(row=13, column=3)

        self.newGame = Button(self)
        self.newGame["text"] = "繼續再戰！"
        self.newGame["command"] = self.__init__
        self.newGame.grid(row=14, column=0, columnspan=4)









    def MoneyModeMethod(self):
        self.modeText.destroy()
        self.TaiMode.destroy()
        self.MoneyMode.destroy()


        self.displayText = Label(self)
        self.displayText["text"] = "決鬥吧"
        self.displayText.grid(row=3, column=0, columnspan=4)

        self.playerText1 = Label(self)
        self.playerText1["text"] = self.player[0] #get player name
        self.playerText1.grid(row=0, column=0)
        self.playerField1 = Entry(self)
        self.playerField1["width"] = 6
        self.playerField1.grid(row=1, column=0)
        self.playerField1.insert(END, "0")

        self.playerText2 = Label(self)
        self.playerText2["text"] = self.player[1] #get player name
        self.playerText2.grid(row=0, column=1)
        self.playerField2 = Entry(self)
        self.playerField2["width"] = 6
        self.playerField2.grid(row=1, column=1)
        self.playerField2.insert(END, "0")

        self.playerText3 = Label(self)
        self.playerText3["text"] = self.player[2] #get player name
        self.playerText3.grid(row=0, column=2)
        self.playerField3 = Entry(self)
        self.playerField3["width"] = 6
        self.playerField3.grid(row=1, column=2)
        self.playerField3.insert(END, "0")

        self.playerText4 = Label(self)
        self.playerText4["text"] = self.player[3] #get player name
        self.playerText4.grid(row=0, column=3)
        self.playerField4 = Entry(self)
        self.playerField4["width"] = 6
        self.playerField4.grid(row=1, column=3)
        self.playerField4.insert(END, "0")


        self.cash = Button(self)
        self.cash["text"] = "貪財貪財"
        self.cash.grid(row=2, column=0, columnspan=4)
        self.cash["command"] =  self.countMethod
        self.playerField1.bind('<Return>', lambda _: self.countMethod())
        self.playerField2.bind('<Return>', lambda _: self.countMethod())
        self.playerField3.bind('<Return>', lambda _: self.countMethod())
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
                self.playerField4.insert(END, str(-(int(self.playerField1.get()) + int(self.playerField2.get()) + int(self.playerField3.get()))))
            elif self.playerField1.get() != "" and self.playerField2.get() != "" and self.playerField4.get() != "":
                #1 2 4打ㄌ
                self.playerField3.insert(END, str(-(int(self.playerField1.get()) + int(self.playerField2.get()) + int(self.playerField4.get()))))
            elif self.playerField1.get() != "" and self.playerField3.get() != "" and self.playerField4.get() != "":
                #1 3 4
                self.playerField2.insert(END, str(-(int(self.playerField1.get()) + int(self.playerField3.get()) + int(self.playerField4.get()))))
            elif self.playerField2.get() != "" and self.playerField3.get() != "" and self.playerField4.get() != "":
                #2 3 4
                self.playerField1.insert(END, str(-(int(self.playerField2.get()) + int(self.playerField3.get()) + int(self.playerField4.get()))))
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
                currentWinner = self.player[0]
                self.winCount[0] += 1
            elif int(self.playerField1.get()) < 0:
                currentLoser = self.player[0]
                self.loseCount[0] += 1
            if int(self.playerField2.get()) > 0:
                currentWinner = self.player[1]
                self.winCount[1] += 1
            elif int(self.playerField2.get()) < 0:
                currentLoser = self.player[1]
                self.loseCount[1] += 1
            if int(self.playerField3.get()) > 0:
                currentWinner = self.player[2]
                self.winCount[2] += 1
            elif int(self.playerField3.get()) < 0:
                currentLoser = self.player[2]
                self.loseCount[2] += 1
            if int(self.playerField4.get()) > 0:
                currentWinner = self.player[3]
                self.winCount[3] += 1
            elif int(self.playerField4.get()) < 0:
                currentLoser = self.player[3]
                self.loseCount[3] += 1

            self.playerField1.delete(0, 'end')
            self.playerField2.delete(0, 'end')
            self.playerField3.delete(0, 'end')
            self.playerField4.delete(0, 'end')
            self.playerField1.insert(END, '0')
            self.playerField2.insert(END, '0')
            self.playerField3.insert(END, '0')
            self.playerField4.insert(END, '0')

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
