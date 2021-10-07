#  @OLLIT_DEV
import random 
capital_letters="QWERTYUIOPASDFGHJKLZXCVBNM"
lowercase_letters="qwertyuiopasdfghjklzxcvbnm"
numbers="1234567890"
symbols="!@#$%^<>?/':;"
stickers="😊😉😋😀😄😅😂😃😆😝😜😛"#😇😒😐😕😏😑😍😘😚😗😙😳😁😬😓😔😌😞😥😩😫😣😖😢😭😪😴😷😎😰😨😱😠😤😵😲😟😦😧😮😯😶🙁🙂🙃🙄"

CL,ll,num,simbol,sticker =True,True,True,True,True

hammasi=""
if CL:
    hammasi+=capital_letters
if ll:
    hammasi+=lowercase_letters
if num:
    hammasi+=numbers
if simbol:
    hammasi+=symbols
if sticker:
    hammasi+=stickers
length=15
number_of_codes=5
for x in range(number_of_codes):
    parol="".join(random.sample(hammasi,length))
    print(parol)