#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - adds a new node to the list
 * @head: first node
 * @number: what to add
 * Return: the address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	temp = *head;
	if (*head == NULL)
		*head = new;
	else
	{
		while (temp)
		{
			if (temp->n < number)
			{
				temp->next = new;
				new->next = temp;
				return (new);
				free(new);
			}
			temp = temp->next;
		}
	}
	return (NULL);
	free(new);
}
