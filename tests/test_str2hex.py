import pytest
from str2hex.src.str2hex import StringStuff

def test_str2hex_eq0():
	"""
	test for no string i.e., no input
	"""
	
	s = StringStuff('')
	assert s.str2hex() == " : "+"0"*8
	assert s._len == 0

def test_str2hex_leq4():
	"""
	tests for strings with len less than equal to 4
	e.g.: "war"
	padding: we want padding for leq4 length strings
	"""
	
	# string len is 1
	s = StringStuff("q")
	assert s.str2hex() == "q : 00000071"
	assert s._len == 1
	
	# string len is 2
	s = StringStuff("ok")
	assert s.str2hex() == "ok : 00006f6b"
	assert s._len == 2
	
	# string len is 3
	s = StringStuff("war")
	assert s.str2hex() == "war : 00776172"
	assert s._len == 3

def test_str2hex_se_leq4():
	"""
	tests for strings endianness swap with len less than equal to 4
	e.g.: "war"
	padding: we want padding for leq4 length strings
	"""
	
	# string len is 1
	s = StringStuff("q", se=True)
	print
	assert s.str2hex() == "q : 00000071\nq\x00\x00\x00 : 71000000"
	#assert s.str2hex() == "q : 00000071\nq : 71000000"
	assert s._len == 1
	
	# string len is 2
	s = StringStuff("ok", se=True)
	assert s.str2hex() == "ok : 00006f6b\nko\x00\x00 : 6b6f0000"
	assert s._len == 2
	
	# string len is 3
	s = StringStuff("war", se=True)
	assert s.str2hex() == "war : 00776172\nraw\x00 : 72617700"
	assert s._len == 3
	

def test_str2hex_eq4():
	"""
	tests for strings with len equal to 4
	e.g.: "hell"
	padding: no padding required
	"""
	
	s = StringStuff("hell")
	assert s.str2hex() == "hell : 68656c6c"
	assert s._len == 4
	
	s = StringStuff("0day")
	assert s.str2hex() == "0day : 30646179"
	assert s._len == 4

def test_str2hex_se_eq4():
	"""
	tests for strings with len equal to 4
	e.g.: "hell"
	padding: no padding required
	"""
	
	s = StringStuff("hell", se=True)
	assert s.str2hex() == "hell : 68656c6c\nlleh : 6c6c6568"
	assert s._len == 4
	
	s = StringStuff("0day", se=True)
	assert s.str2hex() == "0day : 30646179\nyad0 : 79616430"
	assert s._len == 4
	
def test_str2hex_eq5():
	"""
	tests for strings with len equal to 5
	e.g.: "hello"
	padding:
	"""
	
	s = StringStuff("hello")
	assert s.str2hex() == "hell : 68656c6c  o : 0000006f"
	assert s._len == 5
	
	s = StringStuff("plato")
	assert s.str2hex() == "plat : 706c6174  o : 0000006f"
	assert s._len == 5
	
def test_str2hex_eq6():
	"""
	tests for strings with len equal to 6
	e.g.: "reaper"
	padding: padding for splitted string of length <= 4
	"""
	
	s = StringStuff("reaper")
	assert s.str2hex() == "reap : 72656170  er : 00006572"
	assert s._len == 6

def test_str2hex_eq7():
	"""
	tests for strings with len equal to 7
	e.g.: "ripplay"
	padding: padding for splitted strings of length <= 4
	"""
	
	s = StringStuff("ripplay")
	assert s.str2hex() == "ripp : 72697070  lay : 006c6179"
	assert s._len == 7

def test_str2hex_eq8():
	"""
	tests for strings with len equal to 8
	e.g.: "watchers"
	padding: padding for splitted strings of length <=4
	"""
	
	s = StringStuff("watchers")
	assert s.str2hex() == "watc : 77617463  hers : 68657273"
	assert s._len == 8
	
def test_str2hex_eq10():
	"""
	tests for strings with len equal to 10
	e.g.: "MessageBox"
	padding: padding for splitted strings of length <=4
	"""
	
	s = StringStuff("MessageBox")
	assert s.str2hex() == "Mess : 4d657373  ageB : 61676542  ox : 00006f78"
	assert s._len == 10
	
def test_str2hex_eq12():
	"""
	tests for strings with len equal to 12
	e.g.: "threadripper"
	padding: padding for splitted strings of length <=4
	"""
	
	s = StringStuff("threadripper")
	assert s.str2hex() == "thre : 74687265  adri : 61647269  pper : 70706572"
	assert s._len == 12

def test_str2hex_eq13():
	"""
	tests for strings with len equal to 13
	e.g.: "threadripperA"
	padding: padding for splitted strings of length <=4
	"""
	
	s = StringStuff("threadripperA")
	assert s.str2hex() == "thre : 74687265  adri : 61647269  pper : 70706572  A : 00000041"
	assert s._len == 13
