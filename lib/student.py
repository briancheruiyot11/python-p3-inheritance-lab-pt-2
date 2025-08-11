# Parent class
class Student:
    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")

    def raise_hand(self):
        print("Pick me!")


# Child class
class ChattyStudent(Student):
    def hello(self):
        super().hello()  # Call the parent hello()
        print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")

# raise_hand method
    def raise_hand(self):
        for _ in range(10):
            super().raise_hand()  