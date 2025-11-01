"""EM.
The author (Egor Perevalov) is 10 years old.
EM - Egor Moon Language(EM or EML).
"""
# imports
import time, random, os, sys, math, logging
from hashlib import sha1, sha224, sha256, sha384, sha512
# init
sys.set_int_max_str_digits(100000*1000)
logging.basicConfig(level=logging.INFO)
# vars
l = 10000
funs = {}
consts = []
__version__ = '1.1.1'
__author__ = 'Egor Perevalov'
__tg__ = "@Htmlhtmljs"
__emcls__ = "EMCLS(Egor Moon Language Correct Syntatix)\n"
simvols = "qwertyuiopasdfghjklzxcvbnm1234567890-_$#@*!?QWERTYUIOPASDFGHJKLZXCVBNM"
inf = math.pow(100, 100)
__example__ = __emcls__ + """Example:
1) print Hello, world!;
2) a = 4;
print get a;
3) help;
4) a = 4+4;
5) print type gen_key();"""
helps = {"hash": """a = hash('text', 224);
Explanation:
"text": text to hash
"v": version to hash
""",
"print": """Outputting data to the screen.
print var, str, int, float, list, ect.
""",
"indents": """There are no indents in EM!
if a:
	print yes;
	print y;
Wrong!
Right:
if a: print yes; print y;
"""}
file: str | None = None
# defs
def hash(text="", v=256):
	if v == 1:
		return sha1(text.encode()).hexdigest()
	elif v == 224:
		return sha224(text.encode()).hexdigest()
	elif v == 256:
		return sha256(text.encode()).hexdigest()
	elif v == 384:
		return sha384(text.encode()).hexdigest()
	elif v == 512:
		return sha512(text.encode()).hexdigest()
def sin(m):
	return math.sin(m)
def cos(m):
	return math.cos(m)
def exp(m):
	return math.exp(m)
def repl_help(h):
	if h in helps:
		print(helps[h])
	else:
		print("Unknown command.")
def help():
	h = __doc__ + __example__
	print(h)
	print("Help(type «quit» to exit): ")
	while True:
		h = input(">>> ").strip().lower()
		if h == "quit":
			break
		repl_help(h)
def spl(code):
	return code.split(";")
def error(type, e):
	return f"""{type}Error: {e}."""
def num(res):
	if "os" in res or "sys" in res:
		print(error("No rights to this"))
		return 0
	else:
		return eval(res)
def dictionary():
	return {}
def gen_key(l):
	p = ""
	for _ in range(l):
		p+=random.choice(simvols)
	return p
def gen_byte(l):
	p = os.urandom(l)
	return p
def read(file):
	return open(str(file), "r").read()
def st(text="", c=1):
	return text*c
def ranges(e, s=0, st=1):
	return list(range(s, e, st))
def srep(s):
	s = s.replace("%s0", "", l)
	s = s.replace("%s1", " ", l)
	s = s.replace("%s2", ".", l)
	s = s.replace("%s3", ",", l)
	s = s.replace("%s4", "€", l)
	s = s.replace("%s5", "£", l)
	s = s.replace("%s6", "~", l)
	s = s.replace("%s7", "`", l)
	s = s.replace("%s8", "|", l)
	s = s.replace("%s9", "/", l)
	s = s.replace("%s10", "\\", l)
	return s
def parse_s(name, text):
	s = text.strip().strip("{}").split(",")
	code = ""
	for i in range(len(s)):
		res = s[i].strip()
		ress = res.split(":")
		if len(ress) == 2:
			code += f"\"{ress[0]}\": {ress[1]}, "
	exec(name + "=" + "{" + code + "}", globals())
def emc(file, path="__emcache__/"):
	if not os.path.exists(path):
		os.system(f"mkdir {path}")
	pf = path + file
	if os.path.exists(pf):
		f = open(pf, "rb")
		fr = f.read()
		f.close()
		return fr
	return False
def emc_write(code, file, path="__emcache__"):
	if not os.path.exists(path):
		os.system(f"mkdir {path}")
	pf = path + "/" + file
	f = open(pf, "wb")
	f.write(code.encode("utf-8"))
	f.close()
