# 🎮 Math Quiz Game Challenge
---

### **Challenge Overview**:

In this project, you’ll create a simple quiz game where the player answers math questions. The player earns a point for each correct answer. After 5 questions or when the player types `exit`, the game will end and display their score.

---
### 📝 Step-by-Step


- [ ] **1. Set up variables**  
  - Create a variable called `score` and set it to `0`.  
  - Create another variable called `question_count` and set it to `0`.  
  - Create a variable called `total_questions` and set it to `5`.  
---
- [ ] **2. Display a welcome message**  
  - Print a message to welcome the user.  
  - Let them know they can type `exit` to stop anytime.  

---
- [ ] **3. Start a loop with `while True`**  
  - This will keep the game running until the user quits or answers 5 questions.  
---
- [ ] **4. Generate two random numbers**  
  - Use `random.randint(1, 10)` to get two numbers.  
  - Store them in `num1` and `num2`.  
  - Create a variable `correct_answer` that holds their sum.  
---
- [ ] **5. Ask a math question**  
  - Use `input()` to ask:  
    `"What is {num1} + {num2}?"`  
---
- [ ] **6. Handle the exit case**  
  - If the user types `"exit"`, print a goodbye message and `break` out of the loop.  
---
- [ ] **7. Check if the answer is correct**  
  - Use `if` to compare the user’s answer to `correct_answer`.  
  - If it’s right, add 1 to `score` and say `"Correct!"`.  
  - If it’s wrong, print `"Wrong!"` and show the correct answer.  
---
- [ ] **8. Increase the question count**  
  - Add 1 to `question_count` after each question.  
---
- [ ] **9. End the game after 5 questions**  
  - If `question_count == total_questions`, print the final score and end the game with `break`.  
---