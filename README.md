# 🛠️ Python Utility Belt

A beginner-friendly collection of small but useful Python tools.
Think of it like Batman’s belt – a set of little gadgets you can pull out whenever needed.

## ✨ Features
- Simple string helpers (reverse, palindrome check, etc.)
- Basic math helpers (factorial, prime checker, etc.)
- Easy to read, easy to learn from
- Each function comes with examples & docstrings

## 📂 Project Structure
```
utils/
 ├── string_tools.py
 ├── math_tools.py
 └── file_tools.py
tests/
 ├── test_string_tools.py
 ├── test_math_tools.py
```

## 🚀 Usage
```python
from utils.string_tools import reverse_string, is_palindrome
from utils.math_tools import factorial, is_prime

print(reverse_string("hello"))  # 'olleh'
print(is_palindrome("madam"))   # True
print(factorial(5))             # 120
print(is_prime(7))              # True
```

## 🧪 Running Tests
```bash
python -m unittest discover tests
```

## 🤝 Contributing
Want to add your own gadget to the belt?
- Fork the repo
- Add your function in `utils/`
- Write a test in `tests/`
- Open a pull request

## 📜 License
MIT License – free to use, share, and modify.
