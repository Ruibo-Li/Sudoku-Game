#sudokugame.py
#execute a the sudoku game
from sudoku import*
from button import*
from graphics import*

#SudokuGame class
class SudokuGame:
    """This class creates a sudoku game"""
    def __init__(self,win,Pstart,length):
        self.length=length
        self.Pstart=Pstart
        self.win=win
        self.__start(win)

    "This function draws the start interface"
    def __start(self,win):
        Image_back1=Image(Point(600,500),"image\setting1.gif")
        Image_back1.draw(win)
        Button_play=Button(win,Point(500,350),550,100,"Start")
        Button_play.activate()
        Button_how=Button(win,Point(500,250),550,100,"Help",'green')
        Button_how.activate()
        Button_exit=Button(win,Point(500,150),550,100,"Exit",'red')
        Button_exit.activate()
        Image_welcome=Image(Point(500,800),"image\sudoku.gif")
        Image_welcome.draw(win)
        while 1:
            p=win.getMouse()
            if Button_how.clicked(p):
                win.close()
                win2=GraphWin("How to Play It",800,800)
                win2.setCoords(0,0,1000,1000)
                self.__introduction(win2)
                break
            elif Button_play.clicked(p):
                win.close()
                win2=GraphWin("Choose the Level",800,800)
                win2.setCoords(0,0,1000,1000)
                self.__chooselevel(win2)
                break
            elif Button_exit.clicked(p):
                win.close()
                break

    "This function draws the introduction interface"
    def __introduction(self,win):
        Image_back2=Image(Point(500,500),"image\setting2.gif")
        Image_back2.draw(win)
        Text_intro=Text(Point(300,900),"Sudoku, sometimes spelled Su Doku, is a")
        Text_intro.draw(win)
        Text_intro=Text(Point(300,870),"logic-based placement puzzle, also known")
        Text_intro.draw(win)
        Text_intro=Text(Point(300,840),"as Number Place in the United States.")
        Text_intro.draw(win)
        Text_intro=Text(Point(300,810),"The aim of the canonical puzzle is to enter ")
        Text_intro.draw(win)
        Text_intro=Text(Point(300,780),"a numerical digit from 1 through 9 in each")
        Text_intro.draw(win)
        Text_intro=Text(Point(300,750),"cell of a 9*9 grid made up of 3*3 subgrids ")
        Text_intro.draw(win)
        Text_intro=Text(Point(300,720),"(called ""regions""), starting with various ")
        Text_intro.draw(win)
        Text_intro=Text(Point(300,690),"digits given in some cells (the ""givens""). ")
        Text_intro.draw(win)
        Text_intro=Text(Point(300,660),"Each row, column, and region must contain only")
        Text_intro.draw(win)
        Text_intro=Text(Point(300,630),"requires patience and logical ability. Its grid")
        Text_intro.draw(win)
        Text_intro=Text(Point(300,500),"layout is reminiscent of other newspaper puzzles")
        Text_intro.draw(win)
        Text_intro=Text(Point(300,470),"like crosswords and chess problems. Although")
        Text_intro.draw(win)
        Text_intro=Text(Point(300,440),"first published in 1979, Sudoku initially ")
        Text_intro.draw(win)
        Text_intro=Text(Point(300,410),"caught on in Japan in 1986 and attained ")
        Text_intro.draw(win)
        Text_intro=Text(Point(300,370),"international popularity in 2005.")
        Text_intro.draw(win)
        Button_return=Button(win,Point(800,100),150,80,"Return")
        Button_return.activate()
        while 1:
            p=win.getMouse()
            if Button_return.clicked(p):
                win.close()
                win=GraphWin("",800,800)
                win.setCoords(0,0,1000,1000)
                self.__start(win)
                break

    "This function draws the level choosing interface"
    def __chooselevel(self,win):
        Image_back3=Image(Point(500,500),"image\setting3.gif")
        Image_back3.draw(win)
        Button_level=[]
        Button_level.append(Button(win,Point(800,700),300,100,"Easy"))
        Button_level.append(Button(win,Point(800,500),300,100,"Medium",'orange'))
        Button_level.append(Button(win,Point(800,300),300,100,"Hard",'red'))
        Button_return=Button(win,Point(850,100),200,100,"Return",'pink')
        Button_return.activate()
        for i in range(3):
            Button_level[i].activate()
        while 1:
            p=win.getMouse()
            for i in range(3):
                if Button_level[i].clicked(p):
                    win.close()
                    win=GraphWin("Play",800,800)
                    win.setCoords(0,0,1000,1000)
                    self.__playgame(win,i)
                    return
            if Button_return.clicked(p):
                win.close()
                win=GraphWin("",800,800)
                win.setCoords(0,0,1000,1000)
                self.__start(win)
                return

    "This function draws the game interface"
    def __playgame(self,win,level):
        Image_back4=Image(Point(300,500),"image\setting4.gif")
        Image_back4.draw(win)
        sdk=Sudoku()
        self.sdkquestion=sdk.CreateSudoku()
        self.sdkanswer=sdk.getblanks(level)
        self.buttons=[]
        self.tests=[]
        self.win=win
        xstart,ystart=self.Pstart.x-self.length/2,self.Pstart.y-self.length/2
        for i in range(9):
            buttmp=[]
            testtmp=[]
            for j in range(9):
                tmptests=Text(Point(self.Pstart.x+j*self.length,self.Pstart.y+(8-i)*self.length),str(self.sdkquestion[i][j]))
                tmptests.setFace("courier")
                tmptests.setStyle("bold")
                tmptests.setSize(16)
                if self.sdkanswer[i][j]==0:
                    color='white'
                    tmptests.setText("")
                else :
                    color='yellow'
                tmpbuttons=Button(win,Point(self.Pstart.x+j*self.length,self.Pstart.y+(8-i)*self.length),self.length,self.length,"",color)
                tmptests.draw(win)
                buttmp.append(tmpbuttons)
                testtmp.append(tmptests)
            self.buttons.append(buttmp)
            self.tests.append(testtmp)
        for i in range(3):
            for j in range(3):
                rec=Rectangle(Point(xstart+i*3*self.length,ystart+j*3*self.length)\
                ,Point(xstart+(i+1)*3*self.length,ystart+(j+1)*3*self.length))
                rec.draw(win)
                rec.setWidth(2)
        self.Button_check=Button(win,Point(200,150),300,100,"Check",'lightblue')
        self.Button_check.activate()
        self.Button_return=Button(win,Point(500,150),300,100,"Return",'pink')
        self.Button_return.activate()
        self.Button_answer=Button(win,Point(800,150),300,100,"Answer",'green')
        self.Button_answer.activate()
        self.numbuttons=[]
        for i in range(1,10):
            tmpbuttons=Button(win,Point(200+i*60,300),60,60,str(i))
            tmpbuttons.activate()
            self.numbuttons.append(tmpbuttons)
        self.getButton()

    "This function deal with the click"
    def getButton(self):
        while 1:
            p=self.win.getMouse()
            x,y=p.getX(),p.getY()
            for i in range(9):
                for j in range(9):
                    b=self.buttons[i][j]
                    if b.xmin <= x <= b.xmax and\
                       b.ymin <= y <= b.ymax and\
                       self.sdkanswer[i][j]==0:
                        for i in range(9):
                            for j in range(9):
                                self.buttons[i][j].deactivate()
                        b.activate()                        
            for b in self.numbuttons:
                if b.clicked(p) and self.yactived():
                    c=b.getLabel()
                    d=int(c)
                    for i in range(9):
                        for j in range(9):
                            if self.buttons[i][j].active==1:
                                self.tests[i][j].setText(c)
            if self.Button_check.clicked(p):
                self.checkanswer()
                return
            if self.Button_return.clicked(p):
                self.win.close()
                win2=GraphWin("Choose the Level",800,800)
                win2.setCoords(0,0,1000,1000)
                self.__chooselevel(win2)
                return
            if self.Button_answer.clicked(p):
                for i in range(9):
                    for j in range(9):
                        answer=str(self.sdkquestion[i][j])
                        self.tests[i][j].setText(answer)

    "This function activates the clicked button"
    def yactived(self):
        for i in range(9):
            for j in range(9):
                if self.buttons[i][j].active==1:
                    return 1
        return 0

    "This function checks the player's answer"
    def checkanswer(self):
        youranswer=[]
        for i in range(9):
            tmp=[]
            for j in range(9):
                a=self.tests[i][j].getText()
                if a=='':
                    d=0
                else :
                    d=int(a)
                tmp.append(d)
            youranswer.append(tmp)
        checklist=[0,0,0,0,0,0,0,0,0]
        flag=1
        for i in range(9):
            for j in range(9):
                checklist[j]=youranswer[i][j]
            if self.checkit(checklist):
                flag=0  
        for i in range(9):
            for j in range(9):
                checklist[j]=youranswer[j][i]
            if self.checkit(checklist):
                flag=0
        for i in range(3):
            for j in range(3):
                for k in range(3*i,3*i+3,1):
                    for l in range(3*j,3*j+3,1):
                        tmp=(3*k+l)%9
                        checklist[tmp]=youranswer[k][l]
                if self.checkit(checklist):
                    flag=0
        if flag==0:
            for i in range(9):
                for j in range(9):
                    answer=str(self.sdkquestion[i][j])
                    self.tests[i][j].setText(answer)
            win3=GraphWin("Lost",400,200)
            Image_back5=Image(Point(200,100),"image\lose.gif")
            Image_back5.draw(win3)
            result=Text(Point(200,100),"You got a wrong answer!")
            result.draw(win3)
            Button_retry=Button(win3,Point(300,150),60,30,"Retry")
            Button_retry.activate()
            while 1:
                p=win3.getMouse()
                if Button_retry.clicked(p):
                    win3.close()
                    self.win.close()
                    win2=GraphWin("Choose the Level",800,800)
                    win2.setCoords(0,0,1000,1000)
                    self.__chooselevel(win2)
                    return

        else :
            win3=GraphWin("Won",400,200)
            Image_back5=Image(Point(200,100),"image\win.gif")
            Image_back5.draw(win3)
            result=Text(Point(200,100),"Congratulations!")
            result.draw(win3)
            Button_retry=Button(win3,Point(300,150),60,30,"Retry")
            Button_retry.activate()
            while 1:
                p=win3.getMouse()
                if Button_retry.clicked(p):
                    win3.close()
                    self.win.close()
                    win2=GraphWin("Choose the Level",800,800)
                    win2.setCoords(0,0,1000,1000)
                    self.__chooselevel(win2)
                    return

    "This function helps check the answer"
    def checkit(self,ar):
        for i in range(9):
            for j in range(i):
                if ar[j]==ar[i] or ar[i]==0:
                    return 1
        return 0    

if __name__=='__main__':
    win=GraphWin("Sudoku",800,800)
    win.setCoords(0,0,1000,1000)
    begin=SudokuGame(win,Point(300,400),50.0)
    
                







        
        
