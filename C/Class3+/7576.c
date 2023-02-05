#include <stdio.h>
#include <stdlib.h>

#define MAX_QUEUE_SIZE 1000000
int matrix[1000][1000];

typedef struct TomatoType
{
	int row;
	int col;
} TomatoType;
typedef struct QueueType
{
	TomatoType data[MAX_QUEUE_SIZE];
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
void enqueue(QueueType *q, TomatoType data)
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
TomatoType dequeue(QueueType *q)
{
	if (is_empty(q))
	{
		printf("Queue is empty \n");
		exit(1);
	}
	else
	{
		q->front = (q->front + 1) % MAX_QUEUE_SIZE;
		TomatoType data = q->data[q->front];
		return data;
	}
}
int is_all_ripe(int row, int col)
{
	for (int i = 0; i < row; i++)
		for (int j = 0; j < col; j++)
			if (matrix[i][j] == 0)
				return 0;
	return 1;
}

int main()
{
	QueueType Q;
	init_queue(&Q);
	int m, n;
	int left[2] = {0};
	int depth = 0;

	scanf("%d %d", &m, &n);

	TomatoType input_tomato;
	TomatoType output_tomato;

	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
		{
			scanf("%d", &matrix[i][j]);
			if (matrix[i][j] == 1)
			{
				input_tomato.row = i;
				input_tomato.col = j;
				enqueue(&Q, input_tomato);
				left[0]++;
				matrix[i][j] = -1;
			}
		}
	if (is_all_ripe(n, m))
	{
		printf("0");
		return 0;
	}

	while (1)
	{
		while (left[0]-- > 0)
		{
			output_tomato = dequeue(&Q);
			if (output_tomato.row > 0 && matrix[output_tomato.row - 1][output_tomato.col] == 0) //À§
			{
				input_tomato.row = output_tomato.row - 1;
				input_tomato.col = output_tomato.col;
				matrix[input_tomato.row][input_tomato.col] = -1;
				enqueue(&Q, input_tomato);
				left[1]++;
			}
			if (output_tomato.row < n - 1 && matrix[output_tomato.row + 1][output_tomato.col] == 0) //¾Æ·¡
			{
				input_tomato.row = output_tomato.row + 1;
				input_tomato.col = output_tomato.col;
				matrix[input_tomato.row][input_tomato.col] = -1;
				enqueue(&Q, input_tomato);
				left[1]++;
			}
			if (output_tomato.col > 0 && matrix[output_tomato.row][output_tomato.col - 1] == 0) //¿Þ
			{
				input_tomato.row = output_tomato.row;
				input_tomato.col = output_tomato.col - 1;
				matrix[input_tomato.row][input_tomato.col] = -1;
				enqueue(&Q, input_tomato);
				left[1]++;
			}
			if (output_tomato.col < m - 1 && matrix[output_tomato.row][output_tomato.col + 1] == 0) //¿À
			{
				input_tomato.row = output_tomato.row;
				input_tomato.col = output_tomato.col + 1;
				matrix[input_tomato.row][input_tomato.col] = -1;
				enqueue(&Q, input_tomato);
				left[1]++;
			}
		}
		if (left[1] == 0)
			break;
		depth++;
		left[0] = left[1];
		left[1] = 0;
	}
	if (is_all_ripe(n, m))
		printf("%d", depth);
	else
		printf("-1");

	return 0;
}