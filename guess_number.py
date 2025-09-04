import os
import random


def play():
    print("欢迎来到猜数字游戏！")
    number = int(os.getenv("TARGET_NUMBER", random.randint(1, 100)))
    attempts = 0
    while True:
        guess = input("请输入 1 到 100 之间的数字：")
        attempts += 1
        try:
            guess_int = int(guess)
        except ValueError:
            print("请输入有效的数字！")
            continue
        if guess_int < number:
            print("太小了！")
        elif guess_int > number:
            print("太大了！")
        else:
            print(f"恭喜你，猜对了！总共猜了 {attempts} 次。")
            break


if __name__ == "__main__":
    play()
