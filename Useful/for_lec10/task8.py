import re

phone = "2004-959-559 # This is Phone Number"

# Удаление комментариев
num = re.sub(r'#.*$', '', phone)
print(f"Phone number: {num}")

# Удаление всех символов кроме цифр
num = re.sub(r'\D', '', num)
print(f"{num}")
