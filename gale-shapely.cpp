#include <iostream>
#include <vector>
#include <queue>
#include <map>

using namespace std;

bool preference(int womanPrefList[][3], int man, int currentPartner, int newPartner, int n) {
    for (int i = 0; i < n; i++) {
        if (womanPrefList[man][i] == newPartner) return true;
        if (womanPrefList[man][i] == currentPartner) return false;
    }
    return false;
}

void galeShapley(int menPrefList[][3], int womenPrefList[][3], int n) {
    map<int, int> womanPartner;
    bool freeMen[n] = {false};
    queue<int> freeMenQueue;

    for (int i = 0; i < n; i++) {
        freeMenQueue.push(i);
    }

    while (!freeMenQueue.empty()) {
        int man = freeMenQueue.front();
        for (int i = 0; i < n && !freeMen[man]; i++) {
            int woman = menPrefList[man][i];
            if (womanPartner.find(woman) == womanPartner.end()) {
                womanPartner[woman] = man;
                freeMen[man] = true;
                freeMenQueue.pop();
            } else {
                int currentPartner = womanPartner[woman];
                if (preference(womenPrefList, woman, currentPartner, man, n)) {
                    freeMen[currentPartner] = false;
                    freeMenQueue.push(currentPartner);
                    womanPartner[woman] = man;
                    freeMen[man] = true;
                    freeMenQueue.pop();
                }
            }
        }
    }

    for (auto &pair : womanPartner) {
        cout << pair.first << " " << pair.second << endl;
    }
}

int main() {
    int menPrefList[3][3] = {
        {1, 0, 2},
        {0, 2, 1},
        {2, 1, 0}
    };

    int womenPrefList[3][3] = {
        {0, 1, 2},
        {1, 2, 0},
        {2, 0, 1}
    };

    galeShapley(menPrefList, womenPrefList, 3);

    return 0;
}
