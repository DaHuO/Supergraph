from math import sqrt


def run(jamcoin_length: int, jamcoin_count: int):
	def get_base_values(jamcoin_str: str) -> list:
		return [int(jamcoin_str, base) for base in range(2, 10 + 1)]

	def get_next_jamcoin(jamcoin_int: int) -> list:
		jamcoin_int += 1
		jamcoin_str = bin(jamcoin_int + 1)[2:]

		while not is_valid_jamcoin(jamcoin_str):
			jamcoin_int += 1
			jamcoin_str = bin(jamcoin_int + 1)[2:]

		return jamcoin_int, jamcoin_str

	def is_valid_jamcoin(jamcoin_str: str) -> bool:
		if jamcoin_str[0] == '1' and jamcoin_str[-1] == '1':
			for value in get_base_values(jamcoin_str):
				if is_prime(value):
					return False
			return True
		return False

	def is_valid_divisors(divisors: list) -> bool:
		for divisor in jamcoin_divisors:
			if not divisor:
				return False
		return True

	def is_prime(value: int) -> bool:
		return all(value % a for a in range(2, int(sqrt(value)) + 1))

	def get_divisors(jamcoin_str: str) -> list:
		# return {value: get_divisor(value) for value in get_base_values(jamcoin_str)}
		# result = list()
		#
		# for value in get_base_values(jamcoin_str):
		# 	divisor = get_divisor(value)
		#
		# 	if divisor in divisors:
		# 		print('i am here')
		# 		return None
		#
		# 	divisors.append(divisor)
		# 	result.append(divisor)

		return [get_divisor(value) for value in get_base_values(jamcoin_str)]

	def get_divisor(value: int) -> int:
		# for divisor in range(int(sqrt(value)) + 1, 2, -1):
		# 	if (value % divisor == 0) and not (divisor in divisors):
		# 		divisors.add(divisor)
		# 		return divisor

		if not is_prime(value):
			for divisor in range(2, value - 1):
				if value % divisor == 0:
					return divisor * get_divisor(int(value / divisor))

		return 1

	result = list()

	jamcoin_str = '1' + '0' * (jamcoin_length - 1)
	jamcoin_int = int(jamcoin_str, 2)

	for a in range(jamcoin_count):
		jamcoin_int, jamcoin_str = get_next_jamcoin(jamcoin_int)
		jamcoin_divisors = get_divisors(jamcoin_str)

		sub_result = [jamcoin_str]
		sub_result.extend(jamcoin_divisors)

		result.append(sub_result)

	return result


def arguments() -> list:
	arg1, arg2 = input().split()
	return int(arg1), int(arg2)


if __name__ == '__main__':
	input()

	jamcoin_length, jamcoin_count = arguments()
	result = run(jamcoin_length, jamcoin_count)

	print("Case #1:")

	for jamcoin in result:
		for elem in jamcoin:
			print(elem, end=' ')
		print()
