from undo_redo.services.undo_redo_service import UndoRedoService

def show_menu():
    print("\n====== UNDO / REDO MENU ======")
    print("1. Perform Action")
    print("2. Undo")
    print("3. Redo")
    print("4. Show Current State")
    print("5. Exit")
    print("=============================")

def main():
    service = UndoRedoService()

    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            action = input("Enter action (text to add): ")
            service.perform_action(action)
            print("✅ Action performed")

        elif choice == "2":
            print("↩ Undo:", service.undo())

        elif choice == "3":
            print("↪ Redo:", service.redo())

        elif choice == "4":
            print("📝 Current State:", service.get_state())

        elif choice == "5":
            print("👋 Exiting program")
            break

        else:
            print("⚠ Invalid choice")

if __name__ == "__main__":
    main()
