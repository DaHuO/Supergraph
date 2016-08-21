def add_dict(d, key):
	if key not in d:
		d[key] = 1
	else:
		d[key] += 1

def find_doubles(firsts, seconds, topics):
	doubles = []
	for topic in topics:
		if topic[0] in firsts and topic[1] in seconds:
			doubles.append(topic)
	return doubles

def choose_doubles(doubles):
	f = {}
	s = {}
	for topic in doubles:
		add_dict(f, topic[0])
		add_dict(s, topic[1])
	chosen = None
	smallest = None
	for topic in doubles:
		if smallest == None:
			chosen = topic
			smallest = min(f[topic[0]], s[topic[1]])
		else:
			if min(f[topic[0]], s[topic[1]]) < smallest:
				chosen = topic
				smallest = min(f[topic[0]], s[topic[1]])
	return chosen

def solveCase(case, f, fout):
	N = int(f.readline().strip())
	topics = []
	firsts = {}
	seconds = {}
	for _ in xrange(N):
		topic = f.readline().strip()
		first, second = topic.split(' ')
		topics.append((first, second))
		add_dict(firsts, first)
		add_dict(seconds, second)
		
	real_topics = []
	for topic in topics:
		if firsts[topic[0]] == 1 or seconds[topic[1]] == 1:
			real_topics.append(topic)
			
	for topic in real_topics:
		topics.remove(topic)
		if topic[0] in firsts:
			firsts.pop(topic[0])
		if topic[1] in seconds:
			seconds.pop(topic[1])
	
	while firsts or seconds:
		doubles = find_doubles(firsts, seconds, topics)
		if doubles:
			double_topic = choose_doubles(doubles)
			topics.remove(double_topic)
			firsts.pop(double_topic[0])
			seconds.pop(double_topic[1])
		else:
			remove_topic = None
			for topic in topics:
				if topic[0] in firsts:
					firsts.pop(topic[0])
					remove_topic = topic
					break
				if topic[1] in seconds:
					seconds.pop(topic[1])
					remove_topic = topic
					break
			topics.remove(remove_topic)
	
	n_fake = len(topics)
		
	writeLine(fout, case, str(n_fake))

def writeLine(fout, n, result):
	print("Case #%d: %s\n" %(n, result))
	fout.write("Case #%d: %s\n" %(n, result))

if __name__ == '__main__':
	
	inputFileName = 'C-small-attempt1.in'
	
	f = file(inputFileName)
	fout = file("%s.out" %(inputFileName.split(".")[0]), "w")
	
	T = eval(f.readline())
	
	for case in xrange(T):
		solveCase(case + 1, f, fout)
		
	f.close()
	fout.close()