def parse(code, pb=False):
	codep = code.strip()
	codep = codep.replace("%inf", "100000000000000000000000000000", l)
	code = spl(code)
	for i in range(len(code)):
		s = code[i].strip()
		if s == "":
			continue
		s = s.replace("%inf", "100000000000000000000000000000", l)
		s = s.replace("%time", time.strftime("%X"), l)
		s = s.replace("%date", time.strftime("%x"), l)
		s = s.replace("%H", time.strftime("%H"), l)
		s = s.replace("%M", time.strftime("%M"), l)
		s = s.replace("%S", time.strftime("%S"), l)
		s = srep(s)
		if s[0] == "#":
			continue
		if s[0] == " ":
			fg = 0
			for x in range(len(s)):
				if s[x] == " ":
					fg = 1
					break
				elif s[x] == " ":
					continue
				else:
					break
			if not fg:
				break
		if "help" == s:
			help()
		elif "func" in s:
			res = codep.replace("func", "", 1).strip()
			resn = res.split(":", 1)
			if len(resn) != 2:
				print(error("Len", "The length exceeds the norm."))
				return
			funs[resn[0]] = resn[1]
			return
		elif "repeat" in s:
			sres = codep.split(":", 1)
			try:
				sres_0 = int(eval(sres[0].replace("repeat", "")))
			except:
				print(error("Repeat", "Repeat: invalid argument"))
				return
			sres_1 = sres[1]
			if len(sres) != 2:
				print(error("Len", f"Repeat: takes 2 arguments, not {len(sres)}"))
			else:
				sr = sres_1.split(";")
				for _ in range(sres_0):
					for i in range(len(sr)):
						parse(sr[i], True)
		elif "if" in s:
			sres = codep.replace("if", "")
			sres = sres.split(":", 1)
			s0 = bool(eval(sres[0].strip(), globals()))
			if s0:
				parse(sres[1].strip())
		elif "consts" == s:
			print(consts)
		elif "notconst" in s:
			sc = s.replace("notconst", "").strip()
			if sc.strip() in [c.strip() for c in consts]:
				consts.remove(sc)
		elif "const" in s:
			sc = s.replace("const", "").strip()
			consts.append(sc)
		elif "import" in s:
			imp = s.replace("import", "").strip()
			if os.path.exists(f"{imp}.em"):
				t = open(imp + ".em", "r").read()
				parse(t)
			else:
				print(error(f"Import", "Unable to import: {imp}"))
		elif "sleep" in s:
			slp = s.replace("sleep", "").strip()
			try:
				time.sleep(float(slp))
			except:
				print(error("Sleep", "Sleep: invalid argument"))
		elif "write" in s:
			sres = s.split(",", 1)
			if len(sres) != 2:
				print(error("Len", f"Write: takes 2 arguments, not {len(sres)}"))
			else:
				sres0 = sres[0].replace("write", "", 1).strip()
				sres1 = sres[1].strip()
				open(sres0, "w").write(sres1)
		elif s == "stop":
			break
		elif s == "ln":
			print()
		elif "python" in s:
				res = s.replace("python", "", 1).strip()
				try:
					exec(res)
				except Exception as e:
					print(error("Python", f"Invalid operation: PythonError: {e}"))
		elif "exit" == s:
			sys.exit()
		elif "del" in s:
			res = s.replace("del", "", 1).strip()
			exec("del " + res, globals())
		elif "call" in s:
			res = s.replace("call", "", 1).strip()
			if res in funs:
				fun_commands = spl(funs[res])
				for cmd in fun_commands:
					if cmd.strip(): 
						parse(cmd.strip())
		elif "=" in s:
			resn = s.split("=")
			if len(resn) != 2:
				print(error("Var", "The variable is not defined correctly"))
			if resn[0].strip() in [c.strip() for c in consts]:
				print(error("Const", "The constant cannot be changed"))
			else:
				if "}" in s and "{" in s:
					parse_s(resn[0], resn[1])
					return
				if "type" in s:
					ex = resn[1].replace("type", "").strip()
					try:
						exec(f"{resn[0]} = type({ex})", globals())
					except:
						print(error("NotFound", f"{ex} is not defined"))
					return
				try:
					exec(f"{resn[0]} = {resn[1]}", globals())
				except TypeError:
					print(error("Type", "It is not possible to add different types of data together"))
				except ZeroDivisionError:
					print(error("ZeroDivision", "It is impossible to divide by zero"))
		elif "print" in s:
			res = s.replace("print", "", 1).strip()
			try:
				res = eval(res)
				print(res)
			except:
				print(error("Name", f"{res} is not defined"))
		else:
			print(error("NotFound", f"{s} is not defined"))
class EM:
	def __init__(self, name=""):
		self.name = name
	def call(self):
		r = open(self.name, "r")
		res = r.readlines()
		r.close()
		for i in range(len(res)):
			parse(res[i])
	def repl(self):
		cmd = input(">>> ")
		parse(cmd)
em = EM("")
while True:
	em.repl()
