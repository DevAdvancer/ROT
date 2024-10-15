from ROT import rot_cipher


def main():
	operation = input("Choose operation (encode/decode): ").strip().lower()
	input_text = input("Enter the text: ")

	if operation == "encode":
		rotation_value = int(input("Enter the rotation value (1-25): "))
		encoded_text = rot_cipher(input_text, rotation_value)
		print(f"Encoded text: {encoded_text}")
	elif operation == "decode":
		rotation_value = int(input("Enter the rotation value (1-25): "))
		decoded_text = rot_cipher(input_text, 26 - rotation_value)
		print(f"Decoded text: {decoded_text}")
	else:
		print("Invalid operation. Please choose 'encode' or 'decode'.")


if __name__ == "__main__":
	main()
