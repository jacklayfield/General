#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#ifdef _WIN32
#include <conio.h>
#else
#include <unistd.h> 
#include <termios.h> 
#include <fcntl.h> 
#endif

using namespace std;

const int WIDTH = 10;
const int HEIGHT = 20;
vector<vector<char>> board(HEIGHT, vector<char>(WIDTH, ' '));
int curX, curY; // Current position of the falling block
vector<vector<int>> curBlock; // Current falling block shape
int curBlockColor; // Current falling block color
bool gameOver = false;

// Define tetromino shapes
const vector<vector<vector<int>>> tetrominos = {
    { {1, 1, 1, 1} }, // I
    { {1, 1, 1}, {0, 1, 0} }, // T
    { {1, 1, 1}, {1, 0, 0} }, // L
    { {1, 1, 1}, {0, 0, 1} }, // J
    { {1, 1}, {1, 1} }, // O
    { {0, 1, 1}, {1, 1, 0} }, // S
    { {1, 1, 0}, {0, 1, 1} } // Z
};

// Function prototypes
void initBoard();
void generateBlock();
bool isValidPosition();
void moveDown();
void mergeBlock();
void drawBoard();
void handleInput();
void update();
#ifdef _WIN32
int kbhit(); // Windows implementation
#else
int kbhit(); // Linux/macOS implementation
#endif

// Function to initialize the game board
void initBoard() {
    for (int i = 0; i < HEIGHT; ++i) {
        for (int j = 0; j < WIDTH; ++j) {
            board[i][j] = ' ';
        }
    }
}

// Function to generate a random block
void generateBlock() {
    int blockIndex = rand() % tetrominos.size();
    curBlock = tetrominos[blockIndex];
    curBlockColor = blockIndex + 1; // Color index starts from 1
    curX = WIDTH / 2 - curBlock[0].size() / 2;
    curY = 0;
}

// Function to check if the current position of the block is valid
bool isValidPosition() {
    for (int i = 0; i < curBlock.size(); ++i) {
        for (int j = 0; j < curBlock[i].size(); ++j) {
            if (curBlock[i][j] && (curX + j < 0 || curX + j >= WIDTH || curY + i >= HEIGHT || board[curY + i][curX + j] != ' ')) {
                return false;
            }
        }
    }
    return true;
}

// Function to move the block down
void moveDown() {
    curY++;
    if (!isValidPosition()) {
        curY--;
        mergeBlock();
        generateBlock();
        if (!isValidPosition()) {
            gameOver = true;
        }
    }
}

// Function to merge the block with the board when it reaches the bottom
void mergeBlock() {
    for (int i = 0; i < curBlock.size(); ++i) {
        for (int j = 0; j < curBlock[i].size(); ++j) {
            if (curBlock[i][j]) {
                board[curY + i][curX + j] = '0' + curBlockColor;
            }
        }
    }
}

// Function to draw the game board
void drawBoard() {
    system("clear"); // Clear the screen
    for (int i = 0; i < HEIGHT; ++i) {
        for (int j = 0; j < WIDTH; ++j) {
            cout << board[i][j];
        }
        cout << endl;
    }
}

// Function to handle player input
void handleInput() {
    if (kbhit()) {
        char key = getchar();
        switch (key) {
            case 'a':
                curX--;
                if (!isValidPosition()) {
                    curX++;
                }
                break;
            case 'd':
                curX++;
                if (!isValidPosition()) {
                    curX--;
                }
                break;
            case 's':
                moveDown();
                break;
            case 'q':
                gameOver = true;
                break;
        }
    }
}

// Function to update the game state
void update() {
    moveDown();
}

#ifdef _WIN32
// Windows implementation of kbhit() using _kbhit()
int kbhit() {
    return _kbhit();
}
#else
// Linux/macOS implementation of kbhit() using termios
int kbhit() {
    struct termios oldt, newt;
    int ch;
    int oldf;

    tcgetattr(STDIN_FILENO, &oldt);
    newt = oldt;
    newt.c_lflag &= ~(ICANON | ECHO);
    tcsetattr(STDIN_FILENO, TCSANOW, &newt);
    oldf = fcntl(STDIN_FILENO, F_GETFL, 0);
    fcntl(STDIN_FILENO, F_SETFL, oldf | O_NONBLOCK);

    ch = getchar();

    tcsetattr(STDIN_FILENO, TCSANOW, &oldt);
    fcntl(STDIN_FILENO, F_SETFL, oldf);

    if(ch != EOF) {
        ungetc(ch, stdin);
        return 1;
    }

    return 0;
}
#endif

int main() {
    srand(time(NULL)); // Seed the random number generator
    initBoard();
    generateBlock();
    while (!gameOver) {
        drawBoard();
        handleInput();
        update();
        #ifndef _WIN32
        usleep(300000); // Adjust the speed of the falling blocks (300000 microseconds = 0.3 seconds)
        #endif
    }
    cout << "Game Over!" << endl;
    return 0;
}
