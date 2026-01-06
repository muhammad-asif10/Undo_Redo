# 🔁 Undo / Redo System Using Stack (Python)

A **command-line based Undo / Redo system** implemented in **Python** using the **Stack data structure**.
This project demonstrates how Undo and Redo functionality works internally in applications like **text editors, code editors, and browsers**.

---

## 📌 Features

* ✍ Perform actions (text input)
* ↩ Undo last action
* ↪ Redo previously undone action
* 📝 View current state
* 🖥️ Menu-driven **CLI interface**

---

## 🧠 Data Structure Used

### Stack

* Implemented using **Array (Python List)**
* Two stacks are used:

  * **Undo Stack**
  * **Redo Stack**

---

## ⚙️ Working Principle

* When a new action is performed:

  * Current state is pushed onto **Undo Stack**
  * **Redo Stack is cleared**
* When Undo is selected:

  * Current state moves to **Redo Stack**
  * Last state is popped from **Undo Stack**
* When Redo is selected:

  * Current state moves back to **Undo Stack**
  * State is popped from **Redo Stack**

---

## 📁 Project Structure

```
undo_redo_project/
│
├── main.py
├── README.md
│
├── undo_redo/
│   ├── data_structures/
│   │   └── stack.py
│   │
│   ├── services/
│   │   └── undo_redo_service.py
│   │
│   └── utils/
│       └── display.py
```

---

## ▶️ How to Run

1. **Clone the repository**

```bash
git clone https://github.com/muhammad-asif10/undo-redo-system.git
```

2. **Navigate to the project directory**

```bash
cd undo_redo_project
```

3. **Run the program**

```bash
python main.py
```

---

## 🧪 Sample Operations

* Add text as an action
* Undo last change
* Redo undone change
* Display current text state

---

## ⏱️ Time Complexity

| Operation | Complexity |
| --------- | ---------- |
| Push      | O(1)       |
| Pop       | O(1)       |
| Undo      | O(1)       |
| Redo      | O(1)       |

---

## 🎯 Learning Outcomes

* Strong understanding of **Stack data structure**
* Practical implementation of **Undo / Redo logic**
* Modular Python programming
* CLI-based application design

---

## 📚 Suitable For

* Data Structures Lab Projects
* University Assignments
* Viva & Practical Exams
* Beginner Python Portfolio

---

## 🚀 Future Enhancements

* Support for multiple actions (delete, replace)
* File-based undo/redo
* GUI or text editor simulation
* Limit stack size

---

## 👨‍💻 Author

**Muhammad Asif**
BS Computer Science


## 📜 License

This project is open-source and intended for **educational purposes only**.

