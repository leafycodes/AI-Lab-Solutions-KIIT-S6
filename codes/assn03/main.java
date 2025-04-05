class DoublyLinkedList {
    Node head;

    // Node class to represent each element in the doubly linked list
    static class Node {
        int data;
        Node next;
        Node prev;

        Node(int data) {
            this.data = data;
            this.next = null;
            this.prev = null;
        }
    }

    // Method to insert a new node at the end of the list
    public void append(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
        } else {
            Node temp = head;
            while (temp.next != null) {
                temp = temp.next;
            }
            temp.next = newNode;
            newNode.prev = temp;
        }
    }

    // Method to print the list (for verification)
    public void printList() {
        Node temp = head;
        while (temp != null) {
            System.out.print(temp.data + " <=> ");
            temp = temp.next;
        }
        System.out.println("null");
    }

    // Method to reverse the doubly linked list
    public void reverse() {
        if (head == null) {
            return;
        }

        Node current = head;
        Node temp = null;

        // Traverse the list and reverse the next and prev pointers
        while (current != null) {
            temp = current.prev;
            current.prev = current.next;
            current.next = temp;
            current = current.prev;
        }

        // After the loop, temp will point to the previous node of the head, which is now the new head
        if (temp != null) {
            head = temp.prev;
        }
    }

    public static void main(String[] args) {
        DoublyLinkedList list = new DoublyLinkedList();

        // Create a doubly linked list: 1 <=> 2 <=> 3 <=> 4 <=> 5
        list.append(1);
        list.append(2);
        list.append(3);
        list.append(4);
        list.append(5);

        System.out.println("Original List:");
        list.printList();

        // Reverse the doubly linked list
        list.reverse();

        System.out.println("Reversed List:");
        list.printList();
    }
}
