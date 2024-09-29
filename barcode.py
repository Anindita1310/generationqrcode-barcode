#python program code to generate a barcode(with numbers)

!pip install python-barcode
from barcode import EAN13
#EAN13 based barcode can store 13 numbers
data=&#39;1234567890111&#39;
my_code=EAN13(data)
my_code.save(&quot;myBarCode&quot;)

//alphaNumeric barcode
!pip install python-barcode
from barcode import Code128
data1=&#39;IN-2024-09-22&#39;
my_code=Code128(data1)
my_code.save(&quot;myAlphaNumBarCode&quot;)
