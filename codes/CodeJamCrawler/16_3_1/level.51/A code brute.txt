for tc in range(input()):
	N = input()
	escape = ""
	if N == 2:
		A, B = raw_input().split()
		A = int(A)
		B = int(B)
		if A > B:
			escape = escape + "A "*(A-B)
			escape = escape + "AB "*B
		elif A < B:
			escape = escape + "B "*(B-A)
			escape = escape + "AB "*A
		else:
			escape = escape + "AB "*A
	else:
		A, B, C = raw_input().split()
		A = int(A)
		B = int(B)
		C = int(C)
		if A == B == C:
			escape = escape + "C AB "*C
		elif A == B and A > C:
			escape == escape + "AB "*(A-C)
			escape = escape + "C AB "*C
		elif A == C and A > B:
			escape == escape + "AC "*(A-B)
			escape = escape + "C AB "*B
		elif B == C and B > A:
			escape == escape + "BC "*(B-A)
			escape = escape + "C AB "*A
		elif A > B and A > C:
			escape = escape + "A "*min(A-C,A-B)
			if B > C:
				escape = escape + "AB "*(B-C)
				escape = escape + "C AB "*C
			else:
				escape = escape + "AC "*(C-B)
				escape = escape + "C AB "*B
		elif B > A and B > C:
			escape = escape + "B "*min(B-A,B-C)
			if A > C:
				escape = escape + "AB "*(A-C)
				escape = escape + "C AB "*C
			else:
				escape = escape + "BC "*(C-A)
				escape = escape + "C AB "*A				
		elif C > A and C > B:
			escape = escape + "C "*min(C-A,C-B)
			if A > B:
				escape = escape + "CA "*(A-B)
				escape = escape + "C AB "*B
			else:
				escape = escape + "BC "*(B-A)
				escape = escape + "C AB "*A
		escape  = escape[:-1]
	print escape