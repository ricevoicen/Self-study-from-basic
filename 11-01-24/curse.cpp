#include <iostream>

using namespace std;
int tow_number_add (int one, int two) {
    return one + two;
}

// 创作一个对象
class Person {
    public:
        string name;
        int age;
};

// 创建一个复杂一些的对象示例
class Student {
    public:
        string name;
        int age;
        int score;
};

int main() {
    cout << tow_number_add(1, 2) << endl;
    // use 对象 Person
    Person p;
    p.name = "张三";
    p.age = 18;
    cout << p.name << " " << p.age << endl;
    return 0;
}
