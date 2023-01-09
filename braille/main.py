from collections import deque
braille = ['⠴','⠂','⠆','⠒','⠲','⠢','⠖','⠶','⠦','⠔',
			'⠁','⠃','⠉','⠙','⠑','⠋','⠛','⠓','⠊','⠚',
			'⠅','⠇','⠍','⠝','⠕','⠏','⠟','⠗','⠎','⠞',
			'⠥','⠧','⠺','⠭','⠽','⠵',
			'⠱','⠰','⠣','⠿','⠀','⠮','⠐','⠼','⠫','⠩',
			'⠯','⠄','⠷','⠾','⠡','⠬','⠠','⠤','⠨','⠌',
			'⠜','⠹','⠈','⠪','⠳','⠻','⠘','⠸']
Arabic = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
			'أ','ب','ت','ث','ج','ح','خ','د','ذ','ر',
			'ز','س','ش','ص','ض','ط','ظ','ع','غ','ف',
			'ق','ك','ل','م','ن','ه','و','ي',
			':',';','<','=',' ','!','"','#','$','%',
			'&','','(',')','*','+',',','-','.','/',
			'>','?','@','[','\\',']','^','_']
def Braille2Arabic(BrailleText) :
	return ''.join([Arabic[braille.index(fi)] for ch in BrailleText for fi in braille if ch == fi])
def Arabic2Braiile(ArabicText) :
	return ''.join([braille[Arabic.index(fi)] for ch in ArabicText for fi in Arabic if ch == fi])
myText= "مرحبا, اسمي محمد"
myText= myText[::-1]
t= Arabic2Braiile(myText)
print(t)
print(Braille2Arabic(t))
