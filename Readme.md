### Data Structure ###

Data structure: A data structure is a way of organizing and storing data in a computer program or system so that it can be accessed and manipulated efficiently. Examples of common data structures include arrays, linked lists, trees, and graphs.

## LinkedList
A linked list is a linear data structure in which elements are stored in a series of nodes, each of which contains a reference or pointer to the next node in the sequence. In other words, each node contains a piece of data and a reference to the next node in the list.
## LinkedList && Arrays
![image](https://user-images.githubusercontent.com/72993155/229142542-670de972-ed15-46cb-a4e1-d2cfce8c01e1.png)
![image](https://user-images.githubusercontent.com/72993155/229361221-de07cb47-bf04-4579-9129-3f8f2526098d.png)


    1- Memory allocation: In an array, memory is allocated in a contiguous block, which means that each element is stored in a fixed memory location. In contrast, a linked list uses dynamic memory allocation, where each element is stored in a separate memory location, connected by pointers.

    2- Size: The size of an array is fixed at the time of creation and cannot be changed. In contrast, a linked list can grow or shrink in size dynamically, as new elements are added or removed.

    3- Insertion and deletion: Inserting or deleting elements in an array can be slow, especially if the array is large, since it requires shifting all the elements after the insertion point. In contrast, inserting or deleting elements in a linked list is generally faster, since it only requires changing a few pointers to re-link the list.

## Stack
is an abstract data type that represents a collection of elements with two principal operations: push, which adds an element to the collection, and pop, which removes the most recently added element that was not yet removed. The elements in a stack are typically arranged in a last-in-first-out (LIFO) order, meaning that the most recently added element is the first one to be removed.

![image](https://user-images.githubusercontent.com/72993155/229360836-8fbf5bcd-1d2e-45db-a200-384c0ea00e1c.png)

## Stack use cases:
    
    - Function calling in any pg language is managed using a stack
    - Undo (Ctrl+Z) functionality in any editor uses stack to track down last set of operations
    - Browser history in web browsers

## Keep in mind : 

    - Push/Pop element : O(1)
    - Search element by value : O(n)
    - List is not recommneded to be used as stack in python because it is a dynamic array; assuming we have a     list of 10 elements (capacity of 10), and we want to insert the 11 th element, so it will go to another memory are and allocate some extra capacity (additional capacity = 10 *2). Memory allocation issue according with copying issue.

    - The recommended approach in python is to use collections.deque()
