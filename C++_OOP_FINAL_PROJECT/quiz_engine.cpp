#include <iostream> // Allows input/output (cin, cout)
#include <cstring> // Allows working with C-style strings

using namespace std; // So we can write cout, cin directly without std:: prefix

struct Question {
    char prompt[100]; // The question text (max 100 characters)
    char choices[4][40];// 4 possible answers (each max 40 characters)
    int correctIdx;  // The index (0 to 3) of the correct choice
};

// Dynamic array of questions
Question* questions = nullptr; // Pointer to dynamically store all questions
int questionCount = 0; // Keeps track of how many questions we have

// Add a new question
void addQuestion(const Question& q) {
    Question* newArr = new Question[questionCount + 1];// Create a new array with one extra slot
    for (int i = 0; i < questionCount; ++i) {
        *(newArr + i) = *(questions + i); // Copy old questions into new array (using pointer arithmetic)
    }
    *(newArr + questionCount) = q;   // Add the new question to the end
    delete[] questions; // Delete old array
    questions = newArr;  // Point to the new array
    ++questionCount;    // Increase the count
}

// Remove a question by index
void removeQuestion(int index) {
    if (index < 0 || index >= questionCount) return;  // Check if index is valid

    Question* newArr = new Question[questionCount - 1]; // Make a smaller array
    for (int i = 0, j = 0; i < questionCount; ++i) {
        if (i == index) continue;  // Skip the question to remove
        *(newArr + j++) = *(questions + i); // Skip the question to remove
    }
    delete[] questions;  // Delete old array
    questions = newArr;   // Update to new array
    --questionCount;  // Decrease count
}

// Abstract base class
class QuizUser {
public:
    virtual int takeQuiz(Question* questions, int n) = 0;// Abstract method: all users must implement this
    virtual ~QuizUser() {
	}   // Virtual destructor for proper cleanup
};

// RegisteredUser
class RegisteredUser : public QuizUser {
public:
    int takeQuiz(Question* questions, int n) override {
        cout << "Registered User taking quiz:\n";
        int score = 0;
        for (int i = 0; i < n; ++i) {
            Question* q = questions + i;   // Pointer to current question
            cout << "Q" << i + 1 << ": " << q->prompt << "\n";
            for (int j = 0; j < 4; ++j)
                cout << j << ": " << q->choices[j] << "\n";
            int answer;
            cout << "Your answer: ";
            cin >> answer;
            if (answer == q->correctIdx) ++score;
        }
        cout << "Score: " << score << "/" << n << "\n";
        return score;
    }
};

// AnonymousUser
class AnonymousUser : public QuizUser {
public:
    int takeQuiz(Question* questions, int n) override {
        cout << "Anonymous User taking quiz:\n";
        int score = 0;
        for (int i = 0; i < n; ++i) {
            Question* q = questions + i;
            cout << "Q" << i + 1 << ": " << q->prompt << "\n";
            for (int j = 0; j < 4; ++j)
                cout << j << ": " << q->choices[j] << "\n";
            int answer;
            cout << "Your answer: ";
            cin >> answer;
            if (answer == q->correctIdx) ++score;
        }
        cout << "Score: " << score << "/" << n << "\n";
        return score;
    }
};
// main function
int main() {
    // Add sample questions, We manually add 2 questions to test the quiz.
    Question q1 = {
        "What is the capital of Rwanda?",
        {"Bujumbura", "Dodoma", "Kigali", "Kampala"},
        2
    };

    Question q2 = {
        "0 + 4 equals?",
        {"3", "4", "5", "6"},
        1
    };

    addQuestion(q1);
    addQuestion(q2);

    // Create dynamic array of QuizUsers
    int userCount = 2;
    QuizUser** users = new QuizUser*[userCount];
    users[0] = new RegisteredUser();
    users[1] = new AnonymousUser();

    // Each user takes the quiz
    for (int i = 0; i < userCount; ++i) {
        users[i]->takeQuiz(questions, questionCount); //automatically calls the right version (Registered or Anonymous).
        cout << "----------------------\n";
    }

    // Cleanup
    for (int i = 0; i < userCount; ++i)
        delete users[i];     // Delete each user
    delete[] users;  // Delete user array
    delete[] questions;  // Delete questions array

    return 0; //Program end successfully without errors..
}

