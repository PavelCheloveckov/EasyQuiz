# EasyQuiz

EasyQuiz is a simple quiz application built using Python. It allows users to create and answer questions in a quiz format.

## Features
- Create custom quizzes
- Answer questions
- Track score

## Installation

Before running the application, make sure you have Python installed. If not, you can download it from the official [Python website](https://www.python.org/downloads/).

### Installing Dependencies

To install the required dependencies for the project, run the following command:

```bash
pip install -r requirements.txt
```

### Creating Executable

If you want to generate an executable `.exe` file to easily run the application without Python, you can use `PyInstaller` to package the application.

Run this command to create the executable:

```bash
pyinstaller --onefile main.py
```

This will generate a single executable file in the `dist` folder.

## Usage

### Running the Application

#### Option 1: Using the executable

1. After building the `.exe` file with `PyInstaller`, navigate to the `dist` folder inside your project directory.
2. Inside the `dist` folder, you will find the `EasyQuiz.exe` file.
3. You can **double-click** the `EasyQuiz.exe` file to run the application.

#### Option 2: Using the Python script

If you prefer to run the Python script directly, use the following command in your terminal or command prompt:

```bash
python main.py
```

### Directory Structure

The directory structure of the project is as follows:

```bash
easyquiz/
│
├── main.py                # The main Python script for the application
├── requirements.txt       # List of dependencies
└── dist/                  # Folder containing the executable (after building with PyInstaller)
```

## MATHEXAM (Optional Feature or Different File)

If **MATHEXAM** refers to a specific feature, file, or system related to this project, please include more details. You can integrate its usage here.

For example:

```markdown
## MATHEXAM

If you are using **MATHEXAM** for additional functionality, navigate to the relevant directory or execute the associated file like so:

```bash
python mathexam.py
```

OR, if it's another `exe`:

```bash
./dist/mathexam.exe
```
