# 🍔 Telegram Food Ordering Bot

A modern Telegram food ordering bot built with **Aiogram 3** and **SQLite**.

This bot allows users to place food orders, upload payment receipts, and automatically sends order details to the admin.

---

## 🚀 Features

- 🛒 Food selection system
- 🥤 Optional drinks
- 📦 Order summary with total calculation
- 💳 Payment confirmation via photo upload
- 📊 SQLite database storage
- 👑 Admin order notifications
- 📈 Monthly and total statistics support

---

## 🛠 Tech Stack

- Python 3.10+
- Aiogram 3.x
- SQLite3
- FSM (Finite State Machine)
- Git & GitHub

---

## 📂 Project Structure

```
telebot/
│
├── bot.py
├── config.py
├── database.py
│
├── data/
│   └── products.py
│
├── handlers/
│   ├── start.py
│   └── order.py
│
├── keyboards/
│   └── menu.py
│
└── README.md
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/telegram-food-bot.git
cd telegram-food-bot
```

2. Create virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create `.env` file:

```
BOT_TOKEN=your_bot_token
ADMIN_ID=your_telegram_id
```

5. Run the bot:

```bash
python bot.py
```

---

## 📊 Database

All orders are stored in SQLite database:

```
orders.db
```

You can expand the project to include:

- Order status tracking
- Monthly revenue reports
- Admin dashboard
- Payment API integration

---

## 🔐 Environment Variables

| Variable   | Description            |
|------------|-----------------------|
| BOT_TOKEN  | Telegram bot token     |
| ADMIN_ID   | Admin Telegram ID      |

---

## 📈 Future Improvements

- Web admin panel
- Online payment integration (Click / Payme)
- Order history for users
- Deployment on VPS

---

## 👨‍💻 Author

Developed as a scalable Telegram automation system.

---

⭐ If you like this project, consider giving it a star!