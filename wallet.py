import json
from datetime import datetime


class Wallet:
    def __init__(self, filename="data.json"):
        self.filename = filename
        self.informations = self.load_data()
        self.last_id = 0

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                data = file.read()
                if data.strip():
                    return json.loads(data)
                else:
                    return []
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Error decoding JSON. The file may be corrupted.")
            return []

    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.informations, file, indent=4)

    def show_balance(self):
        income = sum(data['Miqdor'] for data in self.informations if data.get('Turkum') == 'income')
        expenses = sum(data['Miqdor'] for data in self.informations if data.get('Turkum') == 'expense')

        balance = income - expenses
        print(f"Balans: {balance}")
        print(f"Umumiy Daromad: {income}")
        print(f"Umumiy Harajatlar: {expenses}")

    def add_data(self, data_type, amount, description=""):
        data = {
            'Sana': datetime.now().strftime("%Y-%m-%d"),
            'Turkum': data_type,
            'Miqdor': amount,
            'Tavsif': description
        }
        self.informations.append(data)
        self.save_data()

    def edit_data(self, searched_data, new_data=None):
        searched_data_str = str(searched_data).lower()
        matches = [i for i, data in enumerate(self.informations)
                   if any(searched_data_str in str(value).lower() for value in data.values())]

        if not matches:
            print("Qidiruvga mos keladigan ma'lumot topilmadi.")
            return None

        print(f"\nQidiruvga asosan {len(matches)} ta ma'lumot topildi:")
        for data_index in matches:
            data = self.informations[data_index]
            print(f"{data_index}: {data}")

        selected_index = int(input("Iltimos, tahrirlamoqchi bo'lgan ma'lumotingizni indeksini kiriting: "))
        if selected_index in matches:
            new_data = {
                'Miqdor': float(input("Miqdorni tahrirlang: ")),
                'Tavsif': input("Ma'lumotni tahrirlang: ")
            }
            self.informations[selected_index].update(new_data)
            self.save_data()
        else:
            print("Siz tanlagan indeksda ma'lumot mavjud emas!")

    def search_informations(self, search_term):
        search_term = str(search_term).lower()
        results = [
            i for i, data in enumerate(self.informations)
            if any(search_term in str(value) for value in data.values())
        ]

        if results:
            print(f"\n{len(results)} ta ma'lumot topildi:")
            for result in results:
                print(f"{result}: {self.informations[result]}")
        else:
            print("Qidiruvga mos keladigan ma'lumot topilmadi.")
