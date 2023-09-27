class auth():
    def dispaly(self):
        dictionary ={
            "The Catcher in the Rye": "J.D. Salinger",
            "To Kill a Mockingbird": "Harper Lee",
            "1984": "George Orwell",
            "Pride and Prejudice": "Jane Austen",
            "The Great Gatsby": "F. Scott Fitzgerald",
            "The Hobbit": "J.R.R. Tolkien",
            "Harry Potter and the Sorcerer's Stone": "J.K. Rowling",
            "The Hunger Games": "Suzanne Collins",
            "The Da Vinci Code": "Dan Brown",
        }
        return dictionary


class book(auth):
    def dispaly(self, author):
        a=auth()
        b=a.dispaly()
        for i, j in b.items():
            if author.upper() == j.upper():
                return (f"The author of '{i}' is {author}")
        else:
            print(f"'{author}' not found in the dictionary.")

    
author =input("Enter a author name : ")
b =book()
print(b.dispaly(author))
