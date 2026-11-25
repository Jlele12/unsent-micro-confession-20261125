import os

LINE = "Unsent: I didn't delete your number. I kept it so I could watch your name light up when someone else texted me, and pretend for one second it might be you. That's all. You can have your hoodie back."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
