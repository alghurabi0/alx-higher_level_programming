#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL, *next, *first_half = NULL;
	int is_palindrome = 1;

	if (!*head)
		return (1);
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}
	if (fast != NULL)
		slow = slow->next;
	first_half = prev;
	while (first_half != NULL && slow != NULL)
	{
		if (first_half->n != slow->n)
		{
			is_palindrome = 0;
			break;
		}
		first_half = first_half->next;
		slow = slow->next;
	}
	return (is_palindrome);
}
