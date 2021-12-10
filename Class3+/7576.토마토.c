#include <stdio.h>
#include <stdlib.h>

#define MAX_QUEUE_SIZE 1000000

typedef struct _Tomato {
	int row;
	int col;
}Tomato;
typedef struct QueueType {
	Tomato data[MAX_QUEUE_SIZE];
	int front, rear;
}QueueType;
void init_queue(QueueType* q) {
	q->front = q->rear = 0;
}
int is_empty(QueueType* q) {
	return (q->front == q->rear);
}
int is_full(QueueType* q) {
	return (q->front == ((q->rear+1)%MAX_QUEUE_SIZE));
}
void enqueue(QueueType* q, Tomato tomato) {
	if (is_full(q)) {
		printf("Queue is full \n");
	}
	else {
		q->rear = (q->rear + 1) % MAX_QUEUE_SIZE;
		q->data[q->rear] = tomato;
	}
}
Tomato dequeue(QueueType* q) {
	if (is_empty(q)) {
		printf("Queue is empty \n");
		exit(1);
	}
	else {
		q->front = (q->front + 1) % MAX_QUEUE_SIZE;
		Tomato data = q->data[q->front];
		return data;
	}
}

int matrix[1000][1000];

int main() {
	int m,n;
	scanf("%d %d", &m, &n); //m : 가로길이, n : 세로길이
	
	for(int i=0;i<n;i++)
		for(int j=0;j<m;j++)
			scanf("%d",&matrix[i][j]);
	
	QueueType T;
	init_queue(&T);
	int depth = 0;
	int left[2] = {0};
	
	Tomato input_data;
	Tomato output_data;
	for(int i=0;i<n;i++)
		for(int j=0;j<m;j++)
			if(matrix[i][j]==1) {
				input_data.row = i;
				input_data.col = j;
				matrix[i][j]=-1;
				enqueue(&T, input_data);
				left[1]++;
			}
	left[0]=left[1];
	left[1]=0;
	while(1) {
		do{
			output_data = dequeue(&T);
			left[0]--;
			printf("\n%d %d\n",left[0], depth);
			if(output_data.row>0 && matrix[output_data.row-1][output_data.col]==0) {
				input_data.row = output_data.row-1;
				input_data.col = output_data.col;
				matrix[input_data.row][input_data.col]=-1;
				enqueue(&T, input_data);
				left[1]++;
				printf("위|%d,%d|",input_data.row, input_data.col);
			}//위
			if(output_data.row<n-1 && matrix[output_data.row+1][output_data.col]==0) {
				input_data.row = output_data.row+1;
				input_data.col = output_data.col;
				matrix[input_data.row][input_data.col]=-1;
				enqueue(&T, input_data);
				left[1]++;
				printf("아래|%d,%d|",input_data.row, input_data.col);
			}//아래
			if(output_data.col>0 && matrix[output_data.row][output_data.col-1]==0) {
				input_data.row = output_data.row;
				input_data.col = output_data.col-1;
				matrix[input_data.row][input_data.col]=-1;
				enqueue(&T, input_data);
				left[1]++;
				printf("왼|%d,%d|",input_data.row, input_data.col);
			}//왼쪽
			if(output_data.col>m-1 && matrix[output_data.row][output_data.col+1]==0) {
				input_data.row = output_data.row;
				input_data.col = output_data.col+1;
				matrix[input_data.row][input_data.col]=-1;
				enqueue(&T, input_data);
				left[1]++;
				printf("오|%d,%d|",input_data.row, input_data.col);
			}//오른쪽
			printf("\n%d\n",left[1]);
		}while(left[0]>0);
		depth++;
		if(left[1]==0)
			break;
		left[0]=left[1];
		left[1] = 0;
	}
	printf("%d",depth);
	return 0;
}