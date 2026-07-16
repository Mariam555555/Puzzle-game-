# main.py
from gamee import main as run_game
from test import test as run_tests

if __name__ == "__main__":
    print("=== 8-Puzzle Game ===")
    run_game()      # تشغل اللعبة GUI
    print("\n=== Running Tests ===")
    run_tests()     # تشغل الاختبارات
