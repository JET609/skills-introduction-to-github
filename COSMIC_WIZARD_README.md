# 🌟 Cosmic Number Wizard 🔮

A fun, interactive number guessing game written in Python!

## 🎮 What is this?

Cosmic Number Wizard is an engaging number guessing game where players try to discover a secret number chosen by the mystical cosmic forces. The game features:

- 🎯 **Multiple difficulty levels** - Choose from Novice to Cosmic Legend
- 🔥 **Dynamic hints** - Get proximity-based feedback (Blazing Hot, Warm, Cool, Ice Cold)
- 📊 **Guess tracking** - See your journey through all your guesses
- ✨ **Beautiful ASCII art** - Enjoy a visually appealing terminal experience
- 🔄 **Replay functionality** - Play as many times as you want!

## 🚀 How to Play

1. **Run the game:**
   ```bash
   python3 cosmic_number_wizard.py
   ```

2. **Choose your difficulty:**
   - **Novice:** 15 attempts (Perfect for beginners!)
   - **Adept:** 10 attempts (A balanced challenge)
   - **Master:** 7 attempts (For experienced players)
   - **Cosmic Legend:** 5 attempts (The ultimate test!)

3. **Start guessing!**
   - The wizard picks a number between 1 and 100
   - Enter your guess and receive mystical hints
   - Use the directional hints (Higher/Lower) and proximity hints (Hot/Cold) to zero in on the answer

4. **Win or learn!**
   - Successfully guess the number to win
   - If you run out of attempts, the secret number will be revealed
   - See your complete guess history either way

## 💡 Features

- **Smart Input Validation:** The game gracefully handles invalid inputs
- **Proximity Hints:** Get feedback on how close you are:
  - 🔥 Blazing Hot (5 or less away)
  - ♨️ Very Warm (6-10 away)
  - 🌡️ Getting Warmer (11-20 away)
  - ❄️ Cool (21-30 away)
  - 🧊 Ice Cold (31+ away)
- **Graceful Exit:** Press Ctrl+C anytime to exit gracefully

## 🛠️ Requirements

- Python 3.6 or higher
- No external dependencies required! Uses only Python standard library

## 🎯 Educational Value

This game is great for:
- Learning Python basics
- Understanding game loops and user input
- Practicing conditional logic
- Getting comfortable with the terminal/command line

## 🌟 Tips for Players

1. Start with a middle number (like 50) to split the search space
2. Pay attention to both directional and proximity hints
3. Use binary search strategy for optimal guessing
4. The proximity hints can help you fine-tune when you're close!

## 🤝 Contributing

Feel free to fork this repository and add your own features! Some ideas:
- Add more difficulty levels
- Implement a scoring system based on number of guesses
- Add a high score tracker
- Create themed variants (Space Wizard, Ocean Oracle, etc.)

## 📝 License

This project is part of the skills-introduction-to-github repository and follows the same MIT License.

---

**Happy Guessing!** May the cosmic forces guide your intuition! 🌙✨
