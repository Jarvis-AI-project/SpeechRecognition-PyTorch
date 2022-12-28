import torch


class TextProcess:
	def __init__(self):
		char_map_str = """
		' 0
		<SPACE> 1
		a 2
		b 3
		c 4
		d 5
		e 6
		f 7
		g 8
		h 9
		i 10
		j 11
		k 12
		l 13
		m 14
		n 15
		o 16
		p 17
		q 18
		r 19
		s 20
		t 21
		u 22
		v 23
		w 24
		x 25
		y 26
		z 27
		. 28
		, 29
		? 30
		! 31
		A 32
		B 33
		C 34
		D 35
		E 36
		F 37
		G 38
		H 39
		I 40
		J 41
		K 42
		L 43
		M 44
		N 45
		O 46
		P 47
		Q 48
		R 49
		S 50
		T 51
		U 52
		V 53
		W 54
		X 55
		Y 56
		Z 57
		0 58
		1 59
		2 60
		3 61
		4 62
		5 63
		6 64
		7 65
		8 66
		9 67
		- 68
		_ 69
		@ 70
		# 71
		$ 72
		% 73
		^ 74
		& 75
		* 76
		( 77
		) 78
		+ 79
		= 80
		[ 81
		] 82
		{ 83
		} 84
		| 85
		\ 86
		/ 87
		: 88
		; 89
		" 90
		' 91
		< 92
		> 93
		~ 94
		` 95
		’ 96
		” 97
		_ 98
	    ‘ 99
		“ 100
		— 101
		"""
		self.char_map = {}
		self.index_map = {}
		for line in char_map_str.strip().split('\n'):
			ch, index = line.split()
			self.char_map[ch] = int(index)
			self.index_map[int(index)] = ch
		self.index_map[1] = ' '

	def text_to_int_sequence(self, text):
		""" Use a character map and convert text to an integer sequence """
		int_sequence = []
		for c in text:
			if c == ' ':
				ch = self.char_map['<SPACE>']
			else:
				# c = c.lower()
				# c = c.replace('.', '<SPACE>')
				# c = c.replace(',', '<SPACE>')
				ch = self.char_map[c]
			int_sequence.append(ch)
		return int_sequence

	def int_to_text_sequence(self, labels):
		""" Use a character map and convert integer labels to an text sequence """
		string = []
		for i in labels:
			string.append(self.index_map[i])
		return ''.join(string).replace('<SPACE>', ' ')


textprocess = TextProcess()

def GreedyDecoder(output, labels, label_lengths, blank_label=28, collapse_repeated=True):
	arg_maxes = torch.argmax(output, dim=2)
	decodes = []
	targets = []
	for i, args in enumerate(arg_maxes):
		decode = []
		targets.append(textprocess.int_to_text_sequence(
				labels[i][:label_lengths[i]].tolist()))
		for j, index in enumerate(args):
			if index != blank_label:
				if collapse_repeated and j != 0 and index == args[j -1]:
					continue
				decode.append(index.item())
		decodes.append(textprocess.int_to_text_sequence(decode))
	return decodes, targets
