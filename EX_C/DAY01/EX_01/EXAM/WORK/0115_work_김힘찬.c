#include <stdio.h>
#include <stdlib.h>

// ===============================
// Circular Doubly Linked List
// - head is a sentinel (dummy) node
// ===============================

typedef struct Node {
    int data;
    struct Node* prev;
    struct Node* next;
} Node;

// ---------- Utility ----------
static void* xmalloc(size_t sz) {
    void* p = malloc(sz);
    if (!p) {
        perror("malloc");
        exit(1);
    }
    return p;
}

Node* create_list(void) {
    Node* head = (Node*)xmalloc(sizeof(Node));
    head->data = 0;                 // dummy
    head->prev = head;
    head->next = head;
    return head;
}

int is_empty(Node* head) {
    return head->next == head;
}

int size(Node* head) {
    int cnt = 0;
    for (Node* cur = head->next; cur != head; cur = cur->next) cnt++;
    return cnt;
}

// index: 0..(size-1)
// return: pointer to node at index, or NULL if out of range
Node* get_node_at(Node* head, int index) {
    if (index < 0) return NULL;

    int n = size(head);
    if (index >= n) return NULL;

    // 약간 최적화: 앞/뒤 중 가까운 쪽으로 이동
    if (index <= n / 2) {
        Node* cur = head->next;
        for (int i = 0; i < index; i++) cur = cur->next;
        return cur;
    }
    else {
        Node* cur = head->prev;
        for (int i = n - 1; i > index; i--) cur = cur->prev;
        return cur;
    }
}

// ---------- Insert ----------
void insert_before(Node* pos, int value) {
    Node* node = (Node*)xmalloc(sizeof(Node));
    node->data = value;

    node->prev = pos->prev;
    node->next = pos;

    pos->prev->next = node;
    pos->prev = node;
}

// insert at index (0..size)
int insert_at(Node* head, int index, int value) {
    int n = size(head);
    if (index < 0 || index > n) return 0;

    if (index == n) {
        // append: insert before head (tail position)
        insert_before(head, value);
        return 1;
    }
    else {
        Node* pos = get_node_at(head, index);
        insert_before(pos, value);
        return 1;
    }
}

void push_back(Node* head, int value) {
    insert_before(head, value);
}

// ---------- Delete ----------
int delete_at(Node* head, int index) {
    Node* target = get_node_at(head, index);
    if (!target) return 0;

    target->prev->next = target->next;
    target->next->prev = target->prev;
    free(target);
    return 1;
}


int delete_value(Node* head, int value) {
    for (Node* cur = head->next; cur != head; cur = cur->next) {
        if (cur->data == value) {
            cur->prev->next = cur->next;
            cur->next->prev = cur->prev;
            free(cur);
            return 1;
        }
    }
    return 0;
}

// ---------- Update ----------
int update_at(Node* head, int index, int new_value) {
    Node* target = get_node_at(head, index);
    if (!target) return 0;
    target->data = new_value;
    return 1;
}


int update_value(Node* head, int old_value, int new_value) {
    for (Node* cur = head->next; cur != head; cur = cur->next) {
        if (cur->data == old_value) {
            cur->data = new_value;
            return 1;
        }
    }
    return 0;
}

// ---------- Print / Free ----------
void print_list(Node* head) {
    printf("[ ");
    for (Node* cur = head->next; cur != head; cur = cur->next) {
        printf("%d ", cur->data);
    }
    printf("]\n");
}

void free_list(Node* head) {
    Node* cur = head->next;
    while (cur != head) {
        Node* nxt = cur->next;
        free(cur);
        cur = nxt;
    }
    free(head);
}

// ===============================
// Demo
// ===============================
int main(void) {
    Node* head = create_list();

    // 삽입
    push_back(head, 10);
    push_back(head, 20);
    push_back(head, 30);
    print_list(head); // [ 10 20 30 ]

    insert_at(head, 1, 15); // index 1에 15 삽입
    print_list(head);       // [ 10 15 20 30 ]

    // 수정
    update_at(head, 2, 99); // index 2 값을 99로 변경
    print_list(head);       // [ 10 15 99 30 ]

    // 삭제
    delete_at(head, 1);     // index 1 삭제(15 삭제)
    print_list(head);       // [ 10 99 30 ]

    delete_value(head, 99); // 값 99 삭제
    print_list(head);       // [ 10 30 ]

    free_list(head);
    return 0;
}
