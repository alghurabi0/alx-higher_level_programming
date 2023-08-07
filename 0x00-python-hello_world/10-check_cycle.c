#include "lists.h"
/**
 * check_cycle - checks for cycles in linked lists
 * @list: head node
 * Return: int
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (head == NULL || head->next == NULL)
		return (0);
	slow = list;
	fast = list->next;
	while (slow != fast)
	{
		if (fast == NULL || fast->next == NULL)
			return (0);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (1);
}
