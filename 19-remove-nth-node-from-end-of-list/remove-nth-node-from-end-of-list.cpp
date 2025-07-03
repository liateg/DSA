/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

   class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (!head) return nullptr;

        // Step 1: Find the length of the list
        int len = 0;
        ListNode* temp = head;
        while (temp) {
            len++;
            temp = temp->next;
        }

        // Step 2: Check if we need to remove the head
        if (n == len) {
            ListNode* newHead = head->next;
            delete head; // Prevent memory leak
            return newHead;
        }

        // Step 3: Traverse again to find the node before the one to delete
        temp = head;
        for (int i = 0; i < len - n - 1; i++) {
            temp = temp->next;
        }

        // Step 4: Remove the target node
        ListNode* toDelete = temp->next;
        temp->next = temp->next->next;
        delete toDelete; // Free memory

        return head;
    }
};
