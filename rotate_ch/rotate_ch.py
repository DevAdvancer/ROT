def rotate_character(char: str, rotation: int) -> str:
	if 'a' <= char <= 'z':
		return chr((ord(char) - ord('a') + rotation) % 26 + ord('a'))
	elif 'A' <= char <= 'Z':
		return chr((ord(char) - ord('A') + rotation) % 26 + ord('A'))
	else:
		return char
