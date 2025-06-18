EXPLANATION OF CODE

#include <iostream>: Brings in standard input/output functions like cin and cout.
#include <cstring>: Enables use of C-style string functions (though not strictly used here).

using namespace std;: Allows you to use standard names like cout and cin directly without std:: prefix.

STRUCT DEFINITION: Question
struct Question {
    char prompt[100];
    char choices[4][40];
    int correctIdx;
};
Defines a Question with:
prompt: The question text (max 99 characters + null terminator).
choices[4][40]: 4 possible answer choices, each max 39 characters.
correctIdx: Index (0–3) of the correct answer.

DYNAMIC QUESTIONS ARRAY
Question* questions = nullptr;
int questionCount = 0;
questions: A pointer to a dynamically allocated array of Question.
questionCount: The current number of questions.

ADDING A QUESTION
void addQuestion(const Question& q) {
    Question* newArr = new Question[questionCount + 1];
Allocates a new array newArr that's one element larger.

    for (int i = 0; i < questionCount; ++i) {
        *(newArr + i) = *(questions + i);
    }
Copies existing questions to the new array using pointer arithmetic.
    *(newArr + questionCount) = q;
Adds the new question at the end.

    delete[] questions;
    questions = newArr;
    ++questionCount;
}
Frees the old array and updates questions to point to the new one.

REMOVING A QUESTION
void removeQuestion(int index) {
    if (index < 0 || index >= questionCount) return;
Ensures the index is valid.

    Question* newArr = new Question[questionCount - 1]; Creates a smaller array to hold the updated question list.

    for (int i = 0, j = 0; i < questionCount; ++i) {
        if (i == index) continue;
        *(newArr + j++) = *(questions + i);
    }
Skips the element at index, copying all others.

    delete[] questions;
    questions = newArr;
    --questionCount;
}: Frees the old array and updates the global pointer and count.

ABSTRACT BASE CLASS: QuizUser
class QuizUser {
public:
    virtual int takeQuiz(Question* questions, int n) = 0;
    virtual ~QuizUser() {}
};
QuizUser is an abstract class with a pure virtual method takeQuiz.
The virtual ~QuizUser() destructor ensures proper cleanup via base pointers.

REGISTERED USER CLASS
class RegisteredUser : public QuizUser {
public:
    int takeQuiz(Question* questions, int n) override {
        cout << "Registered User taking quiz:\n";
Overrides takeQuiz to implement quiz behavior for a registered user.

        int score = 0;
        for (int i = 0; i < n; ++i) {
            Question* q = questions + i;
Iterates using pointer arithmetic. q points to each Question.

            cout << "Q" << i + 1 << ": " << q->prompt << "\n";
            for (int j = 0; j < 4; ++j)
                cout << j << ": " << q->choices[j] << "\n";
Displays the question and choices.

            int answer;
            cout << "Your answer: ";
            cin >> answer;
            if (answer == q->correctIdx) ++score;
        }
        cout << "Score: " << score << "/" << n << "\n";
        return score;
    }
}; Reads user input and scores it.

ANONYMOUS USER CLASS
class AnonymousUser : public QuizUser {
public:
    int takeQuiz(Question* questions, int n) override {
        cout << "Anonymous User taking quiz:\n";
Same behavior as RegisteredUser but different label — illustrates polymorphism.

MAIN FUNCTION
int main() {
    Question q1 = {
        "What is the capital of France?",
        {"Berlin", "London", "Paris", "Rome"},
        2
    };
Creates q1 with the correct answer at index 2 ("Paris").
    Question q2 = {
        "2 + 2 equals?",
        {"3", "4", "5", "6"},
        1
    };
Creates another sample question.
    addQuestion(q1);
    addQuestion(q2);
Adds both questions to the dynamic array.

CREATING USERS
    int userCount = 2;
    QuizUser** users = new QuizUser*[userCount];
Dynamically allocates an array of QuizUser* pointers.

    users[0] = new RegisteredUser();
    users[1] = new AnonymousUser();
Creates one registered and one anonymous user.

USERS TAKE QUIZ (POLYMORPHISM)
    for (int i = 0; i < userCount; ++i) {
        users[i]->takeQuiz(questions, questionCount);
        cout << "----------------------\n";
    }
Calls takeQuiz() on each user via the base class pointer.

CLEANUP

    for (int i = 0; i < userCount; ++i)
        delete users[i];
    delete[] users;
    delete[] questions;
Properly deletes all dynamic memory to avoid memory leaks.
