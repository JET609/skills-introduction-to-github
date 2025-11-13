#!/usr/bin/env python3
"""
🌟 Cosmic Number Wizard 🔮
A mystical number guessing game where you challenge the cosmic forces!

The wizard has chosen a secret number between 1 and 100.
Can you use your intuition to guess it before running out of attempts?
"""

import random
import sys


def print_banner():
    """Display the cosmic wizard banner"""
    print("\n" + "="*60)
    print("🌟  ✨  COSMIC NUMBER WIZARD  ✨  🌟")
    print("="*60 + "\n")


def get_difficulty():
    """Let player choose difficulty level"""
    print("Choose your destiny:")
    print("  1. Novice (15 attempts)")
    print("  2. Adept (10 attempts)")
    print("  3. Master (7 attempts)")
    print("  4. Cosmic Legend (5 attempts)")
    
    while True:
        try:
            choice = input("\nEnter your choice (1-4): ").strip()
            difficulty_map = {
                '1': ('Novice', 15),
                '2': ('Adept', 10),
                '3': ('Master', 7),
                '4': ('Cosmic Legend', 5)
            }
            if choice in difficulty_map:
                return difficulty_map[choice]
            else:
                print("⚠️  Please enter a number between 1 and 4!")
        except (EOFError, KeyboardInterrupt):
            print("\n\n👋 The cosmic forces bid you farewell!")
            sys.exit(0)


def get_guess(attempt_num, max_attempts):
    """Get a valid guess from the player"""
    while True:
        try:
            guess = input(f"\n🔮 Attempt {attempt_num}/{max_attempts} - Enter your guess (1-100): ").strip()
            guess_num = int(guess)
            if 1 <= guess_num <= 100:
                return guess_num
            else:
                print("⚠️  The cosmic realm only accepts numbers between 1 and 100!")
        except ValueError:
            print("⚠️  Please enter a valid number!")
        except (EOFError, KeyboardInterrupt):
            print("\n\n👋 The cosmic forces bid you farewell!")
            sys.exit(0)


def give_hint(guess, secret, attempts_left):
    """Provide mystical hints based on how close the guess is"""
    difference = abs(guess - secret)
    
    if difference == 0:
        return None  # Correct guess!
    elif difference <= 5:
        return "🔥 BLAZING HOT! You're incredibly close!"
    elif difference <= 10:
        return "♨️  Very warm! You're on the right track!"
    elif difference <= 20:
        return "🌡️  Getting warmer..."
    elif difference <= 30:
        return "❄️  Cool... not quite there yet."
    else:
        return "🧊 Ice cold! You're far from the cosmic truth."


def play_game():
    """Main game loop"""
    print_banner()
    print("The Cosmic Wizard has conjured a secret number between 1 and 100.")
    print("Use your mystical intuition to uncover it!\n")
    
    difficulty_name, max_attempts = get_difficulty()
    print(f"\n✨ You have chosen the path of the {difficulty_name}!")
    print(f"   You have {max_attempts} attempts to discover the cosmic number.\n")
    
    input("Press Enter to begin your quest... ")
    
    # Generate the secret number
    secret_number = random.randint(1, 100)
    attempts = 0
    guess_history = []
    
    print("\n" + "-"*60)
    print("🎮 The game begins! May the cosmic forces guide you...")
    print("-"*60)
    
    while attempts < max_attempts:
        attempts += 1
        guess = get_guess(attempts, max_attempts)
        guess_history.append(guess)
        
        if guess == secret_number:
            print("\n" + "🎉"*20)
            print(f"\n✨ CONGRATULATIONS! ✨")
            print(f"You've discovered the cosmic number: {secret_number}")
            print(f"It took you {attempts} attempt(s) to unlock the mystery!")
            print(f"\nYour journey: {' → '.join(map(str, guess_history))}")
            print("\n" + "🎉"*20 + "\n")
            return True
        
        # Give direction hint
        if guess < secret_number:
            direction = "⬆️  Too low! The cosmic number is HIGHER."
        else:
            direction = "⬇️  Too high! The cosmic number is LOWER."
        
        # Give proximity hint
        attempts_left = max_attempts - attempts
        proximity_hint = give_hint(guess, secret_number, attempts_left)
        
        print(f"\n   {direction}")
        print(f"   {proximity_hint}")
        
        if attempts_left > 0:
            print(f"   💫 {attempts_left} attempt(s) remaining...")
        
    # Game over - ran out of attempts
    print("\n" + "💔"*20)
    print(f"\n😢 The cosmic forces have spoken...")
    print(f"You've exhausted all {max_attempts} attempts!")
    print(f"The secret number was: {secret_number}")
    print(f"\nYour journey: {' → '.join(map(str, guess_history))}")
    print("\n" + "💔"*20 + "\n")
    return False


def main():
    """Main entry point"""
    try:
        while True:
            won = play_game()
            
            # Ask if player wants to play again
            while True:
                try:
                    play_again = input("🌟 Would you like to challenge the wizard again? (yes/no): ").strip().lower()
                    if play_again in ['yes', 'y', 'yeah', 'yep', 'sure']:
                        print("\n🔄 The cosmic wheel turns once more...\n")
                        break
                    elif play_again in ['no', 'n', 'nope', 'nah']:
                        print("\n" + "="*60)
                        print("🌙 Thank you for playing Cosmic Number Wizard! 🌙")
                        print("   May the cosmic forces be with you always!")
                        print("="*60 + "\n")
                        return
                    else:
                        print("⚠️  Please answer with 'yes' or 'no'")
                except (EOFError, KeyboardInterrupt):
                    print("\n\n👋 The cosmic forces bid you farewell!")
                    return
                    
    except KeyboardInterrupt:
        print("\n\n👋 The cosmic forces bid you farewell!")


if __name__ == "__main__":
    main()
