#include <stdio.h>
#include <stdlib.h>
struct node 
{
	int data;
	struct node *prev;
	struct node *next;
};
struct node *first;
struct node *last;
void DlListcreation(int n);
void displayDlList();
void DlListcreation(int n)
{
    int i, num;
    struct node *start;
 
    if(n >= 1)
    {
        first = (struct node *)malloc(sizeof(int));
        if(first != NULL)
        {
            scanf("%d", &num);
	  first->data = num;
            first->prev = NULL;
            first->next = NULL;
            last = first;
            for(i=2; i<=n; i++)
            {
                start = (struct node *)malloc(sizeof(int));
                if(start != NULL)
                {
                    scanf("%d", &num);
                    start->data = num;
                    start->prev = last;
                    start->next = NULL;
 					last->next = start; 
                    last = start;        
                }
                else
                {
                    break;
                }
            }
        }
    }
}
void displayDlList()
{
    struct node * tmp;
    int n = 1;
    if(first == NULL)
    {
        printf(" No data found in the List yet.");
    }
    else
    {
        tmp = first;
        while(tmp != NULL)
        {
            printf("%d ", tmp->data);
            tmp = tmp->next;
        }
    }
}
void QuickSortList(struct node *left, struct node *right)
{
	struct node *pStart;
	struct node *current; 
	int n;
	if (left == right) return;
	pStart = left;
	current = pStart->next;
	while (1)
	{
		if (pStart->data < current->data)
		{
			n = current->data;
			current->data = pStart->data;
			pStart->data = n;
		}	
		if (current == right) break;
		current = current->next;
	}
	n = left->data;
	left->data = current->data;
	current->data = n;
	struct node *v = current;
	current = current->prev;
	if (current != NULL)
	{
		if ((left->prev != current) && (current->next != left))
			QuickSortList(left, current);
	}
	current = v;
	current = current->next;
	if (current != NULL)
	{
		if ((current->prev != right) && (right->next != current))
			QuickSortList(current, right);
	}
}
int main()
{
    int n;
    scanf("%d", &n);
    DlListcreation(n);
    QuickSortList(first,last); 
    displayDlList();
    return 0;
}