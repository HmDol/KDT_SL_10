#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Person {
    char phoneNo[14];   // "010-1234-5678" (13 chars + '\0')
    char name[10];      // 한글 3~4글자면 멀티바이트로 더 클 수 있음(주의)
    struct Person* next;
} Person;

// ===== 유틸 =====
static Person* createNode(const char* phoneNo, const char* name) {
    Person* node = (Person*)malloc(sizeof(Person));
    if (!node) {
        printf("메모리 할당 실패\n");
        exit(1);
    }
    strncpy(node->phoneNo, phoneNo, sizeof(node->phoneNo) - 1);
    node->phoneNo[sizeof(node->phoneNo) - 1] = '\0';

    strncpy(node->name, name, sizeof(node->name) - 1);
    node->name[sizeof(node->name) - 1] = '\0';

    node->next = NULL;
    return node;
}

void printList(const Person* head) {
    printf("\n[전화번호부]\n");
    printf("---------------------------------\n");
    const Person* cur = head;
    while (cur != NULL) {
        printf("%s (%s)\n", cur->name, cur->phoneNo);
        cur = cur->next;
    }
    printf("---------------------------------\n");
}

void freeList(Person* head) {
    while (head != NULL) {
        Person* tmp = head;
        head = head->next;
        free(tmp);
    }
}

// ===== 1) addBack: 맨 뒤에 추가 =====
void addBack(Person** head, const char* phoneNo, const char* name) {
    Person* newNode = createNode(phoneNo, name);

    if (*head == NULL) {
        *head = newNode;
        return;
    }

    Person* cur = *head;
    while (cur->next != NULL) {
        cur = cur->next;
    }
    cur->next = newNode;
}

// ===== 2) delete: phoneNo로 삭제 =====
int deleteByPhone(Person** head, const char* phoneNo) {
    if (*head == NULL) return 0;

    Person* cur = *head;
    Person* prev = NULL;

    while (cur != NULL) {
        if (strcmp(cur->phoneNo, phoneNo) == 0) {
            // 삭제 대상 발견
            if (prev == NULL) {
                // 첫 노드 삭제
                *head = cur->next;
            }
            else {
                prev->next = cur->next;
            }
            free(cur);
            return 1; // 삭제 성공
        }
        prev = cur;
        cur = cur->next;
    }
    return 0; // 못 찾음
}

// ===== 3) update: phoneNo로 찾아 수정 =====
// 새 번호를 ""(빈 문자열)로 주면 번호 수정 안 함 같은 정책도 가능하지만,
// 여기서는 둘 다 수정한다고 가정.
int updateByPhone(Person* head, const char* targetPhone, const char* newName, const char* newPhone) {
    Person* cur = head;
    while (cur != NULL) {
        if (strcmp(cur->phoneNo, targetPhone) == 0) {
            strncpy(cur->name, newName, sizeof(cur->name) - 1);
            cur->name[sizeof(cur->name) - 1] = '\0';

            strncpy(cur->phoneNo, newPhone, sizeof(cur->phoneNo) - 1);
            cur->phoneNo[sizeof(cur->phoneNo) - 1] = '\0';

            return 1; // 수정 성공
        }
        cur = cur->next;
    }
    return 0; // 못 찾음
}

// ===== 테스트 main =====
int main(void) {
    Person* head = NULL;

    addBack(&head, "010-1111-1111", "이몽룡");
    addBack(&head, "010-2222-3434", "성춘향");
    addBack(&head, "010-3333-1212", "변학도");

    printList(head);

    printf("\n[수정] 010-3333-1212 -> (홍길동, 010-9999-9999)\n");
    if (updateByPhone(head, "010-3333-1212", "홍길동", "010-9999-9999")) {
        printf("수정 성공\n");
    }
    else {
        printf("수정 실패(대상 없음)\n");
    }
    printList(head);

    printf("\n[삭제] 010-2222-3434 삭제\n");
    if (deleteByPhone(&head, "010-2222-3434")) {
        printf("삭제 성공\n");
    }
    else {
        printf("삭제 실패(대상 없음)\n");
    }
    printList(head);

    freeList(head);
    return 0;
}
