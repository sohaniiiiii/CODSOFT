import re
import random
from difflib import get_close_matches

class AdvancedFoodChatbot:
    def __init__(self):
        self.menu = {
            "pizza": {"margherita": 250, "pepperoni": 300, "bbq chicken": 350},
            "burger": {"cheese burger": 150, "veggie burger": 130, "chicken burger": 180},
            "drinks": {"coke": 50, "lemonade": 60, "iced tea": 70}
        }
        self.order = {}
        self.responses = [
            "Great choice! What else would you like?",
            "Yummy! Anything else on your mind?",
            "Good pick! Want to add more items?",
            "Nice! Let me know if you need anything else.",
            "That sounds delicious! Anything more?"
        ]
    
    def display_menu(self):
        print("\n📜 Here's our menu:")
        for category, items in self.menu.items():
            print(f"\n🍽️ {category.capitalize()}:")
            for item, price in items.items():
                print(f"   - {item.capitalize()} | Rs {price}")
        print("\n💡 You can type 'order', 'show', 'checkout', or 'exit'.")
    
    def find_closest_match(self, user_input):
        available_items = [item for category in self.menu.values() for item in category]
        words = user_input.split()
        for word in words:
            match = get_close_matches(word, available_items, n=1, cutoff=0.6)
            if match:
                return match[0]
        return None
    
    def suggest_items(self, category):
        if category in self.menu:
            suggestions = ", ".join(self.menu[category].keys())
            return f"We have {suggestions}. Which one would you like?"
        return "❌ Sorry, that item is not available. Try something else!"
    
    def take_order(self, user_input):
        words = user_input.split()
        for category in self.menu.keys():
            if category in words:
                return self.suggest_items(category)
        
        item = self.find_closest_match(user_input)
        if item:
            quantity = input(f"➡️ How many {item.capitalize()} would you like? ").strip()
            if not quantity.isdigit() or int(quantity) <= 0:
                return "⚠️ Please enter a valid quantity."
            quantity = int(quantity)
            for category, items in self.menu.items():
                if item in items:
                    if item in self.order:
                        self.order[item]['quantity'] += quantity
                    else:
                        self.order[item] = {"price": items[item], "quantity": quantity}
                    return f"✅ {item.capitalize()} x{quantity} added to your order. {random.choice(self.responses)}"
        return "❌ Sorry, that item is not available. Try something else!"
    
    def show_order(self):
        if not self.order:
            return "🛒 Your cart is empty! Time to add some delicious food!"
        order_summary = "\n📝 Your order summary:\n"
        total = 0
        for item, details in self.order.items():
            cost = details['price'] * details['quantity']
            order_summary += f"🍽️ {item.capitalize()} x{details['quantity']} - Rs {cost}\n"
            total += cost
        order_summary += f"💰 Total: Rs {total}"
        return order_summary
    
    def checkout(self):
        if not self.order:
            return "⚠️ Your cart is empty. Add something tasty before checking out!"
        print(self.show_order())
        confirm = input("✔️ Do you want to confirm your order? (yes/no): ").strip().lower()
        if confirm in ["yes", "y"]:
            return "🎉 Thank you for your order! Your food will be delivered soon. 🚀"
        else:
            return "👌 No worries! Take your time to decide."
    
    def chat(self):
        print("\n🤖 Hello! Welcome to our interactive food ordering chatbot!")
        self.display_menu()
        while True:
            user_input = input("\n🔹 What would you like to do? (order/show/checkout/exit): ").strip().lower()
            if re.search(r'order', user_input):
                item_input = input("🍕 Enter the item you want to order: ").strip().lower()
                print(self.take_order(item_input))
            elif re.search(r'show', user_input):
                print(self.show_order())
            elif re.search(r'checkout', user_input):
                print(self.checkout())
                break
            elif re.search(r'exit', user_input):
                print("👋 Goodbye! Have a delicious day!")
                break
            else:
                print("⚠️ I'm sorry, I didn't understand that. Please enter a valid command.")

# Run the chatbot[]
if __name__ == "__main__":
    bot = AdvancedFoodChatbot()
    bot.chat()
