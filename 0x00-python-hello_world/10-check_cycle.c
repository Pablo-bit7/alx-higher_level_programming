#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
    listint_t *slow = list, *fast = list;

    while (slow && fast && fast->next)
    {
        slow = slow->next;
        fast = fast->next->next;

        /* If there is a cycle, the fast and slow pointers will meet */
        if (slow == fast)
            return (1);
    }

    /* If the loop terminates, there is no cycle */
    return (0);
}
