""""
Description: A client program written to verify correctness of 
the activity classes.
Author: ACE Faculty
Edited by: Jashan
Date: 07/18/2025
"""

# REQUIREMENT - add import statements
from contact_list.contact_list import ContactList

# GIVEN:

from PySide6.QtWidgets import QApplication

# GIVEN:
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = ContactList()
    window.show()
    sys.exit(app.exec())