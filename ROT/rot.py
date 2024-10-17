from rotate_ch import rotate_character


def rot_cipher(text: str, rotation: int) -> str:
	result = []

	for char in text:
		rotated_char = rotate_character(char, rotation)
		result.append(rotated_char)

	return ''.join(result)
