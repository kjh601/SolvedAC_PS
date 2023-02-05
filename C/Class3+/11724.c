#include <stdio.h>
#include <stdlib.h>

#define MAX_QUEUE_SIZE 1000000

typedef struct QueueType
{
  int data[MAX_QUEUE_SIZE];
  int front, rear;
} QueueType;
void init_queue(QueueType *q)
{
  q->front = q->rear = 0;
}
int is_empty(QueueType *q)
{
  return (q->front == q->rear);
}
int is_full(QueueType *q)
{
  return (q->front == ((q->rear + 1) % MAX_QUEUE_SIZE));
}
void enqueue(QueueType *q, int data)
{
  if (is_full(q))
  {
    printf("Queue is full \n");
  }
  else
  {
    q->rear = (q->rear + 1) % MAX_QUEUE_SIZE;
    q->data[q->rear] = data;
  }
}
int dequeue(QueueType *q)
{
  if (is_empty(q))
  {
    printf("Queue is empty \n");
    exit(1);
  }
  else
  {
    q->front = (q->front + 1) % MAX_QUEUE_SIZE;
    int data = q->data[q->front];
    return data;
  }
}

int matrix[1000][1000];
QueueType Q;

int main()
{
  int n, m;
  int node1, node2, tmp;
  int seen[1000] = {0};
  int left = 0;
  int count = 0;

  init_queue(&Q);
  scanf("%d %d", &n, &m);
  for (int i = 0; i < m; i++)
  {
    scanf("%d %d", &node1, &node2);
    matrix[node1 - 1][node2 - 1] = 1;
    matrix[node2 - 1][node1 - 1] = 1;
  }

  for(int i=0;i<n;i++)
  {
    if(seen[i]==0)
    {
      seen[i] = 1;
      enqueue(&Q, i);
      left++;
      count++;
    }
    while (left)
    {
      tmp = dequeue(&Q);
      left--;
      for (int i = 0; i < n; i++)
        if (matrix[tmp][i] == 1 && seen[i] == 0)
        {
          seen[i] = 1;
          enqueue(&Q, i);
          left++;
        }
    }
  }
  printf("%d",count);
  return 0;
}