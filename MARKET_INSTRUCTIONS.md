# 🛒 Huddie's Under-the-Table Market: Python List Learning App

---

## 🧠 About This App

This is a fun terminal-based app designed to help beginners understand how lists work. The underground market theme adds some personality while teaching key list operations like adding, viewing, removing, and accessing items.

---

## 📦 Variables

### Inventory

A list that YOU MAKE of suspicious market items available to the user.

### Cart

An empty list where the user's selected items are stored.

---

## 🔧 All the functions:

### browse_and_add

- Prints the inventory to the user.
- Prompts them to type in an item to add to their cart.
- If the item is available, it’s added to the cart.
- If not, they receive a message saying the item isn’t sold here.

---

### display_cart

- Print the current contents of the cart.
- If empty, tells the user they haven’t added anything yet.

---

### check_first_item

- Displays the first item in the cart.
- Teaches how to access a specific index in a list.

Key concept: accessing list elements

---

## 🧹 clear_all

- Ask the user YES or NO if they really want to delete everything
- use the .clear() function to clear EVERYTHING from the list
- Tell the user that they are now safe

---

### remove_item

- Asks the user what item they want to remove.
- If found, the item is removed from the cart.
- If not, the user is warned that the item isn’t in their cart.

---

###

# ENTER THE LOOP!

## 🖥️ User Commands

| Command  | Description                            |
|----------|----------------------------------------|
| buy      | Add an item from inventory to the cart |
| cart     | View the current cart                  |
| remove   | Remove a specific item from the cart   |
| clear    | Remove all items from the cart         |
| checkout | Finalize the purchase and pay          |
| exit     | Leave the app                          |


## Do what the user wants

- Use if and elif statements to see what command the user typed in and run the correct function

---

## 🧼 Clean Interface Loop

After every action:

- Wait briefly so the user can read the message (using time)
- Clear the screen for a fresh view (using os)

---

## 👋 Exit Message

When the user types "exit", the app ends outside the loop, display a farewell message like:

"You didn’t see me, I didn’t see you. Goodbye."

---
