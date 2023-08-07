#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - checks for cycles in linked lists
 * @head: head node
 * Return: int
 */
int check_cycle(listint_t *head)
{
	listint_t *slow = head;
	listint_t *fast = head->next;

	if (head == NULL || head->next == NULL)
		return (0);
	while (slow != fast)
	{
		if (fast == NULL || fast->next == NULL)
			return (0);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (1);
}
