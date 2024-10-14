import tkinter as tk
from tkinter import messagebox
import DES
import re


def generate_key():
    # 生成密钥的逻辑
    key.set(DES.binary_to_hex(DES.generate_key()))
    messagebox.showinfo("Key Generated", "Key has been generated successfully!")


def is_hex_string(s):
    # 匹配0-9, a-f, A-F之间的字符
    match = re.fullmatch(r'[0-9a-fA-F]+', s)
    return match is not None


def encrypt():
    # 加密逻辑
    plain_text = input_text.get("1.0", tk.END).strip()
    if not plain_text:
        messagebox.showwarning("Input Error", "Please enter the plain text to encrypt.")
        return
    # 验证密钥
    if len(key.get()) == 0 or is_hex_string(key.get()) is False or len(key.get()) != 16:
        messagebox.showwarning("Key Error", "Your key is not valid")
        return
    encrypted_text = DES.encryption(plain_text, DES.hex_to_binary_64(key.get()))
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, encrypted_text)


def decrypt():
    # 解密逻辑
    encrypted_text = input_text.get("1.0", tk.END).strip()
    if not encrypted_text:
        messagebox.showwarning("Input Error", "Please enter the cipher text to decrypt.")
        return
    # 验证密钥
    if len(key.get()) == 0 or is_hex_string(key.get()) is False or len(key.get()) != 16:
        messagebox.showwarning("Key Error", "Your key is not valid")
        return
    plain_text = DES.deciphering(encrypted_text, DES.hex_to_binary_64(key.get()))  # 替换为实际解密逻辑
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, DES.binary_to_utf8_string(plain_text))


# 创建主窗口
root = tk.Tk()
root.title("Welcome To Data Encryption Standard System")

key = tk.StringVar()

# 设置窗口大小
root.geometry("500x500")

# 标题标签
title_label = tk.Label(root, text="Welcome To Data Encryption Standard System", font=("Arial", 14))
title_label.pack(pady=10)

enter_key_label = tk.Label(root, text="Enter Key: ")
enter_key_label.pack(pady=5)

enter_key_entry = tk.Entry(width=40, textvariable=key)
enter_key_entry.pack(pady=5)

generate_key_button = tk.Button(root, text="Generate key", command=generate_key)
generate_key_button.pack(pady=5)

origin_text = tk.StringVar()
result = tk.StringVar()
# 输入框和输出显示区域
input_label = tk.Label(root, text="Enter Plaintext/Ciphertext:")
input_label.pack(pady=5)

input_text = tk.Text(root, height=3, width=40)
input_text.pack(pady=5)

output_label = tk.Label(root, text="Output:")
output_label.pack(pady=5)

output_text = tk.Text(root, height=3, width=40)
output_text.pack(pady=5)

# 加密和解密按钮
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

encrypt_button = tk.Button(button_frame, text="Encryption", command=encrypt)
encrypt_button.pack(side=tk.LEFT, padx=20)

decrypt_button = tk.Button(button_frame, text="Decipher", command=decrypt)
decrypt_button.pack(side=tk.RIGHT, padx=20)

exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack(pady=20)
# 运行主循环
root.mainloop()
