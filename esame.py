class ExamException(Exception):
    pass

class Diff():
    def __init__(self,ratio=1):
        if not (isinstance(ratio,int) or isinstance(ratio,float)):
            raise ExamException("il valore di ratio deve essere un numero reale: {} non valido".format(ratio))
        if ratio==0:
            raise ExamException("il valore di ratio deve esssere diverso da zero: {} non valido".format(ratio))
        self.ratio=ratio
        
    def compute(self, lista):
        if not isinstance(lista,list):
            raise ExamException("l'aromento del metodo compute deve essere di tipo list: {} non valido".format(lista))
        if len(lista)<2:
            raise ExamException("la lista passata deve avere almeno due elementi: {} non valido".format(lista))
        
        result=[]
        for elemento in lista:
            if not (isinstance(elemento,int) or isinstance(elemento, float)):
                raise ExamException("{} /n tutti gli elementi della lista passata al metodo compute deve essere un numero: {} non valido".format(lista,elemento))
        for i in range(len(lista)-1):
            result.append((lista[i+1]-lista[i])/self.ratio)
        return result
    
        