# Weird RSA 

Each character of the plaintext is encrypted using a known N and unknown e, creating a ciphertext array we're given. Infact, the actual RSA behind it is completely irrelevant. All we need to know is that each character is mapped to a number via a mapping function which we cannot reverse. The ciphertext is 932 numbers long, with 31 unique numbers, making it the equivalent of a simple substitution cipher which we can easily break using frequency analysis.

I used this script(with the values already loaded in enc)
```py
english_freq = [' ', 'E','T','A','I','N','O','R','S','L','H',
                'C','M','D','Y','P','U','W','F','G','.','V',
                'B','X','K',',','Q', 'Z', '\'', '0', '9']
freqenc = sorted(set(enc),key=enc.count,reverse=True)
mapping = {}
for num in freqenc:
    if freqenc.index(num) >= len(english_freq):
        mapping[num] = '-'
    else:
        mapping[num] = english_freq[freqenc.index(num)]
dec = ''
for num in enc:
    dec += mapping[num]
print(dec)
```
Which prints out:
```
DOEKHESYW RSRLWANA NA HAEU DIO GOERVNSF AHGATNTHTNIS YNMCEOA. TCE FESEORL NUER NA TI DNSU TCE MIMHLRO LETTEOA NS TCE YNMCEOTEXT RSU TOW TI OEMLRYE TCEP GW TCE YIPPIS LETTEOA NS TCE HAEU LRSFHRFE. TCE RTTRYVEO HAHRLLW YCEYVA AIPE MIAANGNLNTNEA RSU PRVEA AIPE AHGATNTHTNISA ID LETTEOA NS YNMCEOTEXT. CE LIIVA DIO MIAANGLE RMMERONSF BIOUA RSU GRAEU IS TCRT PRVEA PIOE AHGATNTHTNISA. HANSF YIPMHTEOA, NT NA MIAANGLE TI TOW R LIT ID YIPGNSRTNISA NS OELRTNQE ACIOT TNPE. BORM TCE DLRF NS NTA DIOPRT 0 BELLDOEKHESYWRSRLWANAOIYVA. DIO EXRPMLE, ND NS TCE RSRLW'EU YNMCEOTEXT TCE PIAT MIMHLRO LETTEO NA X, ISE PRW MOEUNYT TCRT X OEMLRYEU E IO I ZISE ID TCE PIAT MIMHLRO LETTEOA NS ESFLNAC9 DOIP TCE MLRNSTEXT. NT NA HAEDHL TI LIIV DIO MIMHLRO MRNOA ID LETTEOA IO EQES TOW TI MOEUNYT AIPE DOEKHEST LISFEO AEKHESYEA ID LETTEOA IO BCILE BIOUA. TCE NSTOHUEO RLBRWA TONEA TI DNSU AEKHESYEA ID LETTEOA BCNYC ROE IDTES HAEU NS TCE AELEYTEU LRSFHRFE.
```

I'm not sure why the output is wrong, but it can be chucked into a substitution cipher solver(https://www.guballa.de/substitution-solver) to get the real plaintext:
```
FREQUENCY ANALYSIS IS USED FOR BREAKING SUBSTITUTION CIPHERS. THE GENERAL IDEA IS TO FIND THE POPULAR LETTERS IN THE CIPHERTEXT AND TRY TO REPLACE THEM BY THE COMMON LETTERS IN THE USED LANGUAGE. THE ATTACKER USUALLY CHECKS SOME POSSIBILITIES AND MAKES SOME SUBSTITUTIONS OF LETTERS IN CIPHERTEXT. HE LOOKS FOR POSSIBLE APPEARING WORDS AND BASED ON THAT MAKES MORE SUBSTITUTIONS. USING COMPUTERS, IT IS POSSIBLE TO TRY A LOT OF COMBINATIONS IN RELATIVE SHORT TIME. WRAP THE FLAG IN ITS FORMAT 0 WELLFREQUENCYANALYSISROCKS. FOR EXAMPLE, IF IN THE ANALY'ED CIPHERTEXT THE MOST POPULAR LETTER IS X, ONE MAY PREDICT THAT X REPLACED E OR O ZONE OF THE MOST POPULAR LETTERS IN ENGLISH9 FROM THE PLAINTEXT. IT IS USEFUL TO LOOK FOR POPULAR PAIRS OF LETTERS OR EVEN TRY TO PREDICT SOME FREQUENT LONGER SEQUENCES OF LETTERS OR WHOLE WORDS. THE INTRUDER ALWAYS TRIES TO FIND SEQUENCES OF LETTERS WHICH ARE OFTEN USED IN THE SELECTED LANGUAGE.
```
From here we can see the flag is WELLFREQUENCYANALYSISROCKS wrapped in the flag format(you actually had to put it in lowercase too)

#### Flag: FwordCTF{wellfrequencyanalysisrocks}
