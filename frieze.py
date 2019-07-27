import sys
import copy
from math import ceil,floor
class FriezeError(Exception):
    def __init__(self,message):
        self.message = message

class Frieze:
    def __init__(self,filename):
        self.filename = filename
        b_list=[]
        b=[]
        data=[]

        with open (filename) as file:
            for line in file:
                for i in (line.split()):
                    if int(i)>15 or int(i)<0:
                        raise FriezeError('Incorrect input.')
                    if not i.isdecimal():
                        raise FriezeError('Incorrect input.')
                    if i is not None:
                        if len(bin(int(i)))<4:
                            b.append(('000'+bin(int(i))[2:4]))
                        elif len(bin(int(i)))<5:
                            b.append(('00'+bin(int(i))[2:5]))
                        elif len(bin(int(i)))==5:
                            b.append(('0'+bin(int(i))[2:5]))
                        else:
                            b.append((bin(int(i))[2:6]))
                    else:
                        continue
                if b:               
                    b_list.append(b)

                    b=[]
            if len(b_list[0])<5 or len(b_list[0])>51:
                raise FriezeError('Incorrect input.')
            for line in b_list:
                if len(line)!=len(b_list[0]):
                    raise FriezeError('Incorrect input.')
            if len(b_list) < 3 or len(b_list) > 17:
                raise FriezeError('Incorrect input.')
            
        XX=[]
        c_1=[]
        E=[]
        c_2=[]
        XS=[]
        c_3=[]
        N=[]
        c_4=[]
        for i in b_list:
            for j in i:
                if int(j[0])==1:
                    c_1.append(1)
                else:
                    c_1.append(0)
                if int(j[1])==1:
                    c_2.append(1)
                else:
                    c_2.append(0)
                     
                if int(j[2])==1:
                    c_3.append(1)
                else:
                    c_3.append(0)
               
                if int(j[3])==1:
                    c_4.append(1)
                else:
                    c_4.append(0)
            XX.append(c_1)
            E.append(c_2)
            XS.append(c_3)
            N.append(c_4)
            c_1=[]
            c_2=[]
            c_3=[]
            c_4=[]
        self.XX = XX
        self.E = E
        self.XS = XS
        self.N = N
        self.b_list = b_list
        self.check_frieze()
    def check_frieze(self):
        b_list = self.b_list
        check_period = self.check_translation()
        for i in b_list[0][:-1]:
            if i == '0100' or i == '1100':
                pass
            else:
                raise FriezeError('Input does not represent a frieze.')
        for i in b_list[-1][:-1]:
            if i == '0100' or i =='0101' or i == '0110' or i == '0111':
                pass
            else:
                raise FriezeError('Input does not represent a frieze.')
        for i in range(len(b_list)):
            for j in range(len(b_list[0])):
                if int(b_list[i][j][0]) == 1 and int(b_list[i+1][j][2]) == 1:
                    raise FriezeError('Input does not represent a frieze.')
        b_list_1 = copy.deepcopy(b_list)
        b_list_1 = list(map(list,zip(*b_list_1[:])))
        for i in range(len(b_list_1[0])):
            if int(b_list_1[0][i][3]) ==1 and (b_list_1[-1][i]) !='0001':
                raise FriezeError('Input does not represent a frieze.')
            if int(b_list_1[0][i][3]) ==0 and (b_list_1[-1][i]) !='0000':
                raise FriezeError('Input does not represent a frieze.')
        if not check_period :
            raise FriezeError('Input does not represent a frieze.')
        if min(check_period) ==1:
            raise FriezeError('Input does not represent a frieze.')
        if check_period:
            if len(b_list_1[:-1])% min(check_period) != 0:
                raise FriezeError('Input does not represent a frieze.')
        
        
        
    def translation(self):
        d=[]
        b_list = self.b_list
        reversed_grid=list(map(list,zip(*b_list[::-1])))
        for i in range(1,len(reversed_grid)//2+1):
            if len(reversed_grid)//i-1>1:
                for j in range(1,len(reversed_grid)//i-1):
                    if reversed_grid[0:i]==reversed_grid[j*i:(j+1)*i]:
                        if j==len(reversed_grid)//i-2:
                            d.append(i)
                        
                        else:
                            continue
                    else:
                        break
            else:
                if reversed_grid[0:i]==reversed_grid[i:2*i]:
                    d.append(i)
        period = min(d)
        return (period)
        
    def check_translation(self):
        d=[]
        b_list = self.b_list
        reversed_grid=list(map(list,zip(*b_list[::-1])))
        for i in range(1,len(reversed_grid)//2+1):
            if len(reversed_grid)//i-1>1:
                for j in range(1,len(reversed_grid)//i-1):
                    if reversed_grid[0:i]==reversed_grid[j*i:(j+1)*i]:
                        if j==len(reversed_grid)//i-2:
                            d.append(i)
                        
                        else:
                            continue
                    else:
                        break
            else:
                if reversed_grid[0:i]==reversed_grid[i:2*i]:
                    d.append(i)
        return d
    def W_to_E(self):
        x = []
        r = 0
        E = self.E
        W_E = []
        y=[]
        for i in range(0,len(E)):
            for j in range(0,len(E[0])):
                if E[i][j]==1:
                    y.append(i)
                    x.append(j)
                    r+=1
                    continue
                else:
                    if x:
                        W_E.append(f'\draw ({x[0]},{y[0]}) -- ({x[0]+r},{y[0]})')
                        r=0
                        y=[]
                        x=[]
        return (W_E)
        
                  
    def N_to_S(self):
        r = 0
        x =[]
        y = []
        N = self.N
        N_S = []
        for i in range(len(N[0])):
            for j in range(len(N)):
                if N[j][i] == 1:
                    x.append(i)
                    y.append(j)
                    r +=1
                    continue
                else:
                    if y:
                        N_S.append(f'\draw ({x[0]},{y[0]-1}) -- ({x[0]},{y[0]+r-1})')
                        r = 0
                        y = []
                        x = []
        return ( N_S)
                    
    def NW_to_SE(self):
        XX = self.XX
        NW_SE = []
        change_grid = []
        x = 0
        y = 0
        for i in range(len(XX)):
            temp = [] 
            for j in range(0,len(XX[0])):
                temp.append(0)
            change_grid.append(temp)
        for i in range(len(XX)):
            for j in range(len(XX[0])):
                if XX[i][j] ==1:
                    if change_grid[i][j] == 0:
                        x = j
                        y = i
                        n = 1
                        while XX[y+n][x+n] == 1:
                            change_grid[y+n][x+n] = 1
                            n +=1
                        NW_SE.append(f'\draw ({x},{y}) -- ({x+n},{y+n})')
                    
        return ( NW_SE )
                
                    
    def SW_to_NE(self):
        XS = self.XS
        SW_NE = []
        change_grid = []
        reversed_list = []
        tem_list = []
        x = 0
        y = 0
        for i in range(len(XS)):
            temp = []
            for j in range(len(XS[0])):
                temp.append(0)
            change_grid.append(temp)
        for i in range (len(XS)):
            reversed_list.append(i)
        reversed_list.reverse()
        for j in reversed_list:
            for i in range(len(XS[0])):
                if XS[j][i] == 1:
                    if change_grid[j][i] ==0:
                        x = i
                        y = j
                        n = 1
                        while XS[y-n][x+n] == 1:
                            change_grid[y-n][x+n] =1
                            n +=1
                        tem_list.append(((x,y),(x+n,y-n)))
        tem_list = sorted(tem_list,key = lambda x:(x[0][1],x[0][0],x[1][0]))
        for i in tem_list:
            SW_NE.append(f'\draw ({i[0][0]},{i[0][1]}) -- ({i[1][0]},{i[1][1]})')
            
        return ( SW_NE )

    def display(self):
        N_S = self.N_to_S()
        W_E = self.W_to_E()
        NW_SE = self.NW_to_SE()
        SW_NE = self.SW_to_NE()
        file_name = self.filename.rstrip('.txt') + '.tex'
        result = open(f'{file_name}','w')
        result = open(f'{file_name}','w')
        result.write(r'\documentclass[10pt]{article}')
        result.write('\n')
        result.write(r'\usepackage{tikz}')
        result.write('\n')
        result.write(r'\usepackage[margin=0cm]{geometry}')
        result.write('\n')
        result.write(r'\pagestyle{empty}')
        result.write('\n')
        result.write('\n') 
        result.write(r'\begin{document}')
        result.write('\n')
        result.write('\n') 
        result.write(r'\vspace*{\fill}')
        result.write('\n')
        result.write(r'\begin{center}')
        result.write('\n')
        result.write(r'\begin{tikzpicture}[x=0.2cm, y=-0.2cm, thick, purple]')
        result.write('\n')
        result.write('% North to South lines\n')
        for i in N_S:
            result.write(f'    {i};\n')
        result.write('% North-West to South-East lines\n')
        for i in NW_SE:
            result.write(f'    {i};\n')
        result.write('% West to East lines\n')
        for i in W_E:
            result.write(f'    {i};\n')
        result.write('% South-West to North-East lines\n')
        for i in SW_NE:
            result.write(f'    {i};\n')
        result.write('\end{tikzpicture}\n')
        result.write('\end{center}\n')
        result.write(r'\vspace*{\fill}')
        result.write('\n')
        result.write('\n')
        result.write('\end{document}\n')
        result.close()
            
            
        
            
            
        
            
    def horizonal(self):
        N = self.N
        N_copy = copy.deepcopy(N)
        N_new = copy.deepcopy(N)
        N_new.reverse()
        E = self.E
        E_copy = copy.deepcopy(E)
        E_new = copy.deepcopy(E)
        E_new.reverse()
        XX = self.XX
        XX_copy = copy.deepcopy(XX)
        XX_new = copy.deepcopy(XX)
        XX_new.reverse()
        XS = self.XS
        XS_copy = copy.deepcopy(XS)
        XS_new = copy.deepcopy(XS)
        XS_new.reverse() 
        if len(N)%2 == 0:
            if N_copy[1:len(N_new)//2+1] == N_new[:len(N_new)//2]:
                if E_copy[:len(E_new)//2+1] == E_new[:len(E_new)//2+1]:
                  if XX_copy[:len(XX_copy)//2+1] == XS_new[:len(XS_new)//2+1]:
                      if XS_copy[:len(XS_copy)//2+1] == XX_new[:len(XX_new)//2+1]:
                        return True
            else:
                return False
        if len(N)%2:
            for i in range(len(XX[0])):
                if XX_new[len(N_new)//2][i] != XS_new[len(N_new)//2][i]:
                    return False
            if N_copy[1:len(N)//2+1] == N_new[:len(N_new)//2]:
                if E_copy[:len(N)//2+1] == E_new[:len(E_new)//2+1]:
                    if XX_copy[:len(N)//2+1] == XS_new[:len(XS_new)//2+1]:
                        if XS_copy[:len(N)//2+1] == XX_new[:len(XX_new)//2+1]:
                            return True
            else:
                return False
                  
    def glided_horizonal(self):
        period = self.translation()
        if period%2:
            return False
        else:
            half_period = period//2
            N = copy.deepcopy(self.N)
            N_1 = N[1:]
            N_copy = copy.deepcopy(N_1)
            N_1.reverse()
            E = copy.deepcopy(self.E)
            E_1 =E [:]
            E_copy = copy.deepcopy(E_1)
            E_1.reverse()
            XX = copy.deepcopy(self.XX)
            XX_1 = XX[:-1]
            XX_copy = copy.deepcopy(XX_1)
            XX_1.reverse()
            XS = copy.deepcopy(self.XS)
            XS_1 = XS[1:]
            XS_copy = copy.deepcopy(XS_1)
            XS_1.reverse()
            flg = True
            if len(N)%2:
                if 1 in XS[len(N)//2+1] or 1 in XX[len(N)//2+1]:
                    return False
                else:
                    for i in range(len(N_1)//2):
                        if (E_1[i][half_period:2*period]) == (E_copy[i][:2*period-half_period]):
                            
                            continue
                        else:
                            flg = False
                            break
                        if (N_1[i][half_period:2*period]) == (N_copy[i][:2*period-half_period]):
                            
                            continue
                        else:
                            flg = False
                            break
                        if (XX_1[i][half_period:2*period]) == (XS_copy[i][:2*period-half_period]):
                            
                            continue
                        else:
                            flg = False
                            break
                        if (XS_1[i][half_period:2*period]) == (XX_copy[i][:2*period-half_period]):
                            
                            continue
                        else:
                            flg = False
                            break
                    return flg
            else:
                for i in range(len(E_1)//2):
                    if (E_1[i][half_period:2*period]) == (E_copy[i][:2*period-half_period]):
                        continue
                    else:
                        flg = False
                        break
                    if (N_1[i][half_period:2*period]) == (N_copy[i][:2*period-half_period]):
                        
                        continue
                    else:
                        flg = False
                        break
                    if (XX_1[i][half_period:2*period]) == (XX_copy[i][:2*period-half_period]):
                        
                        continue
                    else:
                        flg = False
                        break
                    if (XS_1[i][half_period:2*period]) == (XS_copy[i][:2*period-half_period]):
                        
                        continue
                    else:
                        flg = False
                        break
                return flg
                
                
    def vertical(self):
        b_list = self.b_list
        period = self.translation()
        cut_line = period/2
        while cut_line <= period:
            c = 0
            flg_1 = 1
            flg_2 = False
            for i in range(len(b_list)):
                for j in range(int((cut_line)*2)):
                    if int(b_list[i][j][3]) ==1 and int(b_list[i][int(cut_line*2-j)][3]) !=1:
                        flg_1 = 0
                        break
                    if int(b_list[i][j][0]) ==1 and int(b_list[i+1][int(cut_line*2-j-1)][2]) !=1:
                        flg_1 = 0
                        break
                    if int(b_list[i][j][1]) ==1 and int(b_list[i][int(cut_line*2-j-1)][1]) !=1:
                        flg_1 = 0
                        break
                    if int(b_list[i][j][2]) ==1 and int(b_list[i-1][int(cut_line*2-j-1)][0]) !=1:
                        flg_1 = 0
                        break
                    
                    
                if flg_1 == 0:
                    break
                else:
                    c +=1
            cut_line += 1/2
            if c ==len(b_list):
                flg_2 = True
                break
        return flg_2


    def rotation(self):
        period = self.translation()
        N = copy.deepcopy(self.N)
        N = N[1:]
        N_copy = copy.deepcopy(N)
        N.reverse()
        N_new = list(map(list,zip(*N[:])))
        E = copy.deepcopy(self.E)
        E_copy = copy.deepcopy(E)
        E.reverse()
        E_new = list(map(list,zip(*E[:])))
        XX = copy.deepcopy(self.XX)
        XX = XX[:-1]
        XX_copy = copy.deepcopy(XX)
        XX.reverse()
        XX_new = list(map(list,zip(*XX[:])))
        XS = copy.deepcopy(self.XS)
        XS = XS[1:]
        XS_copy = copy.deepcopy(XS)
        XS.reverse()
        XS_new = list(map(list,zip(*XS[:])))
        for i in range(0,period+1):
            N_1=[]
            N_2=[]
            N_3=[]
            N_4=[]
            E_1=[]
            E_2=[]
            E_3=[]
            E_4=[]
            XX_1=[]
            XX_2=[]
            XX_3=[]
            XX_4=[]
            XS_1=[]
            XS_2=[]
            XS_3=[]
            XS_4=[]
            N_new = list(map(list,zip(*N_new[::-1])))
            E_new = list(map(list,zip(*E_new[::-1])))
            XX_new = list(map(list,zip(*XX_new[::-1])))
            XS_new = list(map(list,zip(*XS_new[::-1])))
            for j in N_copy:
                N_1.append(j[i:i+2*period+1])
                N_3.append(j[i+1:i+2*period+1])
            for j in N_new:
                N_2.append(j[i:i+2*period+1])
                N_4.append(j[i:i+2*period])
            for j in E_copy:
                E_1.append(j[i:i+2*period])
                E_3.append(j[i:i+2*period+1])
            for j in E_new:
                E_2.append(j[i+1:i+2*period+1])
                E_4.append(j[i:i+2*period+1])
            for j in XX_copy:
                XX_1.append(j[i:i+2*period])
                XX_3.append(j[i:i+2*period+1])
            for j in XX_new:
                XX_2.append(j[i+1:i+2*period+1])
                XX_4.append(j[i:i+2*period+1])
            for j in XS_copy:
                XS_1.append(j[i:i+2*period])
                XS_3.append(j[i:i+2*period+1])
            for j in XS_new:
                XS_2.append(j[i+1:i+2*period+1])
                XS_4.append(j[i:i+2*period+1])
            if XS_1 == XS_2 and XX_1 == XX_2 and E_1 == E_2 and N_1 ==N_2: 
                return True
            if XS_3 == XS_4 and XX_3 == XX_4 and E_3 == E_4 and N_3 ==N_4: 
                return True
                
                
    def analyse(self):
        translation = self.translation()
        horizonal = self.horizonal()
        glided_horizonal = self.glided_horizonal()
        vertical = self.vertical()
        rotation=self.rotation()
##        print(horizonal,glided_horizonal,vertical,rotation)
          
        if not horizonal and not glided_horizonal and not vertical and not rotation:
            print(f'Pattern is a frieze of period {translation} that is invariant under translation only.')
            
        if not glided_horizonal and not vertical and not rotation and horizonal:
            print(f'Pattern is a frieze of period {translation} that is invariant under translation\n        and horizontal reflection only.')
            
        if not horizonal and not vertical and not rotation and glided_horizonal:
            print(f'Pattern is a frieze of period {translation} that is invariant under translation\n        and glided horizontal reflection only.')
            
        if not horizonal and not glided_horizonal and not rotation and  vertical:
            print(f'Pattern is a frieze of period {translation} that is invariant under translation\n        and vertical reflection only.')
            
        if   not horizonal and not glided_horizonal and not vertical and rotation:
            print(f'Pattern is a frieze of period {translation} that is invariant under translation\n        and rotation only.')            
        if not horizonal and vertical and glided_horizonal and  rotation:
            print(f'Pattern is a frieze of period {translation} that is invariant under translation,\n        glided horizontal and vertical reflections, and rotation only.')
            
        if not glided_horizonal and horizonal and vertical and rotation:
            print(f'Pattern is a frieze of period {translation} that is invariant under translation,\n        horizontal and vertical reflections, and rotation only.')
        
        
            
                
                    
                    
        
        

    
                
           


        
    
 

            
    
    
            
            
                    
                

        
        


            
            
    
   
