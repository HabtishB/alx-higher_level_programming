#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include "lists.h"

/**
 *insert_node -inserts new num to linkedlist 
 * @head: head of the linked list
 * @number: number to insert
 */

listint_t *insert_node(listint_t **head, int number)
{
  listint_t *prev, *current;
  listint_t *new_node;
  unsigned int i = 0;

  new_node = malloc(sizeof(listint_t));

  if(!new_node)
    {
      printf("Error\n");
      return (NULL);
    }
  new_node->n = number;
  current = *head
    while (current)
      {
       if(current->n < number)
	 {
	  i++;
	  prev = current;
	  current = current->next;
	 }
       else
	 break;
      }
  if (!i)
    {
     new_node->next = *head;
     *head = new_node;
     return (new_node);
    }
  new_node->next = prev->next;
  prev->next = new_node;

  return (new_node)
 }
