# 🏦 Simple Banking App — Step-by-Step Instructions

- [ ] **1. Start with a balance variable**  
  - Create a variable called `balance` and set it to something like `100.0`, which means $100.

- [ ] **2. Show a welcome message**  
  - Print a friendly message that welcomes the user and tells them their starting balance.

---

- [ ] **3. Start a loop that keeps running**  
  - Use `while True:` to start a loop that will run **forever** unless we use `break` to stop it.

---

- [ ] **4. Show the user a menu to pick an option on what they want to do**  
  Use `print()` to show these options:  
  - `c` - Check balance  
  - `d` - Deposit money  
  - `w` - Withdraw money  
  - `e` - Exit  

---

- [ ] **5. Ask the user to pick an option**  
  - Use `input()` to get what the user types.  
  - Save it in a variable like `choice`.

---

- [ ] **6. If the user typed `"c"` (check balance)**  
  - Show the current balance using `print()`.

---

- [ ] **7. Else if they typed `"d"` (deposit money)**  
  - Ask: “How much would you like to deposit?”  
  - Convert their answer to a number (example: `int(input(...))`)  
  - Add it to the balance (use `+=`)
  - Show the new balance with print()

---

- [ ] **8. Else if they typed `"w"` (withdraw money)**  
  - Ask: “How much would you like to withdraw?”  
  - If the user has enough money (use an `if` statement):  
    - Subtract it from the balance  
    - Show the new balance  
  - Otherwise, print: **"Not enough money!"**

---

- [ ] **9. Else if they typed `"e"` (exit)**  
  - Print a goodbye message  
  - Use `break` to stop the loop

---

- [ ] **10. Else (they typed something else)**  
  - Print: **"Invalid option, try again!"**
