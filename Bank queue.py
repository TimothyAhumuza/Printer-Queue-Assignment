class PrinterQueue:
    def __init__(self):
        self.queue = []
    
    def add_document(self, document_name):
        """Add a document to the print queue"""
        self.queue.append(document_name)
        print(f"Added '{document_name}' to the print queue")
    
    def remove_document(self):
        """Remove and print the next document from the queue"""
        if self.is_empty():
            print("Print queue is empty - nothing to print")
            return None
        document = self.queue.pop(0)
        print(f"Printing: {document}")
        return document
    
    def is_empty(self):
        """Check if the print queue is empty"""
        return len(self.queue) == 0
    
    def show_queue(self):
        """Display the current print queue"""
        if self.is_empty():
            print("Print queue is currently empty")
        else:
            print("Current print queue:")
            for i, doc in enumerate(self.queue, 1):
                print(f"{i}. {doc}")

def main():
    printer = PrinterQueue()
    
    while True:
        print("\nPrinter Queue Management")
        print("1. Add document")
        print("2. Print next document")
        print("3. Check if queue is empty")
        print("4. Show current queue")
        print("5. Exit")
        
        choice = input("Enter your choice(1,2,3,0r 5): ")
        
        if choice == "1":
            doc_name = input("Enter document name: ")
            printer.add_document(doc_name)
        elif choice == "2":
            printer.remove_document()
        elif choice == "3":
            if printer.is_empty():
                print("The print queue is empty")
            else:
                print("The print queue is not empty")
        elif choice == "4":
            printer.show_queue()
        elif choice == "5":
            print("Printer queue system exited")
            break
        else:
            print("Invalid choice, please try again")

if __name__ == "__main__":
    main()
